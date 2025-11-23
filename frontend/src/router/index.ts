import { createRouter, createWebHistory } from 'vue-router'
import Qualifying from '../views/Qualifying.vue'
import Race from '../views/Race.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            redirect: '/race'
        },
        {
            path: '/qualifying',
            name: 'qualifying',
            component: Qualifying
        },
        {
            path: '/race',
            name: 'race',
            component: Race
        }
    ]
})

export default router
