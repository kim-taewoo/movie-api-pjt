import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Movies from '../views/Movies.vue';
import MovieDetail from '@/views/MovieDetail';
import Login from '@/views/Login'
import Signup from '@/views/Signup'
import MovieTrailer from '@/views/MovieTrailer'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies,
  },
  {
    path: '/movies/:id',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/trailer',
    name: 'MovieTrailer',
    component: MovieTrailer,
    props: true
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
