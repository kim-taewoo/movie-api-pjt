<template>
  <v-card class="pa-4" light>
    <v-card-title class="pa-0">Ai 추천</v-card-title>
    <v-row dense>
      <v-col v-for="(card, idx) in cards" :key="idx" cols="3">
        <v-hover v-slot:default="{ hover }">
        <v-card class="recommendItem" :elevation="hover ? 12 : 2"
            :class="{ 'on-hover': hover }" light>
          <v-img
            :src="card.src"
            class="white--text align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="200px"
          >
            <v-card-title v-text="card.title"></v-card-title>
          </v-img>
        </v-card>
        </v-hover>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
data: () => ({
    cards: [
      {
        title: 'Pre-fab homes',
        src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
      },
      {
        title: 'Favorite road trips',
        src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
      },
      {
        title: 'Best airlines',
        src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
      },
      {
        title: 'Favorite road trips',
        src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
      },
    ],
  }),
}
</script>

<style>
.v-application a {
  text-decoration: none !important;
  color: white;
}

.recommendItem {
  transition: opacity 0.4s ease-in-out;
  cursor: pointer;
}

.recommendItem:not(.on-hover) {
  opacity: 0.85;
}
</style>