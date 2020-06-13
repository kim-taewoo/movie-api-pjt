<template>
  <v-row>
    <v-col cols="12" sm="6" offset-sm="3">
      <v-card class="px-1" light>
        <v-card-title>Trailers</v-card-title>
        <v-row dense>
          <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
            <v-card light>
              <v-img
                :src="card.src"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="200px"
              >
                <div class="text-center">
                  <v-icon color="blue lighten-5" x-large>mdi-play-circle-outline</v-icon>
                </div>
                <v-card-title v-text="card.title"></v-card-title>
              </v-img>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data: () => ({
    cards: [
      {
        title: 'Pre-fab homes',
        src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        flex: 12,
      },
      {
        title: 'Favorite road trips',
        src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
        flex: 6,
      },
      {
        title: 'Best airlines',
        src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
        flex: 6,
      },
    ],
  }),
};
</script>

<style></style>
