import { defineStore } from "pinia";
import axios from "axios";


export const useAuthStore = defineStore('user',{
    state: () => {
        return {
            authUser: null
        }
    },
    getters: {
        user: (state) => state.authUser
    },
    actions: {
        async login(login, password){

            let JWT = ''

            axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/login', {
                login: login,
                password: password
            }).then(
                response => (
                    this.authUser = response.data.token
                )
            )
            // router.push('/');
        },
        logout(){
            this.login = ''
            this.name = ''
            this.surname = ''
            this.patronymic = ''
            this.phone = ''
            this.JWT = ''
            this.op_id = ''
            localStorage.removeItem('user')
            // router.push('/login')
        }
    }
})