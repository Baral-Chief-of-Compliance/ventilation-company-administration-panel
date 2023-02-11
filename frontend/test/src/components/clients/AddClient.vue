<template>
    <div class="text-h3 py-6 mx-10">Добавить клиента</div>

    <v-form v-model="valid">
        <v-container class="d-flex justify-center">
            <v-col>
                <v-row class="mx-10">
                    <v-text-field
                        label="Фамилия"
                        color="indigo"
                        required
                        class="mx-5"
                    ></v-text-field>

                    <v-text-field
                        label="Имя"
                        color="indigo"
                        required
                        class="mx-5"
                    ></v-text-field>

                    <v-text-field
                        label="Отчество"
                        color="indigo"
                        class="mx-5"
                    ></v-text-field>

                    <v-text-field
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
                                label="Город"
                                color="indigo"
                                required
                            ></v-text-field>

                            <v-text-field
                                v-show="selected === 'phys'"
                                label="Улица"
                                color="indigo"
                                required
                                class="mx-2"
                            ></v-text-field>
 
                            <v-text-field
                                v-show="selected === 'phys'"
                                label="Дом"
                                color="indigo"
                                class="mx-2"
                            ></v-text-field>

                            <v-text-field
                                v-show="selected === 'phys'"                            
                                label="Корпус"
                                color="indigo"
                                class="mx-2"
                            ></v-text-field>

                            <v-text-field
                                v-show="selected === 'phys'"
                                label="Квартира"
                                color="indigo"
                                class="mx-2"
                            ></v-text-field>

                </v-row>

                <v-row class="mx-13 mt-15">

                        <v-text-field
                            v-show="selected === 'entity'"
                            label="Название компании"
                            color="indigo"
                            required
                        ></v-text-field>

                        <v-text-field
                            v-show="selected === 'entity'"
                            label="ИНН"
                            color="indigo"
                            required
                            class="mx-2"
                        ></v-text-field>
                    
                </v-row>
            
                <v-row class="mx-14 mt-15">
                    <v-btn color="indigo" size="x-large" block>
                        Добавить клиента
                    </v-btn>
                </v-row>

            </v-col>
        </v-container>
    </v-form>
</template>

<script>

    export default {
        data () {
        return {
            selected: null,
        }
        }
    }
</script>