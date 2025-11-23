import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { RaceData } from '../types'

export const useRaceStore = defineStore('race', () => {
    const data = ref<RaceData | null>(null)
    const isConnected = ref(false)
    let socket: WebSocket | null = null

    function connect() {
        if (socket && (socket.readyState === WebSocket.OPEN || socket.readyState === WebSocket.CONNECTING)) return

        // In production, this URL should be configurable
        socket = new WebSocket('ws://localhost:8000/ws')

        socket.onopen = () => {
            isConnected.value = true
            console.log('WebSocket connected')
        }

        socket.onmessage = (event) => {
            try {
                const payload = JSON.parse(event.data)
                data.value = payload
            } catch (e) {
                console.error('Failed to parse WebSocket message', e)
            }
        }

        socket.onclose = () => {
            isConnected.value = false
            socket = null
            console.log('WebSocket disconnected, retrying in 3s...')
            setTimeout(connect, 3000)
        }

        socket.onerror = (err) => {
            console.error('WebSocket error:', err)
            socket?.close()
        }
    }

    return {
        data,
        isConnected,
        connect
    }
})
