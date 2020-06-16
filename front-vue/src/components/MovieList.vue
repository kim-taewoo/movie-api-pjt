<template>
  <v-row>
    <v-col class="py-1" v-for="(movie, i) in movies" :key="i" cols="12">
      <MovieListItem class="movieItem" :movie="movie" />
    </v-col>
  </v-row>
</template>

<script>
import MovieListItem from './MovieListItem'
export default {
  name: 'MovieList',
  props: ['movies'],
  components: {
    MovieListItem
  }
};
</script>

<style></style>
