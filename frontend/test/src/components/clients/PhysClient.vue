<template v-slot:activator="{ props }">
    <div class="text-h3 py-6 mx-10 text-left">Физическое лицо</div>

    <v-container class="d-flex justify-center">

        <v-col>
            <div>
                <span class="text-h5 my-2 pa-6 mx-14">ФИО</span>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row">

                    <b class="pr-2">Фамилия: </b>  {{ phys.surname }} 
                    <v-spacer></v-spacer>

                    <b class="pr-2">Имя:</b> {{ phys.name }} 
                    <v-spacer></v-spacer>  

                    <b class="pr-2">Отчество:</b>  {{ phys.patronymic }} 
                </v-card>
            </div>

            <div class="mt-15">
                <span class="text-h5 my-2 pa-6 mx-14">Телефон</span>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row">
                    <b class="pr-2">Номер: </b>  {{ phys.phone }} 
                </v-card>
            </div>

            <div class="mt-15">
                <span class="text-h5 my-2 pa-6 mx-14">Адрес</span>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row">

                    <b class="pr-2">Город: </b>  {{ phys.town }}
                    <v-spacer></v-spacer> 

                    <b class="pr-2">Улица: </b>  {{ phys.street }}
                    <v-spacer></v-spacer> 

                    <b class="pr-2">Дом: </b>  {{ phys.house }}
                    <v-spacer></v-spacer> 

                    <b class="pr-2">Корпус: </b>  {{ phys.frame }}
                    <v-spacer></v-spacer> 

                    <b class="pr-2">Квартира: </b>  {{ phys.apartment }}
                    <v-spacer></v-spacer> 
                </v-card>
            </div>

            <div class="mt-15">
                <span class="text-h5 my-2 pa-6 mx-14">Заказы</span>
                <div v-for="app in phys.applications">
                    <v-hover v-slot="{ isHovering, props }" >
                        <v-card  class="my-2 pa-6 mx-14 d-flex flex-row"
                            v-bind="props"
                            :color="isHovering ? 'indigo': undefined"
                            :to="{ name: 'application_inf', params: {id: app.id}}"
                        >

                            <b class="pr-2">Создан: </b>  
                            {{ this.format_date(app.date_create) }}
                            <v-spacer></v-spacer>

                            <b class="pr-2">Начало работы: </b> 
                            {{ this.format_date(app.date_start_work) }}
                            <v-spacer></v-spacer>

                            <b class="pr-2">Конец работы: </b>
                            {{ this.format_date(app.date_end_work) }}
                            <v-spacer></v-spacer>

                            <b class="pr-2">Закрыт: </b>
                            {{ this.format_date(app.date_close) }}
                            <v-spacer></v-spacer>

                        </v-card>
                    </v-hover>
                </div>
            </div>
        </v-col>

    </v-container>
</template>

<script>
import axios from 'axios';


export default{
    data(){
        return{
            phys: {
                applications: []
            }
        }
    },

    mounted(){
        this.get_data()
    },

    methods: {
        get_data(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/clients/phys_clients/${this.$route.params.id}`)
            .then(response => {
                this.phys = response.data
            })
        },

        format_date(date){
            if (date === null){
                return 'не закрыт'
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
        }
    }
}
</script>