<template>
  
    <!-- <v-card
        class="mx-auto"
        width="300"
      >
        <v-list>


            <v-list-group value="Brigades">
              <template v-slot:activator="{ props }">
                <v-list-item
                  v-bind="props"
                  prepend-icon="mdi-account-circle"
                  title="Бригады"
                ></v-list-item>
              </template>

              <v-list-item
                v-for="([title, icon], i) in brigades"
                :key="i"
                :title="title"
                :prepend-icon="icon"
                :value="title"
              ></v-list-item>
            </v-list-group>

            <v-list-group value="Clients">
              <template v-slot:activator="{ props }">
                <v-list-item
                  v-bind="props"
                  prepend-icon="mdi-account-circle"
                  title="Клиенты"
                ></v-list-item>
              </template>

              <v-list-item
                v-for="([title, icon], i) in clients"
                :key="i"
                :title="title"
                :prepend-icon="icon"
                :value="title"
              ></v-list-item>

              
            </v-list-group>

            <v-list-group value="Stocks">
              <template v-slot:activator="{ props }">
                <v-list-item
                  v-bind="props"
                  prepend-icon="mdi-account-circle"
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
                  prepend-icon="mdi-account-circle"
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

        </v-list>
    </v-card> -->
    <v-card>
    <v-layout>
      <v-navigation-drawer
        expand-on-hover
        rail
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


<v-list-group value="Brigades">
  <template v-slot:activator="{ props }">
    <v-list-item
      v-bind="props"
      prepend-icon="mdi-account-circle"
      title="Бригады"
    ></v-list-item>
  </template>

  <v-list-item
    v-for="([title, icon], i) in brigades"
    :key="i"
    :title="title"
    :prepend-icon="icon"
    :value="title"
  ></v-list-item>
</v-list-group>

<v-list-group value="Clients">
  <template v-slot:activator="{ props }">
    <v-list-item
      v-bind="props"
      prepend-icon="mdi-account-circle"
      title="Клиенты"
    ></v-list-item>
  </template>

  <v-list-item
    v-for="([title, icon], i) in clients"
    :key="i"
    :title="title"
    :prepend-icon="icon"
    :value="title"
  ></v-list-item>

  
</v-list-group>

<v-list-group value="Stocks">
  <template v-slot:activator="{ props }">
    <v-list-item
      v-bind="props"
      prepend-icon="mdi-account-circle"
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
      prepend-icon="mdi-account-circle"
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

</v-list>
      </v-navigation-drawer>

      <v-main style="height: 250px"></v-main>
    </v-layout>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      brigades: [
        ['Добавить', 'mdi-account-multiple-plus'],
        ['Удалить', 'mdi-account-multiple-remove'],
        ['Список', 'mdi-account-multiple'],
      ],
      clients:[
        ['Добавить', 'mdi-account-plus'],
        ['Найти', 'mdi-account-search'],
        ['Список', 'mdi-account-multiple']
      ],
      stocks:[
        ['Добавить', 'mdi-account-plus'],
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

