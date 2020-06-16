<template>
  <v-card outlined flat class="">
    <div class="text-right">
      <v-btn @click="onReviewDeleteClick" icon>
        <v-icon small>mdi-close</v-icon>
      </v-btn>
    </div>
    <div class="text-center mt-2">
      <v-rating
        v-model="review.rating"
        color="yellow darken-3"
        background-color="grey darken-1"
        empty-icon="$ratingFull"
        half-increments
        dense
        readonly
      ></v-rating>
      {{ review.rating }}
    </div>
    <v-card-text class="py-1 text-center body-1">
      {{review.content}}
    </v-card-text>
    <v-card-actions class="py-0">
      <v-list-item class="py-0">
        <v-list-item-content>
          <v-list-item-title>{{review.creator.username}}</v-list-item-title>
        </v-list-item-content>

        <v-row align="center" justify="end">
          <v-btn @click="onReviewLikeClick" icon color="pink" class="mr-1">
            <v-icon>{{review.is_liked ? 'mdi-heart' : 'mdi-heart-outline'}}</v-icon>
          </v-btn>
          <span class="subheading mr-2">{{review.likes_count}}</span>
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  props: ['review'],
  data: () => ({
  }),
  methods: {
    ...mapActions(['deleteReview', 'likeReview']),
    onReviewDeleteClick() {
      this.deleteReview(this.review.id)
    },
    onReviewLikeClick() {
      this.likeReview(this.review.id)
    }
  }
};
</script>

<style></style>
