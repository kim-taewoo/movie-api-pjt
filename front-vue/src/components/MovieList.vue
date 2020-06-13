<template>
  <v-row>
    <v-col class="py-1" v-for="(item, i) in items" :key="i" cols="12">
      <v-card style="overflow:hidden" light>
        <div class="d-flex flex-no-wrap justify-start">
          <v-avatar size="130" tile>
            <v-img :src="item.src"></v-img>
          </v-avatar>
          <div>
            <v-card-title class="headline" v-text="item.title"></v-card-title>

            <v-card-subtitle v-text="item.artist"></v-card-subtitle>
          </div>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'MovieList',
  data: () => ({
    items: [
      {
        color: '#1F7087',
        src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
        title: 'Supermodel',
        artist: 'Foster the People',
      },
      {
        color: '#952175',
        src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
        title: 'Halcyon Days',
        artist: 'Ellie Goulding',
      },
    ],
  }),
};
</script>

<style></style>
