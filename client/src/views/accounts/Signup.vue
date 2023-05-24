<template>
  <div>
    <h1>SignUp</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="userdata.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="userdata.password">
    </div>
    <div>
      <label for="paswordConfirm">비밀번호 확인: </label>
      <input type="password" id="passwordConfirm" @keyup.enter="signup" v-model="userdata.passwordConfirm">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios' 

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'Signup', 
  data: function () {
    return {
      userdata: {
        username: null,
        password: null,
        passwordConfirm: null,
      },
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: this.userdata, 
      })
      .then(() => {
        this.$router.push({ name: 'Login' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
