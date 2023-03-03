<template>
     <div class="text-h3 py-6 mx-10 text-left"> Заказ № {{ $route.params.id }} </div>
     <v-container class="d-flex justify-center">
        <v-col>
            <v-card class="my-2 pa-6 mx-14 d-flex flex-row"></v-card>
            <span class="text-h5 my-2 pa-6 mx-14">Материалы</span>
            <v-card v-for="mat in inf.materials" class="my-2 pa-6 mx-14 d-flex flex-row">
                <span class="pr-2">Название: </span> <b>{{ mat.name }}</b> <span class="px-2">Количество:</span> <b>{{ mat.quantity }}</b>
            </v-card>
            <span class="text-h5 my-2 pa-6 mx-14">Клиент</span>
            <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
                <span class="pr-2">Имя: </span> <b>{{ inf.name }}</b> <span class="px-2">Фамилия:</span> <b>{{ inf.surname }}</b> <span class="px-2">Отчество:</span> <b>{{ inf.patronymic }}</b> <span class="px-2">Телефон:</span> <b>{{ inf.phone }}</b>
            </v-card>
        </v-col>
     </v-container>
</template>

<script>
import axios from 'axios';


export default{
    data(){
        return{
            inf: {}
        }
    },

    mounted(){
        this.get_data()
    },

    methods: {
        get_data(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/applications/${this.$route.params.id}`)
            .then(response => (
                this.inf = response.data
            ))
        }
    }

}
</script>