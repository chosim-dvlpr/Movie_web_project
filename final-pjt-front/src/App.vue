<template>
  <div id="app">
    <div id="nav">
      <div class="title">
        <span>CEMO</span>
        <span style="font-size:30px">Choose Entertaining Movies Ourselves</span>
      </div>
      <!-- v-if/v-else 디렉티브를 통해 로그인 여부에 따라 다른 링크들이 표시되도록 구성 -->
      <span v-if="isLogin" style="display:flex; justify-content:space-between;"> 
        
        <div style="position:absolute; top:40%; left:50px;">
          <!-- router-link 는 to 다음에 목표경로 설정, a tag와 비슷한 역할 -->
          <router-link :to="{ name: 'MainView' }">Main</router-link>
          <!-- <router-link :to="{ name: 'UserProfile' }">UserProfile</router-link> -->
        </div>
        <div class="hello_user">
          <p>{{ userName }}님, 안녕하세요!</p>
          <router-link :to="{ name: 'UserProfile' }">Profile</router-link>
          <!--.native : 현재 컴포넌트에 요청을 보내기 위해 사용 -->
          <router-link to="#" @click.native="logout">Logout</router-link> 
        </div>

      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fffdef;
  background-color: black;
  width: 100%;
  height: 5000px;
}

#nav {
  padding: 30px;
  z-index: 3;
  text-align: right;
  background-color: #FFD700;
  position:fixed;
  display: flex;
  justify-content: flex-end;
  align-items: flex-start;
  width: 100%;
  height: 180px;
}

#nav a {
  font-weight: bold;
  color: black;
}

#nav a.router-link-exact-active {
  color: #5c4e00;
}

.hello_user {
  display: flex;
  position: relative;
  right: 15px;
  margin-top: 20px;
  flex-direction: column;
  color: #5c4e00;
  font-size: 15px;
}

.title {
  display: flex;
  position: absolute;
  justify-content: center;
  margin: auto;
  left:38%;
  font-size: 50px;
  font-weight: bold;
  flex-direction: column;
  align-items: center;
  color: black;
  padding-bottom: 29px;
}

</style>
