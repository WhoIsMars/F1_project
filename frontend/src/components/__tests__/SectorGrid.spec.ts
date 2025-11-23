import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import SectorGrid from '../SectorGrid.vue'
import { createPinia, setActivePinia } from 'pinia'
import { useRaceStore } from '../../stores/race'

describe('SectorGrid', () => {
    it('renders sector times correctly', () => {
        setActivePinia(createPinia())
        const store = useRaceStore()

        store.data = {
            race: 'Test GP',
            lap: 1,
            drivers: [
                {
                    id: 'verstappen',
                    position: 1,
                    lapTime: '1:20.000',
                    winProbability: 90,
                    sectors: { s1: 21.5, s2: 30.0, s3: 22.0 }
                }
            ]
        }

        const wrapper = mount(SectorGrid)

        expect(wrapper.text()).toContain('VER')
        expect(wrapper.text()).toContain('21.500')
        expect(wrapper.text()).toContain('30.000')
        expect(wrapper.text()).toContain('22.000')
    })
})
