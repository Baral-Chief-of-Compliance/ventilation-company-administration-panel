<template>
    <div class="text-h3 py-6 mx-10">Добавить клиента</div>

    <v-form v-model="valid">
        <v-container class="d-flex justify-center">
            <v-col>
                <v-row class="mx-10">
                    <v-text-field
                        v-model="surname"
                        label="Фамилия"
                        color="indigo"
                        required
                        class="mx-5"
                    ></v-text-field>

                    <v-text-field
                        v-model="name"
                        label="Имя"
                        color="indigo"
                        required
                        class="mx-5"
                    ></v-text-field>

                    <v-text-field
                        v-model="patronymic"
                        label="Отчество"
                        color="indigo"
                        class="mx-5"
                    ></v-text-field>

                    <v-text-field
                        v-model="phone"
                        label="Телефон"
                        color="indigo"
                        class="mx-5"
                        required
                    ></v-text-field>
                </v-row >

                <v-row class="mx-13 mt-15">

                        <v-radio-group v-model="selected">
                            <v-radio 
                            label="Физическое лицо" 
                            value="phys" 
                            color="indigo"
                            
                            >
                            </v-radio>
                            <v-radio 
                            label="Юридическое лицо" 
                            value="entity" 
                            color="indigo"
                            >
                        </v-radio>
                        </v-radio-group>

                            <v-text-field
                                v-show="selected === 'phys'"
                                v-model="town"
                                label="Город"
                                color="indigo"
                            ></v-text-field>

                            <v-text-field
                                v-show="selected === 'phys'"
                                v-model="street"
                                label="Улица"
                                color="indigo"
                            ></v-text-field>
 
                            <v-text-field
                                v-show="selected === 'phys'"
                                v-model="house"
                                label="Дом"
                                color="indigo"
                            ></v-text-field>

                            <v-text-field
                                v-show="selected === 'phys'"
                                v-model="frame"                            
                                label="Корпус"
                                color="indigo"
                            ></v-text-field>

                            <v-text-field
                                v-show="selected === 'phys'"
                                v-model="apartment"
                                label="Квартира"
                                color="indigo"
                            ></v-text-field>



                        <v-text-field
                            v-show="selected === 'entity'"
                            v-model="name_of_company"
                            label="Название компании"
                            color="indigo"
                        ></v-text-field>

                        <v-text-field
                            v-show="selected === 'entity'"
                            v-model="inn"
                            label="ИНН"
                            color="indigo"
                        ></v-text-field>
                    
                </v-row>
            
                <v-row class="mx-14 mt-15">
                    <v-btn 
                        color="indigo" 
                        size="x-large" 
                        block
                        @click="set_null"
                        >
                        Добавить клиента
                    </v-btn>
                </v-row>

            </v-col>
        </v-container>
    </v-form>
</template>

<script>
import axios from 'axios'

    export default {
        data () {
        return {
            selected: null,
            surname: null,
            name: null,
            patronymic: null,
            phone: null,
            town: null,
            street: null,
            house: null,
            frame: null,
            apartment: null,
            name_of_company: null,
            inn: null
        }
        },
        methods:{
            submit: function(){
                if (this.selected === 'phys'){
                    axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/clients/add_phys_client', {
                        surname : this.surname,
                        name : this.name,
                        patronymic : this.patronymic,
                        phone : this.phone,
                        town : this.town,
                        street : this.street,
                        house : this.house,
                        frame : this.frame,
                    })
                }
                else if (this.selected === 'entity'){
                    axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/clients/add_entity_client',{
                        surname : this.surname,
                        name : this.name,
                        patronymic : this.patronymic,
                        phone : this.phone,
                        name_of_company : this.name_of_company,
                        inn : this.inn
                    })

                }

                this.set_null()
            },
            set_null(){
                    this.selected = null,
                    this.surname = null,
                    this.name = null,
                    this.patronymic = null,
                    this.phone = null,
                    this.town = null,
                    this.street = null,
                    this.house = null,
                    this.frame = null,
                    this.apartment = null,
                    this.name_of_company = null,
                    this.inn = null
            }
        }
    }
</script>