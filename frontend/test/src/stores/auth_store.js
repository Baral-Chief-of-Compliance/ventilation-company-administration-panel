import { defineStore } from "pinia";
import axios from "axios";


export const useAuthStore = defineStore({
    id: 'user',
    state: () => ({
      login: '',
      name: '',
      surname: '',
      patronymic: '',
      phone: '',
      JWT: '',
      op_id: ''
    }),

    actions: {
        async login(login, password){

            let JWT = ''

            axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/login', {
                login: login,
                password: password
            }).then(
                response => (
                    JWT = response.data.token
                )
            )

            localStorage.setItem('user', {
                'login': 'admin',
                'name': 'Кто',
                'surname': 'Я',
                'patronymic': 'Ебаный',
                'phone': 'Стыд',
                'JWT': JWT,
                'op_id': '1'
            })

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