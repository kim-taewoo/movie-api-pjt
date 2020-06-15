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
      {{review.content}}
    </v-card-text>
    <v-card-actions class="py-0">
      <v-list-item class="py-0">
        <v-list-item-content>
          <v-list-item-title>{{review.creator.username}}</v-list-item-title>
        </v-list-item-content>

        <v-row align="center" justify="end">
          <v-btn icon color="pink" class="mr-1">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <span class="subheading mr-2">{{review.likes_count}}</span>
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['review'],
  data: () => ({
  }),
  computed: {
    rating() {
      return this.review.rating
    }
  }
};
</script>

<style></style>
