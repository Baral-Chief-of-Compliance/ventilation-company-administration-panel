<template>

    <v-app :style="{ background: '#3F51B5' }" >
        <div class="d-flex justify-center">

            <v-card width="500" height="300" class="mt-15 pa-6">
                <v-card-title>
                    Административная панель
                </v-card-title>
                <v-card-subtitle>
                    ООО "Вентелятор"
                </v-card-subtitle>
                <v-card-item>
                    <v-text-field
                        v-model="login"
                        label="Логин"
                        color="indigo"
                    >
                    </v-text-field>
                    <v-text-field
                        v-model="password"
                        label="Пароль"
                        color="indigo"
                    >
                    </v-text-field>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="green" @click="enter_into_system(login, password)">Войти</v-btn>
                    </v-card-actions>
                </v-card-item>
            </v-card>

        </div>

    </v-app>

</template>

<script>
import { useAuthStore } from '@/stores/auth_store';
 
const store = useAuthStore()
    export default{
        data(){
            return{
                login: null,
                password: null
            }
        },
        methods: {
            enter_into_system(login, password){
                store.login(login, password)

                this.login = '',
                this.password = ''
            }
        }
    }
</script>