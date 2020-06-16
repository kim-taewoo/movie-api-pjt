<template>
  <div>
    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <v-card light class="pa-2">
          <h2 class="ma-2 display-1 font-weight-light">All Movies</h2>
          <MovieFilter @onTypeSelect="onTypeSelect" />
          <MovieList :movies="movies" class="mt-2" />
        </v-card>

        <v-row class="mt-8" justify="center">
          <v-col cols="12" class="d-flex justify-center">
            <div ref="loading" class="loader">
              <div class="circle white"></div>
              <div class="circle white"></div>
              <div class="circle white"></div>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import MovieFilter from '@/components/MovieFilter';
import MovieList from '@/components/MovieList';
import { mapState, mapActions } from 'vuex';
export default {
  components: {
    MovieFilter,
    MovieList,
  },
  computed: {
    ...mapState(['movies']),
  },
  methods: {
    ...mapActions(['fetchMovies', 'fetchMoreMovies']),
    onTypeSelect(type) {
      this.type = type
      this.fetchMovies({
        params: {
          page: 1,
          order_by: type,
        },
      });
      this.page = 1;
    },
    scrollFunction() {
      const {
        scrollTop,
        scrollHeight,
        clientHeight,
      } = document.documentElement;

      if (scrollTop + clientHeight >= scrollHeight - 10) {
        this.showLoading();
      }
    },
    showLoading: async function () {
      if (this.isLoading) {
        return;
      }
      this.page++;
      this.isLoading = true;
      this.$refs.loading.classList.add('show');
      try {
        await this.fetchMoreMovies({
          params: {
            page: this.page,
            order_by: this.type,
          },
        }); // <-- key part!!!
        this.isLoading = false; // only then do we enable further loading
        this.$refs.loading.classList.remove('show'); // and remove the loader
      } catch(err) {
        console.error(err);
        this.isLoading = false; // only then do we enable further loading
        this.$refs.loading.classList.remove('show'); // and remove the loader
      }
    }
  },
  data() {
    return {
      page: 1,
      type: '-rating',
      isLoading: false,
    };
  },
  mounted() {    
    window.addEventListener('scroll', this.scrollFunction);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.scrollFunction)
  }
};
</script>

<style>
.loader {
  opacity: 0;
  display: flex;
  bottom: 50px;
  transition: opacity 0.3s ease-in;
}

.loader.show {
  opacity: 1;
}

.circle {
  background-color: #fff;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin: 5px;
  animation: bounce 0.5s ease-in infinite;
}

.circle:nth-of-type(2) {
  animation-delay: 0.1s;
}

.circle:nth-of-type(3) {
  animation-delay: 0.2s;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }
}
</style>
