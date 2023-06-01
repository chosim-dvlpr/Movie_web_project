<template>
  <main id="main-signup">
    <h1 id="signup-header">Sign Up</h1>
    <!-- 입력 오류 시 에러 메세지 -->
    <div id="signup-err-msg-holder">
      <p id="signup-err-msg" :style="{ opacity : isError }" >Invalid username <span id="err-msg-second-line">and/or password</span></p>
    </div>
    
    <!-- 회원가입 폼 -->
    <form id="signup-form">
      <!-- <label for="username">Username : </label> -->
      <input type="text" name="username" id="username" class="signup-form-field" v-model="userdata.username" placeholder="Username">

      <!-- <label for="password">Password : </label> -->
      <input type="password" name="password" id="password" class="signup-form-field" v-model="userdata.password" placeholder="Password">
      
      <input type="password" id="passwordConfirm" class="signup-form-field" @keyup.enter="signup" v-model="userdata.passwordConfirm" placeholder="Password Confirm">
      <input type="submit" id="signup-form-submit" @click="signup" value="signup">
      <!-- <button type="submit" @click="signup" id="signup-form-submit">로그인</button> -->
    </form>
  </main>
  <!-- <div class="signup">
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
  </div> -->
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
      isError: 0,
    }
  },
  methods: {
    signup: function (event) {
      event.preventDefault()
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: this.userdata, 
      })
      .then(() => {
        alert("You have successfully signed up.")
        this.$router.push({ name: 'Login' })
      })
      .catch((err) => {
        this.isError = 1
        if (err.response.status === 400) {
          alert("Username already exists!")
        } 
      })
    }
  }
}
</script>
<style scoped>

#main-signup {
  position: relative;
  top: 200px;
  align-items: center;
  margin: auto;

  width: 50%;
  height: 50%;
  display: grid;
  justify-items: center;
  background-color: beige;
  border-radius: 7px;
  box-shadow: 0px 0px 5px 2px black;
}

#signup-err-msg-holder {
  width: 100%;
  height: 100%;
  display: grid;
  justify-items: center;
  align-items: center;
}

#signup-err-msg {
  width: 23%;
  text-align: center;
  margin: 0;
  padding: 5px;
  font-size: 12px;
  font-weight: bold;
  color: #8a0000;
  border: 1px solid #8a0000;
  background-color: #e58f8f;
  /* 로그인 에러 시 opacity 변경 */
  opacity: 0;
}

#err-msg-second-line {
  display: block;
}

#signup-form {
  align-self: flex-start;
  display: grid;
  justify-items: center;
  align-items: center;
}

.signup-form-field::placeholder {
  color: #3a3a3a;
}

.signup-form-field {
  border: none;
  border-bottom: 1px solid #3a3a3a;
  margin-bottom: 10px;
  border-radius: 3px;
  outline: none;
  padding: 0px 0px 5px 5px;
}

#signup-form-submit {
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

/* .signup {
  position: relative;
  top: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
} */

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

/* .input_box {
  display: flex;
  align-items: flex-end;
  flex-direction: column;
  margin: 5px;
}

.input_box > div {
  margin: 3px;
} */


</style>