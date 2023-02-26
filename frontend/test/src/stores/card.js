import { defineStore } from "pinia";


export const useCartStore = defineStore({
    id: 'cart',
    state: () => ({
        rawItems: {}
    }),

    actions: {
        addItem(id, quantity){
            this.rawItems[id] = quantity
        },
        removeItem(id){
            delete this.rawItems[id]
        }
    }
})
