import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieDetail from '@/views/movies/MovieDetail'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/moviedetail/:id',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  // {
  //   path: '/todos/create',
  //   name: 'CreateTodo',
  //   component: CreateTodo,
  // },
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
