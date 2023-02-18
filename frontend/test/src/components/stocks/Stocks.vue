<template>
    <div class="text-center">
      <v-dialog
        v-model="dialog"
        width="auto"
      >
        <template v-slot:activator="{ props }">
  
          <div class="text-h3 py-6 mx-10 text-left">Склады</div>
  
          <v-container class="d-flex justify-center">
            <v-col>
                <v-row class="mx-10">
                  <v-col 
                    v-for="el in Stocks"
                    :key="el.id"
                    cols="12"
                    md="3"
                    v-bind="props_hover"  
                  >
                  <v-hover v-slot="{ isHovering, props }">
                    <v-card v-bind="props" height="200" width="300" 
                      class="mx-auto" 
                      :color="isHovering ? 'indigo' : undefined"
                      :to="{ name: 'stock_inf', params: {id: el.id}}"
                    >
                    <v-card-item class="text-h6">
                      {{ el.town }} {{ el.street }} {{ el.house }} {{ el.frame }}
                    </v-card-item>
     
                    </v-card>
                    <v-card-actions class="mt-3">
                      <v-spacer></v-spacer>
                      <v-btn @click="delete_stock(el.id)" variant="outlined" color="red"
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
                    Добавить склад
                  </v-btn>
                </v-row>
            </v-col>
  
  
          </v-container>
  
        </template>
  
        <v-card>
          <v-card-title>
            Форма для добавления склада
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
  
  
    export default {
      data () {
        return {
          dialog: false,
          Stocks: null,
          stock_town: null,
          stock_street: null,
          stock_house: null,
          stock_frame: null
        }
      },
      updated(){
        this.get_data()
      },
      methods: {
        add_stock(){
          axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/stocks/add_stock',{
            town: this.stock_town,
            street: this.stock_street,
            house: this.stock_house,
            frame: this.stock_frame
          }).then((Stocks)=>this.get_data())
  
          this.stock_town = null,
          this.stock_street = null,
          this.stock_house = null,
          this.stock_frame = null,
          this.dialog = false
  
          },
        get_data(){
          axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/stocks')
          .then(response => (this.Stocks = response.data))
        },
        delete_stock(id){
          axios.delete(`http://127.0.0.1:5000/admin_panel/api/v1.0/stocks/${id}`).then(
                  (Stocks)=>this.get_data()
          )
        }
      }
    }
  </script>