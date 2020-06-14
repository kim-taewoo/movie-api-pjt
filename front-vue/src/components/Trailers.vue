<template>
  <v-card class="px-1" light>
    <v-card-title>Trailers</v-card-title>
    <v-row dense>
      <v-col v-for="movie in movies" :key="movie.title" :cols="movie.flex">
        <v-hover v-slot:default="{ hover }">
          <v-card
            class="trailerItem"
            light
            :elevation="hover ? 12 : 2"
            :class="{ 'on-hover': hover }"
            :to="{name: 'MovieTrailer', params: {title: movie.title}}"
          >
            <v-img
              :src="movie.src"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <div class="text-center">
                <v-icon color="blue lighten-5" x-large
                  >mdi-play-circle-outline</v-icon
                >
              </div>
              <v-card-title v-text="movie.title"></v-card-title>
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
    movies: [
      {
        id:1,
        title: '나홀로집에',
        src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg',
        flex: 12,
      },
      {
        id:2,
        title: 'flipped',
        src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg',
        flex: 6,
      },
      {
        id: 3,
        title: 'Best airlines',
        src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg',
        flex: 6,
      },
    ],
  }),
};
</script>

<style>
.trailerItem {
  transition: opacity 0.4s ease-in-out;
  cursor: pointer;
}

.trailerItem:not(.on-hover) {
  opacity: 0.85;
}
</style>
