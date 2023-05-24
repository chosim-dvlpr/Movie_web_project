<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="userdata.username">
    </div>
    <div>
      <label for="pasword">비밀번호 확인: </label>
      <input type="password" id="passwordConfirm" @keyup:enter="login" v-model="userdata.password">
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Login',
  data: function () {
    return {
      userdata: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${API_URL}/api/token/`,
        data: this.userdata, 
      })
      .then((res) => {
        // console.log(res.config)
        localStorage.setItem("jwt", res.data.access)
        this.getUser()
        this.$emit('login')
        this.$router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUser() {
      // server에서 user 정보를 불러옴
      axios({
        method: 'get',
        url: `${API_URL}/accounts/login/`,
        headers: this.setToken(),
      })
      .then((res) => {
        // console.log(res.data.userId)
        localStorage.removeItem("username")
        localStorage.removeItem("userId")
        console.log(res.data.username)
        localStorage.setItem("username", res.data.username)
        localStorage.setItem("userId", res.data.userId)
      })
      .catch((err) => {
        console.log(err)
      })
      },
      setToken: function() {
        const token = localStorage.getItem('jwt')
        const config = {
            Authorization: `Bearer ${token}`
        }
        return config
      },
  }
}
    
  

</script>
