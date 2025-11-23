import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import DriverList from '../DriverList.vue'
import { createPinia, setActivePinia } from 'pinia'
import { useRaceStore } from '../../stores/race'

describe('DriverList', () => {
    it('renders driver list correctly', async () => {
        setActivePinia(createPinia())
        const store = useRaceStore()

        // Mock data
        store.data = {
            race: 'Test GP',
            lap: 1,
            drivers: [
                { id: 'max_verstappen', code: 'VER', team: 'red_bull', position: 1, lapTime: '1:20.000', winProbability: 90 },
                { id: 'charles_leclerc', code: 'LEC', team: 'ferrari', position: 2, lapTime: '1:20.500', winProbability: 10 }
            ]
        }

        const wrapper = mount(DriverList)

        expect(wrapper.text()).toContain('VER')
        expect(wrapper.text()).toContain('LEC')
        expect(wrapper.text()).toContain('1:20.000')
    })

    it('shows waiting message when no drivers', () => {
        setActivePinia(createPinia())
        const wrapper = mount(DriverList)
        expect(wrapper.text()).toContain('Waiting for live timing data')
    })
})
