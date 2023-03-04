<template>
     <div class="text-h3 py-6 mx-10 text-left"> Заказ № {{ $route.params.id }} </div>
     <v-container class="d-flex justify-center">
        <v-col>

            <div>
                <span class="text-h5 my-2 pa-6 mx-14">Даты</span>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
                    <b class="pr-2">Создан: </b>  {{ inf.date_create }} 
                    <v-spacer></v-spacer> 
                    <b class="pr-2">Начало работы:</b> {{ inf.date_start_work }} 
                    <v-spacer></v-spacer> 
                    <b class="pr-2">Конец работы:</b>  {{ inf.date_end_work }} 
                    <v-spacer></v-spacer>
                    <b v-show="date_close_status" class="pr-2">Дата закрытия:</b>  {{ inf.date_close }}
                    <v-spacer></v-spacer>
                    <b v-show="date_close_status"  class="pr-2">Дней задержки:</b>  {{ inf.days_of_delay }}
                    <v-spacer></v-spacer>
                    <v-btn v-show="!date_close_status" color="indigo" @click="close_application" >Закрыть</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn variant="outlined" color="red">Удалить</v-btn>
                </v-card>
            </div>

            <div class="mt-15">
                <span class="text-h5 my-2 pa-6 mx-14">Клиент</span>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
                    <span class="pr-2">Имя: </span> <b>{{ inf.name }}</b> <span class="px-2">Фамилия:</span> <b>{{ inf.surname }}</b> <span class="px-2">Отчество:</span> <b>{{ inf.patronymic }}</b> <span class="px-2">Телефон:</span> <b>{{ inf.phone }}</b>
                </v-card>
            </div>

            <div class="mt-15">
                <span class="text-h5 my-2 pa-6 mx-14">Материалы</span>
                <v-card v-for="mat in inf.materials" class="my-2 pa-6 mx-14 d-flex flex-row">
                    <span class="pr-2">Название: </span> <b>{{ mat.name }}</b> <span class="px-2">Количество:</span> <b>{{ mat.quantity }}</b>
                </v-card>
            </div>


            <div class="mt-15">
                <span class="text-h5 my-2 pa-6 mx-14">Адрес Склада</span>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
                    <span class="pr-2">Город: </span> <b>{{ inf.stock_inf.town }}</b> <span class="px-2">Улица:</span> <b>{{ inf.stock_inf.street }}</b> <span class="px-2">Дом:</span> <b>{{ inf.stock_inf.house }}</b> <span class="px-2">Корпус:</span> <b>{{ inf.stock_inf.frame }}</b>
                </v-card>
            </div>

    
            <div class="mt-15">
                <span class="text-h5 my-2 pa-6 mx-14">Адрес работы</span>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
                    <span class="pr-2">Город: </span> <b>{{ inf.town }}</b> <span class="px-2">Улица:</span> <b>{{ inf.street }}</b> <span class="px-2">Дом:</span> <b>{{ inf.house }}</b> <span class="px-2">Корпус:</span> <b>{{ inf.frame }}</b>
                </v-card>
            </div>

            

        </v-col>
     </v-container>
     <span class="text-h5 my-2 pa-6 mx-14">Карта</span>
     <div class="py-6 mx-10 d-flex justify-center">
        
        <MapApllication :odr_latitude="inf.latitude" 
                        :odr_longitude="inf.longitude" 
                        :st_latitude="inf.stock_inf.latitude"
                        :st_longitude="inf.stock_inf.longitude"
        />
     </div>
     <span class="text-h5 my-2 pa-6 mx-14">Легенда карты</span>
     <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
        <v-icon color="red" icon="mdi-map-marker"></v-icon> <sapn class="pr-6">- маркер адреса заказа</sapn> <v-icon color="blue" icon="mdi-map-marker"></v-icon> - маркер склада
     </v-card>
</template>

<script>
import axios from 'axios';
import MapApllication from '../Map/MapApllication.vue';


export default{
    data(){
        return{
            inf: { stock_inf: {}, date_close_status: true}
        }
    },

    components: {
        MapApllication
    },

    mounted(){
        this.get_data()
    },

    methods: {
        format_date(date){
                if (date === null){
                    this.inf.date_close_status = false
                    return date
                }
                else{
                    var d = new Date(date)

                    var dd = d.getDate()
                    if (dd < 10) dd = '0' + dd

                    var mm = d.getMonth() + 1
                    if (mm < 10) mm = '0' + mm

                    var yy = d.getFullYear()

                    return dd + '.' + mm + '.' + yy
                }

            },

        get_data(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/applications/${this.$route.params.id}`)
            .then(response => {

                response.data.date_create = this.format_date(response.data.date_create)
                response.data.date_end_work = this.format_date(response.data.date_end_work)
                response.data.date_start_work = this.format_date(response.data.date_start_work)
                response.data.date_close = this.format_date(response.data.date_close)

                this.inf = response.data
            }

            )
        },

        close_application(){
            let date_close = new Date()
            let date_end_work = new Date(this.inf.date_end_work)

            if (date_end_work >= date_close){
                var days_of_delay = 0
            }
            else{
                var days_of_delay = Math.abs(date_close - date_end_work) / (1000*60*60*24)
            }

            axios.patch(`http://127.0.0.1:5000/admin_panel/api/v1.0/applications/${this.$route.params.id}`,
            {
                date_close: date_close,
                days_of_delay: days_of_delay
            }
            )
        }
    }

}
</script>