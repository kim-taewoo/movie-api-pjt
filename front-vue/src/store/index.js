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
    reviews: []
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
        .post(SERVER.URL + SERVER.ROUTES.movieList, null, getters.config)
        .then((res) => commit('SET_MOVIES', res.data))
        .catch((err) => console.error(err));
    },

    fetchMovies: async function({ commit, getters }, params) {
      try {
        const res = await axios.get(SERVER.URL + SERVER.ROUTES.movieList, {
          ...getters.config,
          ...params,
        });
        const data = await res.data;
        commit('SET_MOVIES', data.results);
      } catch (err) {
        console.error(err);
      }
    },

    fetchMovie: async function({getters}, movieId) {
      try {
        const res = await axios.get(SERVER.URL + SERVER.ROUTES.movieDetail + movieId, getters.config)
        const data = await res.data[0];
        return data;
      } catch (err) {
        console.error(err);
      }
    },

    fetchReviews({ getters, commit }, movieId) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.reviewList + movieId + '/reviews/',
          getters.config
        )
        .then((res) => {
          commit('SET_REVIEWS', res.data);
          return res.data;
        })
        .catch((err) => console.error(err));
    },

    fetchRecommends({ getters, commit }, movieId) {
      axios
        .get(
          SERVER.URL + SERVER.ROUTES.recommendList + movieId + '/recommend/',
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
