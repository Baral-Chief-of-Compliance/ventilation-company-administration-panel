<template>
    <div class="text-center">
          <v-dialog
          v-model="dialog"
          width="auto"
          >
      <template v-slot:activator="{ props }">

      <div class="text-h3 py-6 mx-10 text-left"> Склад по адресу: г. {{ town }} ул. {{ street }} д. {{ house }} {{ frame }}</div>

      <v-container class="d-flex justify-center">
          <v-col>
              <v-row v-for="mat in materials" :key="mat.id" class="mx-10">
                  <v-card class="my-2 pa-6 mx-14 d-flex flex-row" >
                      <div>
                          <b>{{ mat.name }}</b> Количество <b>{{ mat.quantity }}</b> шт.
                      </div>
                  </v-card>
                  <v-card-actions class="mt-3">
                  <v-spacer></v-spacer>
                  <v-btn variant="outlined" color="red"  @click="delete_material(mat.id)"
                  >Удалить</v-btn>
                </v-card-actions>
              </v-row>
              <v-row class="mx-14 mt-15">
                  <v-btn block
                  color="indigo"
                  v-bind="props"
                  >
                  Добавить материал
                  </v-btn>
              </v-row>
          </v-col>
      </v-container>

      <div class="py-6 mx-10 d-flex justify-center">
        <MapForOne :latitude="latitude" :longitude="longitude" />
      </div>
    </template>

    <v-card>
      <v-card-title>
        Форма для добавления материала
      </v-card-title>
      <v-form  class="mx-5 mb-5">
        <v-text-field
          v-model="name_of_material"
          label="Название"
          color="indigo"
        >
        </v-text-field>
        <v-text-field
          v-model="quantity"
          label="Количество"
          color="indigo"
        >
        </v-text-field>
      </v-form>
      <v-card-actions>
        <v-btn color="red" @click="dialog = false">Закрыть</v-btn>
        <v-btn color="green" @click="add_material">Добавить</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</div>



</template>



<script>
import axios from 'axios';
import MapForOne from '@/components/Map/MapForOne.vue'


export default{
  data(){
      return{
        town: null,
        street: null,
        house: null,
        frame: null,
        latitude: null,
        longitude: null,
        materials: null,
        name_of_material: null,
        quantity: null,
        dialog: false
      }
  },
  components: {
    MapForOne
  },
  updated(){
      this.get_data()
  },
  methods: {
        add_material(){
          axios.post('http://127.0.0.1:5000/admin_panel/api/v1.0/materials/add_material', {
            name_of_material : this.name_of_material,
            quantity: this.quantity,
            stock_id : this.$route.params.id
          })

          this.name_of_material = null,
          this.quantity = null,
          this.dialog = false
      },
      get_data(){
          axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/stocks/${this.$route.params.id}`)
          .then(response => (
              this.town = response.data.address.town,
              this.street = response.data.address.street,
              this.house = response.data.address.house,
              this.frame = response.data.address.frame,
              this.latitude = response.data.address.latitude,
              this.longitude = response.data.address.longitude,
              this.materials = response.data.materials
          ))
      },
      delete_material(id){
          axios.delete(`http://127.0.0.1:5000/admin_panel/api/v1.0/materials/${id}`).then(
              (materials)=>this.get_data()
          )    
      }
 }
}
</script>