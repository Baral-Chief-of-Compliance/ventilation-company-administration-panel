<template>
    <v-list-group value="Brigades">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-account-multiple"
        title="Бригады"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in brigades"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>
  </v-list-group>

  <v-list-group value="Clients">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-account-details"
        title="Клиенты"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in clients"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>

    
  </v-list-group>

  <v-list-group value="Stocks">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-garage"
        title="Склады"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon], i) in stocks"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
    ></v-list-item>

    
  </v-list-group>

  <v-list-group value="Orders">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-application"
        title="Заказы"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon], i) in orders"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
    ></v-list-item>

    
  </v-list-group>
</template>

<script>
  export default {
    data: () => ({
      brigades: [
        ['Добавить', 'mdi-account-multiple-plus', '/add_brigades'],
        ['Список', 'mdi-account-multiple', '/brigades']
      ],
      clients:[
        ['Добавить', 'mdi-account-plus', '/add_client'],
        ['Найти', 'mdi-account-search'],
        ['Список', 'mdi-account-multiple']
      ],
      stocks:[
        ['Добавить', 'mdi-home-plus-outline'],
        ['Найти', 'mdi-account-search'],
        ['Список', 'mdi-account-multiple']
      ],
      orders: [
        ['Добавить', 'mdi-plus-outline'],
        ['Найти', 'mdi-file-outline'],
        ['Список', 'mdi-update']
      ],
    }),
  }
</script>