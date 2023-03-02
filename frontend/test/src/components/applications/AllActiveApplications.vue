<template>
     <div class="text-h3 py-6 mx-10 text-left">Активные заказы</div>

     <div class="py-6 mx-10 d-flex justify-center">
        <v-col>
            <v-card v-for="app in applications" class="my-2 pa-6 mx-14 d-flex flex-row">
                <b class="pr-2">Создан: </b>  {{ app.date_create }} <v-spacer></v-spacer> <b class="pr-2">Начало работы:</b> {{ app.date_start_work }} <v-spacer></v-spacer> <b class="pr-2">Конец работы:</b>  {{ app.date_end_work }} <v-spacer></v-spacer> <v-card>{{ app.days_are_left }}</v-card>
            </v-card>
        </v-col>
     </div>
</template>

<script>
import axios from 'axios';


    export default{

        data: () => ({
            applications: []
        }),

        mounted(){
            this.get_all_application()
        },

        methods: {
            format_date(date){
                var d = new Date(date)

                var dd = d.getDate()
                if (dd < 10) dd = '0' + dd

                var mm = d.getMonth() + 1
                if (mm < 10) mm = '0' + mm

                var yy = d.getFullYear()

                return dd + '.' + mm + '.' + yy
            },
            get_all_application(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/applications/show_all_active_application')
                .then (response =>{
                    var d = new Date()
                    for (let res of response.data){
                        var d_end = new Date(res.date_end_work)
                        var difference =  Math.abs(d_end - d) / (1000*60*60*24)
                        this.applications.push({
                            id: res.id,
                            date_create: this.format_date(res.date_create),
                            date_start_work: this.format_date(res.date_start_work),
                            date_end_work: this.format_date(res.date_end_work),
                            days_are_left: Math.ceil(difference)
                        })
                    }
                })
            }
        }


    }
</script>