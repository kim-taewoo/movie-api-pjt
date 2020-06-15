<template>
  <v-card class="px-1" light>
    <v-card-title>Trailers</v-card-title>
    <v-row dense>
      <v-col v-for="(movie, idx) in selectedMovies" :key="movie.title" :cols="idx===0?12:6">
        <v-hover v-slot:default="{ hover }">
          <v-card
            class="trailerItem"
            light
            :elevation="hover ? 12 : 2"
            :class="{ 'on-hover': hover }"
            :to="{name: 'MovieTrailer', params: {title: movie.title}}"
          >
            <v-img
              :src="movie.horizontal_poster"
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
import {mapState} from 'vuex'
import _ from 'lodash'
export default {
  computed: {
    ...mapState(['movies']),
    selectedMovies() {
      return _.sampleSize(this.movies, 3)
    }
  }
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
