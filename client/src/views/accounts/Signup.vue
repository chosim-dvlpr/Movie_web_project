<template>
  <div class="signup">
    <div class="signup_box">
      <div class="input_box">
        <div style="align-items:center; margin:auto;">
          <h1>SignUp</h1>
        </div>
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
      </div>
      <button @click="signup">회원가입</button>
    </div>
    <div class="logo_triangle"></div>
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
<style scoped>
.signup {
  position: relative;
  top: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* .signup_box {
  border: 1px solid yellow;
  padding: 30px;
  border-radius: 5px;
} */

/* .logo_triangle {
  display: flex;
  position: relative;
  z-index: 0;
  width: 0px;
  height: 0px;
  border-bottom: 360px solid #FFD700;
  border-left: 180px solid transparent;
  border-right: 180px solid transparent;
  } */

.input_box {
  display: flex;
  align-items: flex-end;
  flex-direction: column;
  margin: 5px;
}

.input_box > div {
  margin: 3px;
  /* align-items: flex-end; */

}
</style>