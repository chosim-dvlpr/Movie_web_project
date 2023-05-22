import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieDetail from '@/views/movies/MovieDetail'
import MainView from '@/views/movies/MainView'
import ReviewList from '@/views/movies/ReviewList'
import ReviewCreate from '@/views/movies/ReviewCreate'
import ReviewDetail from '@/views/movies/ReviewDetail'
import ReviewModify from '@/views/movies/ReviewModify'

import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/moviedetail/:id',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/mainview',
    name: 'MainView',
    component: MainView,
  },
  {
    path: '/reviewlist/:id',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/reviewcreate',
    name: 'ReviewCreate',
    component: ReviewCreate,
  },
  {
    path: '/reviewdetail/:id',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path: '/reviewmodify/:id',
    name: 'ReviewModify',
    component: ReviewModify,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
