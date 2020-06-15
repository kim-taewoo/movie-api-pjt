<template>
  <v-card class="pa-4" light>
    <v-row>
      <v-col cols="12" class="pb-0">
        <h2 class="display-1 font-weight-thin">
          REVIEWs
        </h2>
      </v-col>
    </v-row>
    <hr />
    <v-row>
      <v-col v-for="review in reviews" :key="review.id" cols="12" sm="6" class="py-1">
        <MovieReviewItem :review="review" />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-card outlined>
          <v-card-text class="pb-1">
            <div>
              <v-text-field
                label="나의 감상평"
                single-line
                outlined
                v-model="reviewData.content"
              ></v-text-field>
            </div>
            <div class="text-center">
              <v-rating
                v-model="reviewData.rating"
                color="yellow darken-3"
                background-color="grey darken-1"
                empty-icon="$ratingFull"
                half-increments
                hover
              ></v-rating>
              나의 평점: {{ reviewData.rating }}
            </div>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn @click.stop="onReviewSubmit" block color="pink" dark>리뷰 남기기</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import MovieReviewItem from '@/components/MovieReviewItem';
import {mapActions, mapState} from 'vuex'
export default {
  props: ['movieId'],
  components: {
    MovieReviewItem,
  },
  data() {
    return {
      reviewData: {
        rating: 5,
        content: ''
      }
    };
  },
  methods: {
    ...mapActions(['fetchReviews', 'createReview']),
    onReviewSubmit() {
      console.log({...this.reviewData})
      this.createReview({movieId: this.movieId, ...this.reviewData})
      this.reviewData = {
        rating: 5.0,
        content: ''
      }
    }
  },
  computed: {
    ...mapState(['reviews'])
  },
  created() {
    this.fetchReviews(this.movieId)
  }
};
</script>

<style></style>
