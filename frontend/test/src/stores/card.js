import { defineStore } from "pinia";
import axios from "axios";


export const useCartStore = defineStore({
    id: 'cart',
    state: () => ({
        rawItems: {}
    }),

    getters: {
        items(state){
            return state.rawItems
        }
    },

    actions: {
        addItem(id, quantity){
            this.rawItems[id] = quantity
        },

        removeItem(id){
            delete this.rawItems[id]
        },

        sendData(){
                axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/applications/add_materials_in_order',
                {
                    items: this.rawItems
                })
                this.rawItems = {}

        }
    }
})
