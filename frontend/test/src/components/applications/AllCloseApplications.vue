<template v-slot:activator="{ props }">
    <div class="text-h3 py-6 mx-10 text-left">Закрытые заказы</div>

    <div class="py-6 mx-10 d-flex justify-center">
        <v-col>
            <div v-for="app in applications">
                <v-hover v-slot="{ isHovering, props }" >
                    <v-card
                        v-bind="props"
                        class="my-2 pa-6 mx-14 d-flex flex-row"
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

                            <b class="pr-2">Закрыт:</b> 
                            {{ app.date_close }}
                    </v-card>
                </v-hover>
            </div>
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
            this.get_all_close_applications()
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

            get_all_close_applications(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/applications/show_all_close_application')
                .then (response =>{
                    for (let res of response.data){
                        this.applications.push({
                            id: res.id,
                            date_create: this.format_date(res.date_create),
                            date_start_work: this.format_date(res.date_start_work),
                            date_end_work: this.format_date(res.date_end_work),
                            date_close: this.format_date(res.date_close)
                        })
                    }
                })
            }
        }




    }
</script>