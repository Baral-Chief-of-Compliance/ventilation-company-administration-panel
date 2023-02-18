<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="auto"
    >
      <template v-slot:activator="{ props }">

        <div class="text-h3 py-6 mx-10 text-left">Бригады</div>

        <v-container class="d-flex justify-center">
          <v-col>
              <v-row class="mx-10">
                <v-col 
                  v-for="el in allBrigades"
                  :key="el.id"
                  cols="12"
                  md="3"
                  v-bind="props_hover"  
                >
                <v-hover v-slot="{ isHovering, props }">
                  <v-card v-bind="props" height="200" width="300" 
                    class="mx-auto" 
                    :color="isHovering ? 'indigo' : undefined"
                    :to="{ name: 'brigade_inf', params: {id: el.id}}"
                  >
                  <v-card-item class="text-h6">
                    {{ el.name }}
                  </v-card-item>
   
                  </v-card>
                  <v-card-actions class="mt-3">
                    <v-spacer></v-spacer>
                    <v-btn @click="delete_brigade(el.id)" variant="outlined" color="red"
                    >Удалить</v-btn>
                  </v-card-actions>

                </v-hover>
                </v-col>
              </v-row>
              <v-row class="mx-14 mt-15">
                <v-btn block
                  color="indigo"
                  v-bind="props"
                  >
                  Добавить бригаду
                </v-btn>
              </v-row>
          </v-col>


        </v-container>

      </template>

      <v-card>
        <v-card-title>
          Форма для добавления бригады
        </v-card-title>
        <v-form>
          <v-text-field
            v-model="brigades_name"
            label="название бригады"
            color="indigo"
            class="mx-5 mb-5"
          >

          </v-text-field>
        </v-form>
        <v-card-actions>
          <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
          <v-btn color="green"  @click="create_brigade">Добавить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios'


  export default {
    data () {
      return {
        dialog: false,
        allBrigades: null,
        brigades_name: null
      }
    },
    methods: {
      create_brigade(){
        axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/create_brigades',{
          name: this.brigades_name
        })

        this.brigades_name = null
        this.dialog = false

        },
      get_data(){
        axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/brigades')
        .then(response => (this.allBrigades = response.data))
      },
      delete_brigade(id){
        axios.delete(`http://127.0.0.1:5000/admin_panel/api/v1.0/brigades/${id}`).then(
                (employees)=>this.get_data()
        )
      }
    },
    updated(){
      this.get_data()
    }
  }
</script>