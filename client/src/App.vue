<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin"> <!-- v-if/v-else 디렉티브를 통해 로그인 여부에 따라 다른 링크들이 표시되도록 구성 -->
        <!-- router-link 는 to 다음에 목표경로 설정, a tag와 비슷한 역할 -->
        <router-link :to="{ name: 'MainView' }">Main</router-link> | 
        <router-link :to="{ name: 'ReviewList' }">ReviewList</router-link> | 
        <router-link :to="{ name: 'ReviewCreate' }">ReviewCreate</router-link> | 
        <router-link to="#" @click.native="logout">Logout</router-link> 
        <!--.native : 현재 컴포넌트에 요청을 보내기 위해 사용 -->
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


export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function() {                  // logout 메서드 정의하는데, 로그아웃을 처리하기 위해 사용.
      this.isLogin = false                // isLogin 을 false 로 설정.
      localStorage.removeItem('jwt')      // 로컬스토리지에서 jwt 제거
      this.$router.push({name: 'Login'})  // 로그인 페이지로 이동
    }
  },
  created () {                        // 앱이 생성될떄 호출되는 함수 정의(라이프사이클훅)
    const token = localStorage.getItem('jwt')   // 로컬스토리지에서 jwt(JSON Web Token을 나타내며, 로그인한 사용자를 인증하는 데 사용되는 토큰) 값을 가져와서 token이라는 변수에 할당.
    if (token) {                                // 토큰에 값이 있다면
      this.isLogin = true                       // isLogin 을 false 에서 true 로 변환     
    }
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
