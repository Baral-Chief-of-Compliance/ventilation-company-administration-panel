<template v-slot:activator="{ props }">
    <div class="text-h3 py-6 mx-10 text-left">Клиенты</div>

    <div class="py-6 mx-10 d-flex justify-center">
        <v-radio-group inline color="indigo" v-model="radio">
            <v-radio label="Физические лица" value="phys"></v-radio>
            <v-radio label="Юридические лица" value="entity"></v-radio>
        </v-radio-group>
    </div>

    <div class="py-6 mx-10 d-flex justify-center" >
        <v-col v-show="radio === 'phys'">
            <div v-for="phys in phys_clients">
                <v-hover v-slot="{ isHovering, props }" >
                    <v-card  class="my-2 pa-6 mx-14 d-flex flex-row"
                        v-bind="props"
                        :color="isHovering ? 'indigo': undefined"
                        :to="{ name: 'phys_client_info', params: {id: phys.id}}"
                    >
                        <b class="pr-2">Фамилия: </b>  {{ phys.surname }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Имя:</b> 
                        {{ phys.name }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Отчество:</b>  
                        {{ phys.patronymic }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Телефон:</b> 
                        {{ phys.phone }}
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Адрес:</b> 
                        г. {{ phys.town }} 
                        ул. {{ phys.street }} 
                        д. {{ phys.house }} 
                        к. {{ phys.frame }}
                        кв. {{ phys.apartment }}
                    </v-card>
                </v-hover>

            </div>
        </v-col>

        <v-col v-show="radio === 'entity'">
            <div v-for="ent in entity_clients">
                <v-hover v-slot="{ isHovering, props }" >
                    <v-card  class="my-2 pa-6 mx-14 d-flex flex-row"
                        v-bind="props"
                        :color="isHovering ? 'indigo': undefined"
                    >
                        <b class="pr-2">Фамилия: </b>  {{ ent.surname }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Имя:</b> 
                        {{ ent.name }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Отчество:</b>  
                        {{ ent.patronymic }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Телефон:</b> 
                        {{ ent.phone }}
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Компания:</b> 
                        {{ ent.name_of_company }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">ИНН:</b> 
                        {{ ent.inn }}
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
        phys_clients: [],
        entity_clients: [],
        radio: ''
    }),

    mounted(){
        this.get_entity_clients()
        this.get_phys_clients()
    },

    methods: {
        get_phys_clients(){
            axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/clients/phys_clients')
            .then(response => (this.phys_clients = response.data) )
        },

        get_entity_clients(){
            axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/clients/entity_clients')
            .then(response => (this.entity_clients = response.data) )
        }
    }  
}
</script>