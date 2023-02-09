<template>
  <v-app-bar color="indigo">
    <v-btn>Бригада</v-btn>
    <v-btn>Склады</v-btn>
    <v-btn>Клиенты</v-btn>
    <v-btn>Заказы</v-btn>
  </v-app-bar>
</template>

<script>
  export default {
    data () {
      return {
        tab: null,
        items: [
          'Бригада', 'Склады', 'Клиенты', 'Заказы',
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>

