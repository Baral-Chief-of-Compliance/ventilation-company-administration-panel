<template>
  <v-app>
    <v-layout>
      <v-navigation-drawer
        expand-on-hover
        rail
        color="indigo"
        
      >
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
            title="Sandra Adams"
            subtitle="sandra_a88@gmailcom"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

    <v-list>
      <nav-options />
    </v-list>
      </v-navigation-drawer>

      <v-main><default-view /></v-main>
    </v-layout>

    
  </v-app>
</template>

<script setup>
  import DefaultBar from './AppBar.vue'
  import DefaultView from './View.vue'
  import NavOptions from './NavOptions.vue';
</script>
