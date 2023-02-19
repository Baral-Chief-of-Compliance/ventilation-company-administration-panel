<template>
    <div class="text-center">
        <v-dialog
        v-model="dialog"
        width="auto"
        >

                <template v-slot:activator="{ props }">
                    <div class="text-h3 py-6 mx-10 text-left">Добавить заявку</div>

                    <div class="py-6 mx-10 d-flex justify-center">
                        <v-col>
                            <v-row class="ma-10" v-if="stage === 0">


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

                                <v-combobox
                                    v-show="selected === 'phys'"
                                    v-model="phys_check"
                                    label="Физическое лицо"
                                    color="indigo"
                                    :items="phys_clients"

                                ></v-combobox>

                                <v-combobox
                                    v-show="selected === 'entity'"
                                    v-model="entity_check"
                                    label="Юридическое лицо"
                                    color="indigo"
                                    :items="entity_clients"
                                ></v-combobox>

                            </v-row>
                                        
                            <v-row class="ma-10" v-else-if="stage === 1">
                                <v-combobox
                                    v-model="stock_check"
                                    label="Склад"
                                    color="indigo"
                                    :items="stocks"
                                ></v-combobox>
                            </v-row>
                            <v-row class="ma-10" v-else-if="stage === 2">
                                <v-btn block
                                    color="indigo"
                                    v-bind="props"
                                    >
                                    Добавить склад
                                </v-btn>
                            </v-row>
                                <div v-else>
                                    Нихуя нет
                                </div>

                        
                            <v-row class="ma-10">
                                <v-btn @click="exit_stage" color="gray">
                                    Назад
                                </v-btn>

                                <v-spacer></v-spacer>
                                <v-btn @click="enter_stage" color="indigo">
                                    Вперед
                                </v-btn>

                            </v-row>

                            <v-row class="ma-10">
                                {{ stage }}
                                {{ phys_check }}
                                {{ entity_check }}
                                {{ stock_id }}
                            </v-row>
                        </v-col>
                    </div>

                </template>

                <v-card>
                    <v-card-title>
                        Форма для добавления материала в заказ
                    </v-card-title>
                    <v-form  class="mx-5 mb-5">
                        <v-text-field
                            v-model="stock_town"
                            label="город"
                            color="indigo"
                        >
                        </v-text-field>

                        <v-text-field
                            v-model="stock_street"
                            label="улица"
                            color="indigo"
                        >
                        </v-text-field>

                        <v-text-field
                            v-model="stock_house"
                            label="дом"
                            color="indigo"
                        >
                        </v-text-field>

                        <v-text-field
                            v-model="stock_frame"
                            label="корпус"
                            color="indigo"
                        >
                        </v-text-field>
                    </v-form>
                    <v-card-actions>
                        <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                        <v-btn color="green"  @click="add_stock">Добавить</v-btn>
                    </v-card-actions>
                </v-card>
        </v-dialog>
    </div>
</template>

<script>
import axios from 'axios'

    export default{
        data(){
            return{
                dialog: false,
                stage: 0,
                selected: null,
                phys_clients: [],
                entity_clients: [],
                stocks: [],

                phys_check : null,
                entity_check: null,
                stock_check: null,
                stock_id: null
            }
        },
        mounted(){
            this.all_phys_client_apllication()
            this.all_entity_client_apllication()
            this.all_stocks_application()
        },
        methods: {
            enter_stage(){
                if (this.stage === 1){
                    this.get_stock_id()
                }
                this.stage++
            },
            exit_stage(){
                this.stage--
            },
            all_phys_client_apllication(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/applications/all_phys_client_apllication')
                .then (response => (this.phys_clients = response.data ))
            },
            all_entity_client_apllication(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/applications/all_entity_client_apllication')
                .then (response => (this.entity_clients = response.data))
            },
            all_stocks_application(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/applications/all_stocks_apllication')
                .then(response => (this.stocks = response.data))
            },
            get_stock_id(){
                let array_stock = this.stock_check.split(' ')
                this.stock_id = array_stock[1]
            }
        }
    }
</script>