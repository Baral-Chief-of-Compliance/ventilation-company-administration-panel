

                <template>
                    <div class="text-h3 py-6 mx-10 text-left">Добавить заявку</div>

                    <v-row class="d-flex justify-center my-5">
                        <v-card v-show="add_inf" class="pa-6" color="green-accent-1">
                            Заказа Добавлен 
                        </v-card>
                    </v-row>

                    <div class="py-6 mx-10 d-flex justify-center">
                        <v-col>
                            <v-row class="ma-10" v-if="stage === 0">

                                    <v-radio-group v-model="selected" inline>
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

                            </v-row>
            

                            <v-row class="ma-10" v-if="stage === 0">
                                <v-card
                                    v-show="selected === 'phys'"
                                    v-model="phys_check"
                                    class="my-2 pa-6 mx-14 overflow-y-auto"
                                    max-height="600"

                                >
                                    <v-card-text>
                                        <v-radio-group v-model="ph_id">
                                                <v-radio color="indigo"  v-for="ph in phys_clients"
                                                    :value="ph.id"
                                                    :label="`${ph.surname} ${ph.name} ${ph.patronymic} ${ph.phone}`"
                                                    >
                                                </v-radio>
 
                                        </v-radio-group>

                                    </v-card-text>
                                
                            
                                </v-card>

                                <v-card
                                    v-show="selected === 'entity'"
                                    v-model="entity_check"
                                    class="my-2 pa-6 mx-14 overflow-y-auto"
                                    max-height="600"

                                >
                                    <v-card-text>
                                        <v-radio-group v-model="en_id">
                                            <v-radio color="indigo" v-for="en in entity_clients"
                                                :value="en.id"
                                                :label="`${en.surname} ${en.name} ${en.patronymic} ${en.name_of_company} ${en.phone}`"
                                            >
                                            </v-radio>
                                        </v-radio-group>

                                    </v-card-text>
                            
                                </v-card>

                            </v-row>
                                        
                            <v-row class="ma-10" v-else-if="stage === 1">
                                <v-card   class="my-2 pa-6 mx-14">
                                    <v-radio-group v-model="stock_id">
                                        <v-radio v-for="st in stocks"
                                            :label="`Склад по адресу г. ${st.town} ул. ${st.street} д. ${st.house} к. ${st.frame}`" 
                                            :value="st.id" 
                                            color="indigo"
                                        >
                                        </v-radio>
                                    </v-radio-group>
                                </v-card>

                            </v-row>

                            <v-row class="ma-10" v-else-if="stage === 2">
                                <v-col>
                                    <v-card v-for="mat in stocks_info" class="my-2 pa-6 mx-14 d-flex flex-row" >
                                        <b>{{ mat.name }}</b> <v-spacer></v-spacer> Количество: <b>{{ mat.quantity }}</b>/ <v-text-field v-model="data[mat.id]" type="number" hide-details density="compact" :min="0" :max="mat.quantity"></v-text-field> <v-btn color="green" variant="outlined" @click="addItem(mat.id, data[mat.id])">Добавить</v-btn><v-btn color="red" variant="outlined" @click="removeItem(mat.id)">Удалить</v-btn>
                                    </v-card>
                                </v-col>
                            </v-row>

                            
                            <v-row class="ma-10" v-else-if="stage === 3">
                                <v-radio-group v-model="selected_brigade">

                                    <v-radio v-for="br in brigades_info"
                                        :label="br.name" 
                                        :value="br.id" 
                                        color="indigo"
                                    >
                                    </v-radio>

                                </v-radio-group>
                            </v-row>

                            <v-row class="ma-10" v-else-if="stage === 4">
                                <v-text-field v-model="date_create" type="date" label="Дата оформления заявки" color="indigo"></v-text-field>
                                <v-text-field v-model="date_start_work" type="date" label="Дата начала работы" color="indigo"></v-text-field>
                                <v-text-field v-model="date_end_work" type="date" label="Дата конца работы" color="indigo"></v-text-field>
                                
                            </v-row>


                            <v-row class="ma-10" v-else-if="stage === 5">
                                <v-text-field v-model="town" color="indigo" label="Город"></v-text-field>
                                <v-text-field v-model="street" color="indigo" label="Улица"></v-text-field>
                                <v-text-field v-model="house" color="indigo" label="Дом"></v-text-field>
                                <v-text-field v-model="frame" color="indigo" label="Корпус"></v-text-field>
                            </v-row>
                                <div v-else>
                                    Нихуя нет
                                </div>

                        
                            <v-row class="ma-10">
                                <v-btn @click="exit_stage" color="gray" v-if="stage != 0 ">
                                    Назад
                                </v-btn>

                                <v-spacer></v-spacer>
                                <v-btn @click="enter_stage" color="indigo" v-if="stage !=5">
                                    Вперед
                                </v-btn>

                            </v-row>

                            <v-row class="ma-10" v-if="stage === 5">
                                <v-btn block color="indigo" @click="send_data_about_application(), sendData()">Добавить заявку</v-btn>
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
                stage: 0,
                selected: null,
                phys_clients: [],
                entity_clients: [],
                stocks: [],
                data: [],
                date_create: '',
                date_start_work: '',
                date_end_work: '',
                town: '',
                street: '',
                house: '',
                frame: '',
                ph_id: 0,
                en_id: 0,
                add_inf: false,

                stocks_info: [],
                selected_brigade: 0,

                phys_check : '',
                entity_check: '',
                stock_check: '',
                stock_id: ''

            }
        },
        computed: {
            ...mapState(useCartStore, ['cart']),
        },
        mounted(){
            this.all_phys_client_apllication()
            this.all_entity_client_apllication()
            this.all_stocks_application()
            this.get_brigades()
        },
        methods: {
            ...mapActions(useCartStore, ['addItem']),

            ...mapActions(useCartStore, ['removeItem']),

            ...mapActions(useCartStore, ['sendData']),

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
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/clients/phys_clients')
                .then (response => (this.phys_clients = response.data ))
            },
            all_entity_client_apllication(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/clients/entity_clients')
                .then (response => (this.entity_clients = response.data))
            },
            all_stocks_application(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/stocks')
                .then(response => (this.stocks = response.data))
            },
            get_stock_id(){
                this.get_materials_from_stock(this.stock_id)
            },
            get_materials_from_stock(id){
                axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/stocks/${id}`)
                .then(response => (this.stocks_info = response.data.materials))
            },
            get_brigades(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/brigades')
                .then(response => (this.brigades_info = response.data))
            },

            send_data_about_application(){
                let cl_id_for_send = 0
                if (this.selected === 'phys'){
                    cl_id_for_send = this.phys_check
                }
                else if (this.selected === 'entity'){
                    cl_id_for_send = this.entity_check
                }
                axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/applications/add_application', {
                    cl_id: cl_id_for_send,
                    op_id: 1,
                    br_id: this.selected_brigade,
                    town: this.town,
                    street: this.street,
                    house: this.house,
                    frame: this.frame,
                    apartment: 20,
                    date_create: this.date_create,
                    date_of_start_work: this.date_start_work,
                    date_of_end_work: this.date_end_work
                })

                this.add_inf = true,
                this.stage = 0,
                this.selected = null,
                this.data = [],
                this.date_create = '',
                this.date_start_work = '',
                this.date_end_work = '',
                this.town = '',
                this.street = '',
                this.house = '',
                this.frame = '',
                this.ph_id = 0,
                this.en_id = 0,
                this.selected_brigade = 0,
                this.phys_check = '',
                this.entity_check = '',
                this.stock_check = '',
                this.stock_id = ''
            }
        }
    }
</script>