<template>
    <div class="text-h3 py-6 mx-10">Добавить клиента</div>

    <v-row class="d-flex justify-center my-5">
        <v-card v-show="show_phys_card" class="pa-6" color="green-accent-1" v-model="phys_inf_add">
            Физическое лицо {{ phys_surname }} {{ phys_name }} {{ phys_patronymic }} телефон: {{ phys_phone }} г. {{ phys_town }} ул. {{ phys_street }} {{ phys_house }} {{ phys_frame }} кв. {{ phys_apartment }} добавлено
        </v-card>
        <v-card v-show="show_entyti_card" class="pa-6" color="green-accent-1" v-model="phys_inf_add">
            Юридическое лицо {{ entity_surname }} {{ entity_name }} {{ entity_patronymic }} телефон: {{ entity_phone }} компания {{ entity_name_of_company }} ИНН {{ entity_inn }} добавлено
        </v-card>
    </v-row>

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
                        @click="submit"
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
            inn: null,

            phys_surname: null,
            phys_name: null,
            phys_patronymic: null,
            phys_phone: null,
            phys_town: null,
            phys_street: null,
            phys_house: null,
            phys_frame: null,
            phys_apartment: null,


            entity_surname: null,
            entity_name: null,
            entity_patronymic: null,
            entity_phone: null,
            entity_name_of_company: null,
            entity_inn: null,
            
            show_phys_card : false,
            show_entyti_card : false
        }
        },
        methods:{
            submit: function(){

                this.show_phys_card = false,
                this.show_entyti_card = false


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
                        apartment : this.apartment
                    })

                    this.phys_surname = this.surname,
                    this.phys_name = this.name,
                    this.phys_patronymic = this.patronymic,
                    this.phys_phone = this.phone,
                    this.phys_town = this.town,
                    this.phys_street = this.street,
                    this.phys_house = this.house,
                    this.phys_frame = this.frame,
                    this.phys_apartment = this.apartment

                    this.show_phys_card = true
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

                    this.entity_surname = this.surname
                    this.entity_name = this.name
                    this.entity_patronymic = this.patronymic
                    this.entity_phone = this.phone
                    this.entity_name_of_company = this.name_of_company
                    this.entity_inn = this.inn

                    this.show_entyti_card = true
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