import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieDetail from '@/views/movies/MovieDetail'
import MainView from '@/views/movies/MainView'
import ArticleView from '@/views/movies/ArticleView'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/moviedetail',
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
    path: '/articleview',
    name: 'ArticleView',
    component: ArticleView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
