<template>
  <div>
    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <HeroImage />
        <MovieDescription class="mt-4" />
        <MovieReviews class="mt-4" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import HeroImage from '@/components/HeroImage'
import MovieDescription from '@/components/MovieDescription'
import MovieReviews from '@/components/MovieReviews'
export default {
  components: {
    HeroImage,
    MovieDescription,
    MovieReviews
  }
};
</script>

<style></style>
