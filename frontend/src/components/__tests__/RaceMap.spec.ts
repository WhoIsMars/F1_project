import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import RaceMap from '../RaceMap.vue'
import { createPinia, setActivePinia } from 'pinia'
import { useRaceStore } from '../../stores/race'

describe('RaceMap', () => {
    it('renders driver dots', () => {
        setActivePinia(createPinia())
        const store = useRaceStore()

        store.data = {
            race: 'Test GP',
            lap: 1,
            drivers: [
                {
                    id: 'max_verstappen',
                    code: 'VER',
                    team: 'red_bull',
                    position: 1,
                    lapTime: '1:20.000',
                    winProbability: 90,
                    coordinates: { x: 50, y: 50 }
                }
            ]
        }

        const wrapper = mount(RaceMap)

        // Check if dot exists
        const dot = wrapper.find('.rounded-full.border-2')
        expect(dot.exists()).toBe(true)
        expect(dot.text()).toBe('1')
    })
})
