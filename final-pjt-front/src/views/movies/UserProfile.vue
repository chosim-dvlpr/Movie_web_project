<template>
    <div class="profile">
        <h1 style="margin-top:20px;">{{ this.userName }}님의 Profile 페이지</h1>
        <br>
        <div class="whois_following">
            <p>{{ this.userName }}님을 팔로우하는 사람 : {{ this.followers }} 명</p>
            <p>{{ this.userName }}님이 팔로잉하는 사람 : {{ this.followings }} 명</p>
        </div>
        <!-- profile 주인의 정보와 접속한 사람의 정보가 다르다면 팔로우 버튼 표시 -->
        <!-- 팔로우하지 않은 상태라면 팔로우하기 버튼을, 팔로우한 상태라면 팔로잉 취소 버튼 -->
        <div v-if="!this.isUser">
            <span v-if="!isFollowing">
                <button @click="clickFollow">팔로우하기</button>
            </span>
            <span v-else>
                <button @click="clickFollow">팔로우 취소하기</button>
            </span>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'UserProfile',
    data() {
        return {
            userName: localStorage.getItem('username'),
            userId: null,
            currentUserName: localStorage.getItem('username'),
            currentUserId: localStorage.getItem('userId'),
            isUser: false, // 프로필 페이지의 유저와 로그인한 유저가 다르면 true
            isFollowing: false,

            followers: 0,
            followings: 0,
        }
    },
    methods: {
        // User 정보 불러오기
        // getUser() {
        //     axios({
        //         method: 'get',
        //         url: `${API_URL}/accounts/login/`,
        //         headers: this.setToken(),
        //     })
        //     .then(res => {
        //         this.userId = res.data.userId
        //         this.userName = res.data.username
        //     })
        //     .catch(err => {
        //         console.log(err)
        //     })
        // },

        // 팔로잉 버튼 클릭
        clickFollow() {
            axios({
                method: 'post',
                url: `${API_URL}/accounts/${this.userName}/follow/`,
                data: this.userName,
                headers: this.setToken(),
            })
            .then(res => {
                // console.log(JSON.stringify(res["data"]))
                this.isFollowing = JSON.stringify(res["data"]["is_followed"])
                this.following = JSON.stringify(res["data"]["followings_count"])
                this.followers = JSON.stringify(res["data"]["followers_count"])
            })
            .catch(err => {
                console.log(err)
            })
        },
        // 토큰
        setToken: function() {
        const token = localStorage.getItem('jwt')
        const config = {
            Authorization: `Bearer ${token}`
        }
        return config
      },
    },
    created() {
        // this.getUser()

        // 프로필 주인 정보와 접속한 사람의 정보 확인
        // 정보가 다르면 true, 같으면 false(디폴트)
        if (this.userId !== this.currentUserId) {
            this.isUser = true
        }
        // this.userName = this.$route.params.id
    },
}
</script>

<style>
.profile {
  position: relative;
  top: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 5px solid #FFD700;
  border-radius: 5px;
  width: 800px;
  height: 500px;
  align-items: center;
  justify-content: flex-start;
  margin: auto;
  padding: 100px;
  box-shadow: 2px 2px 10px gray;
}


.whois_following {
    font-size: 25px;
}
</style>