<template>
  <main id="main-login">
    <h1 id="login-header">Login</h1>
    <!-- 로그인 오류 시 에러 메세지 -->
    <div id="login-err-msg-holder">
      <p id="login-err-msg" :style="{ opacity : isError }" >Invalid username <span id="err-msg-second-line">and/or password</span></p>
    </div>
    
    <!-- 로그인 폼 -->
    <form id="login-form">
      <!-- <label for="username">Username : </label> -->
      <input type="text" name="username" id="username" class="login-form-field" v-model="userdata.username" placeholder="Username">

      <!-- <label for="password">Password : </label> -->
      <input type="password" name="password" id="password" class="login-form-field" @keyup.enter="login" v-model="userdata.password" placeholder="Password">
      
      <input type="submit" id="login-form-submit" @click="login" value="Login">
      <!-- <button type="submit" @click="login" id="login-form-submit">로그인</button> -->
    </form>
  </main>

    <!-- <div class="login">
    <div class="input_box">
      <div style="align-items:center; margin:auto;">
        <h1>Login</h1>
      </div>
          <div>
            <label for="username">사용자 이름: </label>
            <input type="text" id="username" v-model="userdata.username">
          </div>
          <div>
            <label for="pasword">비밀번호 확인: </label>
            <input type="password" id="passwordConfirm" @keyup.enter="login" v-model="userdata.password">
          </div>
      <button @click="login" style="margin:auto;">로그인</button>
    </div>
  </div> -->
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
      },
      isError: 0,
    }
  },
  methods: {
    login: function (event) {
      // event가 재실행되는 것을 막아줌 (input 또는 button클릭 시 페이지가 reload되는 것을 막음)
      event.preventDefault()
      axios({
        method: 'post',
        url: `${API_URL}/api/token/`,
        data: this.userdata, 
      })
      .then((res) => {
        sessionStorage.setItem("jwt", res.data.access)
        this.getUser()
        this.$emit('login')
        alert("You have successfully logged in.")
        this.$router.push({ name: 'MainView' })
      })
      .catch((err) => {
        this.isError = 1
        if (err.response.status === 401) {
          alert("Username/Password is invalid!")
        } else if (err.response.status === 400) {
          alert("Username/Password is empty!")
        }
      })
      return false
    },
    getUser() {
      // server에서 user 정보를 불러옴
      axios({
        method: 'get',
        url: `${API_URL}/accounts/login/`,
        headers: this.setToken(),
      })
      .then((res) => {
        // localStorage.removeItem("username")
        // localStorage.removeItem("userId")
        sessionStorage.setItem("username", res.data.username)
        sessionStorage.setItem("userId", res.data.userId)
      })
      .catch((err) => {
        console.log(err)
      })
      },
      setToken: function() {
        const token = sessionStorage.getItem('jwt')
        const config = {
            Authorization: `Bearer ${token}`
        }
        return config
      },
  },
}
    
  

</script>

<style scoped>
#main-login {
  position: relative;
  top: 200px;
  align-items: center;
  margin: auto;

  width: 50%;
  height: 50%;
  display: grid;
  justify-items: center;
  background-color: rgb(0, 0, 0);
  border-radius: 7px;
  box-shadow: 0px 0px 5px 2px black;
  color: white;
}

#login-err-msg-holder {
  width: 100%;
  height: 100%;
  display: grid;
  justify-items: center;
  align-items: center;
}

#login-err-msg {
  width: 23%;
  text-align: center;
  margin: 0;
  padding: 5px;
  font-size: 12px;
  font-weight: bold;
  color: #8a0000;
  border: 1px solid #8a0000;
  background-color: #e8a8a8;
  /* 로그인 에러 시 opacity(투명도) 변경 */
  opacity: 0;
}

#err-msg-second-line {
  display: block;
}

#login-form {
  align-self: flex-start;
  display: grid;
  justify-items: center;
  align-items: center;
}

.login-form-field::placeholder {
  color: #3a3a3a;
}

.login-form-field {
  border: none;
  border-bottom: 1px solid #3a3a3a;
  margin-bottom: 10px;
  border-radius: 3px;
  outline: none;
  padding: 0px 0px 5px 5px;
}

#login-form-submit {
  width: 100%;
  padding: 7px;
  border: none;
  border-radius: 5px;
  color: white;
  font-weight: bold;
  background-color: #3a3a3a;
  cursor: pointer;
  outline: none;
}


/* 
.input_box {
  display: flex;
  align-items: flex-end;
  flex-direction: column;
  margin: 5px;
}

.input_box > div {
  margin: 3px;
} */




</style>