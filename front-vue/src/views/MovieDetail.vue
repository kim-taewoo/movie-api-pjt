<template>
  <div>
    <v-row>
      <v-col cols="12">
        <HeroImage />
      </v-col>
      <v-col cols="12" sm="6">
        <MovieDescription class="mt-3 mt-sm-0" />
      </v-col>
      <v-col cols="12" sm="6">
        <MovieReviews class="mt-3 mt-sm-0" />
        <MovieRecommend class="mt-3" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import HeroImage from '@/components/HeroImage'
import MovieDescription from '@/components/MovieDescription'
import MovieReviews from '@/components/MovieReviews'
import MovieRecommend from '@/components/MovieRecommend'
export default {
  components: {
    HeroImage,
    MovieDescription,
    MovieReviews,
    MovieRecommend
  }
};
</script>

<style></style>
