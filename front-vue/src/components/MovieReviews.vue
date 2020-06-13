<template>
  <v-card class="pa-4" light>
    <v-row>
      <v-col cols="12" class="pb-0">
        <h2 class="display-1 font-weight-thin">
          REVIEWs
        </h2>
      </v-col>
    </v-row>
    <hr>
    <v-row>
      <v-col cols="12" sm="6" class="pb-1">
        <MovieReviewItem />
      </v-col>
      <v-col cols="12" sm="6" class="py-1">
        <MovieReviewItem />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import MovieReviewItem from '@/components/MovieReviewItem'
export default {
  components: {
    MovieReviewItem
  }
}
</script>

<style>

</style>