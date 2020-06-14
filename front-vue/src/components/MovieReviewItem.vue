<template>
  <v-card outlined flat class="">
    <div class="text-center mt-2">
      <v-rating
        v-model="rating"
        color="yellow darken-3"
        background-color="grey darken-1"
        empty-icon="$ratingFull"
        half-increments
        dense
        readonly
      ></v-rating>
      {{ rating }}
    </div>
    <v-card-text class="py-1">
      If you enjoy using Vuetify, please take a few seconds to rate your
      experience with the framework. It really helps!
    </v-card-text>
    <v-card-actions class="py-0">
      <v-list-item class="py-0">
        <v-list-item-content>
          <v-list-item-title>Evan You</v-list-item-title>
        </v-list-item-content>

        <v-row align="center" justify="end">
          <v-btn icon color="pink" class="mr-1">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <span class="subheading mr-2">256</span>
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    rating: 4.5,
  }),
};
</script>

<style></style>
