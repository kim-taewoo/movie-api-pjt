import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Movies from '../views/Movies.vue';
import MovieDetail from '@/views/MovieDetail';
import Login from '@/views/Login';
import Signup from '@/views/Signup';
import MovieTrailer from '@/views/MovieTrailer';
import store from '../store';

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
    props: true,
  },
  {
    path: '/trailer',
    name: 'MovieTrailer',
    component: MovieTrailer,
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  },
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isLoggedIn;
  console.log(isAuthenticated);
  if (isAuthenticated) {
    next()
  } else {
    if (to.name === 'Login' || to.name === 'Signup') next()
    else next({name: 'Login'})
  }
});

export default router;
