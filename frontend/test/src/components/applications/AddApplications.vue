

                <template>
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
                                <v-col>
                                    <v-card v-for="mat in stocks_info" class="my-2 pa-6 mx-14 d-flex flex-row" >
                                        <b>{{ mat.name }}</b> <v-spacer></v-spacer> Количество: <b>{{ mat.quantity }}</b>/ <v-text-field v-model="data[mat.id]" type="number" hide-details density="compact" :min="0" :max="mat.quantity"></v-text-field> <v-btn color="green" variant="outlined" @click="addItem(mat.id, data[mat.id])">Добавить</v-btn><v-btn color="red" variant="outlined" @click="removeItem(mat.id)">Удалить</v-btn>
                                    </v-card>
                                </v-col>
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
                                {{ stocks_info }}
                                {{ stocks_info.materials }}
                                {{ list_name }}
                                {{ cart }}
                            </v-row>
                        </v-col>
                    </div>

                </template>


<script>
import axios from 'axios'
import { useCartStore } from '@/stores/card'
import { mapState, mapActions } from 'pinia'


    export default{
        data(){
            return{
                dialog: false,
                stage: 0,
                selected: null,
                phys_clients: [],
                entity_clients: [],
                stocks: [],
                data: [],

                stocks_info: [],

                phys_check : null,
                entity_check: null,
                stock_check: null,
                stock_id: null
            }
        },
        computed: {
            ...mapState(useCartStore, ['cart']),
        },
        mounted(){
            this.all_phys_client_apllication()
            this.all_entity_client_apllication()
            this.all_stocks_application()
        },
        methods: {
            ...mapActions(useCartStore, ['addItem']),
            ...mapActions(useCartStore, ['removeItem']),
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
                this.get_materials_from_stock(this.stock_id)
            },
            get_materials_from_stock(id){
                axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/stocks/${id}`)
                .then(response => (this.stocks_info = response.data.materials))

                for (const el in this.stocks_info){
                        console.log(el)
            }
            }
        }
    }
</script>