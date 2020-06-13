<template>
  <div>
    <v-row>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-card color="#eeeeee" light class="pa-2">
          <h2 class="ma-2 display-1 font-weight-thin">All Movies</h2>
          <MovieFilter />
          <MovieList class="mt-2" />
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import MovieFilter from '@/components/MovieFilter'
import MovieList from '@/components/MovieList';

export default {
  components: {
    MovieFilter,
    MovieList,
  },
};
</script>

<style></style>
