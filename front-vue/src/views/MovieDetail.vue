<template>
  <div>
    <v-row v-if="currentMovie">
      <v-col cols="12">
        <HeroImage :movie="currentMovie" />
      </v-col>
      <v-col cols="12" sm="6">
        <MovieDescription :movie="currentMovie" class="mt-3 mt-sm-0" />
      </v-col>
      <v-col cols="12" sm="6">
        <MovieReviews :movieId="currentMovie.id" class="mt-3 mt-sm-0" />
        <MovieRecommend :movieId="currentMovie.id" class="mt-3" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import HeroImage from '@/components/HeroImage';
import MovieDescription from '@/components/MovieDescription';
import MovieReviews from '@/components/MovieReviews';
import MovieRecommend from '@/components/MovieRecommend';
import { mapActions } from 'vuex';
export default {
  name: 'MovieDetail',
  props: ['movie'],
  data() {
    return {
      currentMovie: null,
    };
  },
  components: {
    HeroImage,
    MovieDescription,
    MovieReviews,
    MovieRecommend,
  },
  methods: {
    ...mapActions(['fetchMovie']),
  },
  watch: {
    $route(to, from) {
      if (to !== from) {
        this.fetchMovie(this.$route.params.id).then((res) => {
          this.currentMovie = res;
        });
      }
    },
  },
  created() {
    if (typeof this.movie === 'undefined') {
      this.fetchMovie(this.$route.params.id).then((res) => {
        console.log(res);
        this.currentMovie = res;
      });
    } else {
      this.currentMovie = this.movie;
    }
  },
};
</script>

<style></style>
