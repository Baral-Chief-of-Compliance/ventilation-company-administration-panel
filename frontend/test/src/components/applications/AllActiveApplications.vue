<template v-slot:activator="{ props }">
     <div class="text-h3 py-6 mx-10 text-left">Активные заказы</div>

     <div class="py-6 mx-10 d-flex justify-center">
        <v-col>
            <v-hover v-slot="{ isHovering, props }" >
                <v-card 
                    v-bind="props"
                     v-for="app in applications" class="my-2 pa-6 mx-14 d-flex flex-row"
                    :color="isHovering ? 'indigo': undefined"
                    :to="{ name: 'application_inf', params: {id: app.id}}"
                >
                    <b class="pr-2">Создан: </b>  
                    {{ app.date_create }} 
                    <v-spacer></v-spacer> 
                    
                    <b class="pr-2">Начало работы:</b> 
                    {{ app.date_start_work }} 
                    <v-spacer></v-spacer> 
                    
                    <b class="pr-2">Конец работы:</b> 
                     {{ app.date_end_work }} 
                     <v-spacer></v-spacer> 
                     
                     <v-card 
                        v-show="!app.delay_status" 
                        class="pa-1" color="green-accent-1" 
                        outline><span class="pr-1"
                    >
                        Осталось:</span>{{ app.days_are_left }} 
                        <span class="pl-1">дней</span>
                    </v-card> <v-card v-show="app.delay_status" class="pa-1" color="red-accent-1" outline><span class="pr-1">Задержка в:</span>{{ app.days_are_left }} <span class="pl-1">дней</span></v-card>
                </v-card>
            </v-hover>

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

                        if (d_end >= d){
                            var delay_status = false
                        }
                        else {
                            var delay_status = true
                        }
                        var difference =  Math.abs(d_end - d) / (1000*60*60*24)
                        this.applications.push({
                            id: res.id,
                            date_create: this.format_date(res.date_create),
                            date_start_work: this.format_date(res.date_start_work),
                            date_end_work: this.format_date(res.date_end_work),
                            days_are_left: Math.ceil(difference),
                            delay_status: delay_status
                        })
                    }
                })
            }
        }


    }
</script>