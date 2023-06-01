<template>
  <div id="app">
    <div id="nav">
      <div v-if="!isLogin" class="not-login-title">
        <!-- <div class="not-login-title"> -->
          <span class="shadow_title">CEMO</span>
          <span class="shadow_title" style="font-size:30px">Choose Entertaining Movies Ourselves</span>
        <!-- </div> -->
      </div>
      <!-- v-if/v-else 디렉티브를 통해 로그인 여부에 따라 다른 링크들이 표시되도록 구성 -->
      <!-- <div v-if="isLogin" style="display:flex; justify-content:space-between;">  -->
      <div v-if="isLogin" class="is-login"> 
        <div class="login-title">
          <span>CEMO</span>
        </div>
        <!-- <div style="position:absolute; top:40%; left:0px;"> -->
        <div id="main-button">
          <!-- router-link 는 to 다음에 목표경로 설정, a tag와 비슷한 역할 -->
          <router-link :to="{ name: 'MainView' }">Main</router-link>
        </div>
        <div class="hello_user">
          <p>{{ userName }}님, 안녕하세요!</p>
          <router-link :to="{ name: 'UserProfile' }">Profile</router-link>
          <!--.native : 현재 컴포넌트에 요청을 보내기 위해 사용 -->
          <router-link to="#" @click.native="logout">Logout</router-link> 
        </div>
      </div>
      <div v-else class="is-not-login">
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </div>
    </div>
    <router-view @login="isLogin=true"/> <!--라우터뷰는 클릭시 주어진 URL과 일치하는 컴포넌트를 렌더링, 장고의 block tag 와 비슷하다. -->
  </div>
</template>

<script>

// import axios from 'axios'

// const URL = "https://www.googleapis.com/youtube/v3/videos"

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      userName: localStorage.getItem('username'),
    }
  },
  methods: {
      logout: function() {                  // logout 메서드 정의하는데, 로그아웃을 처리하기 위해 사용.
        this.isLogin = false                // isLogin 을 false 로 설정.
        localStorage.removeItem('jwt')      // 로컬스토리지에서 jwt 제거
        this.$router.push({ name: 'Login' })  // 로그인 페이지로 이동
      },
    },
  created() {                        // 앱이 생성될떄 호출되는 함수 정의(라이프사이클훅)
    const token = localStorage.getItem('jwt')   // 로컬스토리지에서 jwt(JSON Web Token을 나타내며, 로그인한 사용자를 인증하는 데 사용되는 토큰) 값을 가져와서 token이라는 변수에 할당.
    if (token) {                                // 토큰에 값이 있다면
      this.isLogin = true                       // isLogin 을 false 에서 true 로 변환     
    }
    this.userName = localStorage.getItem('username')
  },
  mounted() {
    this.userName = localStorage.getItem('username')
  }
}

</script>


<style scoped>
@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 100;
    font-style: normal;
}

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  /* color: #fffdef; */
  background-color: black;
  width: 100%;
  height: 100%;
}

#nav {
  z-index: 1;
  text-align: right;
  background-color: #FFD700;
  position:fixed;
  display: grid;
  /* grid-template-columns: repeat(2, 1fr); */
  justify-items: center;
  width: 100%;
  height: 180px;
}

#nav a {
  font-weight: bold;
  color: black;
}

#nav a.router-link-exact-active {
  color: #2c2500;
}

.hello_user {
  display: flex;
  position: absolute;
  right: 50px;
  margin-top: 46.5px;
  flex-direction: column;
  color: #5c4e00;
  font-size: 15px;
}

.not-login-title {
  display: grid;
  position: relative;
  justify-items: center;
  align-content: center;
  font-size: 50px;
  font-weight: bold;
  color: black;
}

.shadow_title {
  text-shadow: 0 1px 1px rgba(0,0,0,0.15), 
              0 2px 2px rgba(0,0,0,0.15), 
              0 4px 4px rgba(0,0,0,0.15), 
              0 8px 8px rgba(0,0,0,0.15);
}

.is-login {
  display: grid;
  position: relative;
  width: 100%;
  justify-content: space-around;
}

.is-not-login {
  display: flex;
  position: absolute;
  justify-content: flex-end;
  align-items: center;
  width: 100%;
  height: 100%;
  margin-right: 50px;
}

/* .login-title-box {
  position: absolute;
  background-color: blue;
} */

.login-title {
  display: grid;
  position: absolute;
  justify-items: start;  
  font-size: 40px;
  font-weight: bold;
  color: black;
  line-height: 180px;
  margin-left: 50px;
  text-shadow: 3px 3px #3333334e;
}

#main-button {
  position: relative;
  display: flex;
  justify-content: start;
  line-height: 180px;
  
  /* width: 100%; */
  /* left: -300px; */
}

</style>
