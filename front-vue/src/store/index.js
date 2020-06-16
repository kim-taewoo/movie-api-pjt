import Vue from 'vue';
import Vuex from 'vuex';

import cookies from 'vue-cookies';
import router from '@/router';
import axios from 'axios';

import SERVER from '@/api/drf';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    movies: [],
    recommends: [],
    reviews: [],
  },
  getters: {
    isLoggedIn: (state) => !!state.authToken,
    config: (state) => ({
      headers: {
        Authorization: `JWT ${state.authToken}`,
        'content-Type': 'Application/json',
      },
    }),
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token;
      cookies.set('auth-token', token);
    },
    SET_MOVIES(state, movies) {
      state.movies = movies;
    },
    SET_REVIEWS(state, reviews) {
      state.reviews = reviews;
    },
    SET_RECOMMENDS(state, recommends) {
      state.recommends = recommends;
    },
    ADD_REVIEW(state, review) {
      state.reviews = [...state.reviews, review];
    },
    DELETE_REVIEW(state, reviewId) {
      state.reviews = state.reviews.filter((review) => review.id !== reviewId)
    },
    LIKE_REVIEW(state, reviewId) {
      const review = state.reviews.find(item=> item.id === reviewId)
      if (review.is_liked) {
        review.is_liked = false;
        review.likes_count = review.likes_count - 1;
      } else {
        review.is_liked = true
        review.likes_count++;
      }
    }
  },
  actions: {
    postAuthData({ commit }, info) {
      axios
        .post(SERVER.URL + info.location, info.data)
        .then((res) => {
          commit('SET_TOKEN', res.data.token);
          router.push({ name: 'Home' });
        })
        .catch((err) => console.error(err.response.data));
    },
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.signup,
      };
      dispatch('postAuthData', info);
    },
    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.login,
      };
      dispatch('postAuthData', info);
    },
    logout({ getters, commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.logout, getters.config).then(() => {
        // 장고에선 삭제, cookie, state 엔 아직
        commit('SET_TOKEN', null);
        cookies.remove('auth-token');
        router.push({ name: 'Home' });
      });
      // .catch((err) => console.error(err.response.data));
    },

    initiateMoviesDB({ getters, commit }) {
      axios
        .post(SERVER.URL + SERVER.ROUTES.movies, null, getters.config)
        .then((res) => commit('SET_MOVIES', res.data))
        .catch((err) => console.error(err));
    },

    fetchMovies: async function({ commit, getters }, params) {
      try {
        const res = await axios.get(SERVER.URL + SERVER.ROUTES.movies, {
          ...getters.config,
          ...params,
        });
        const data = await res.data;
        commit('SET_MOVIES', data.results);
        console.log(data)
      } catch (err) {
        console.error(err);
      }
    },

    fetchMovie: async function({ getters }, movieId) {
      try {
        const res = await axios.get(
          SERVER.URL + SERVER.ROUTES.movies + movieId,
          getters.config
        );
        return res.data;
      } catch (err) {
        console.error(err);
      }
    },

    fetchReviews({ getters, commit }, movieId) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.movies + movieId + '/reviews/', {
          ...getters.config,
          params: { page: 1 },
        })
        .then((res) => {
          console.log(res.data);
          commit('SET_REVIEWS', res.data);
        })
        .catch((err) => console.error(err));
    },

    createReview({ getters, commit }, reviewData) {
      const {movieId, ...reviewDataForm} = reviewData
      console.log({...reviewData});
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.movies + movieId + '/reviews/',
          reviewDataForm,
          getters.config
        )
        .then((res) => {
          console.log(res.data);
          commit('ADD_REVIEW', res.data);
        })
        .catch((err) => console.error(err));
    },
    deleteReview({getters, commit}, reviewId) {
      axios.delete(SERVER.URL + SERVER.ROUTES.movies + 'reviews/' + reviewId + '/', getters.config).then((res) => {
        console.log(res.data);
        commit('DELETE_REVIEW', reviewId)
      }).catch((err) => console.error(err))
    },
    likeReview({getters, commit}, reviewId) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.movies + 'reviews/' + reviewId + '/like/',
          getters.config
        )
        .then((res) => {
          console.log(res.data);
          commit('LIKE_REVIEW', reviewId);
        })
        .catch((err) => console.error(err));
    },

    fetchRecommends({ getters, commit }, movieId) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.movies + movieId + '/recommend/',
          getters.config
        )
        .then((res) => {
          commit('SET_RECOMMENDS', res.data);
          return res.data;
        })
        .catch((err) => console.error(err));
    },
  },
  modules: {},
});
