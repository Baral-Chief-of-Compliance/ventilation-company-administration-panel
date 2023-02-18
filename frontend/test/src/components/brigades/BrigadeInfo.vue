<template>
      <div class="text-center">
            <v-dialog
            v-model="dialog"
            width="auto"
            >
        <template v-slot:activator="{ props }">

        <div class="text-h3 py-6 mx-10 text-left"> Бригада {{ brigade_name }} </div>

        <v-container class="d-flex justify-center">
            <v-col>
                <v-row v-for="emp in employees" :key="emp.id" class="mx-10">
                    <v-card class="my-2 pa-6 mx-14 d-flex flex-row" >
                        <div>
                            <b>{{ emp.position }}</b> {{ emp.surname }} {{ emp.name }} {{ emp.patronymic }} {{ emp.phone }}   
                        </div>
                    </v-card>
                    <v-card-actions class="mt-3">
                    <v-spacer></v-spacer>
                    <v-btn variant="outlined" color="red"  @click="delete_employee(emp.id)"
                    >Удалить</v-btn>
                  </v-card-actions>
                </v-row>
                <v-row class="mx-14 mt-15">
                    <v-btn block
                    color="indigo"
                    v-bind="props"
                    >
                    Добавить сотрудника
                    </v-btn>
                </v-row>
            </v-col>
        </v-container>
      </template>

      <v-card>
        <v-card-title>
          Форма для добавления сотрудника
        </v-card-title>
        <v-form  class="mx-5 mb-5">
          <v-text-field
            v-model="surname"
            label="Фамилия"
            color="indigo"
          >
          </v-text-field>
          <v-text-field
            v-model="name"
            label="Имя"
            color="indigo"
          >
          </v-text-field>
          <v-text-field
            v-model="patronymic"
            label="Отчество"
            color="indigo"
          >
          </v-text-field>
          <v-text-field
            v-model="position"
            label="Должность"
            color="indigo"
          >
          </v-text-field>
          <v-text-field
            v-model="phone"
            label="Телефон"
            color="indigo"
          >
          </v-text-field>
        </v-form>
        <v-card-actions>
          <v-btn color="red" @click="dialog = false">Закрыть</v-btn>
          <v-btn color="green" @click="add_employee">Добавить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>

</template>



<script>
import axios from 'axios';


export default{
    data(){
        return{
            brigade_name: null,
            employees: null,
            dialog: false,
            surname: null,
            name: null,
            patronymic: null,
            position: null,
            phone: null
        }
    },
    updated(){
        this.get_data()
    },
    methods: {
        add_employee(){
            axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/add_employee', {
                surname : this.surname,
                name : this.name,
                patronymic : this.patronymic,
                position : this.position,
                phone : this.phone,
                br_id : this.$route.params.id
            })

            this.surname = null,
            this.name = null,
            this.patronymic = null,
            this.position = null,
            this.phone = null
            this.dialog = false
        },
        get_data(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/brigades/${this.$route.params.id}`)
            .then(response => (
                this.brigade_name = response.data.name,
                this.employees = response.data.employees
            ))
        },
        delete_employee(id){
            axios.delete(`http://127.0.0.1:5000/admin_panel/api/v1.0/employees/${id}`).then(
                (employees)=>this.get_data()
            )    
        }
   }
}
</script>