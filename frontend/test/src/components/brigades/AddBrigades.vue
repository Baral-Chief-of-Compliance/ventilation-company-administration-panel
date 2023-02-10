<template>
    <div class="text-h3 py-6">Добавить бригаду</div>


    
    
    <v-form v-model="valid">
    <v-container class="d-flex justify-center">
        <v-col>

        <v-row>
                <div></div>
                <v-text-field
                v-model="brigades"
                label="Название бригады"
                color="indigo"
                required
            ></v-text-field>
        </v-row>

        <v-row>


          <v-text-field
            v-model="firstname"
            label="First name"
            required
          ></v-text-field>

        

    
          <v-text-field
            v-model="lastname"
            :rules="nameRules"
            :counter="10"
            label="Last name"
            required
          ></v-text-field>

          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
    </v-row>
</v-col>
    </v-container>
  </v-form>

</template>

<script>

</script>