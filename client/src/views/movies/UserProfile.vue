<template>
    <div>
        <h1>여기는 {{ username }}님의 Profile 페이지</h1>
        <p>current user : {{ this.currentUserName }}</p>
        <div>
            <p>{{ username }}님을 팔로우하는 사람 : {{ }} 명</p>
            <p>{{ username }}님이 팔로잉하는 사람 : {{ }} 명</p>
        </div>
        <!-- profile 주인의 정보와 접속한 사람의 정보가 다르다면 팔로우 버튼 표시 -->
        <!-- 팔로우하지 않은 상태라면 팔로우하기 버튼을, 팔로우한 상태라면 팔로잉 취소 버튼 -->
        <div v-if="!this.isUser">
            <div v-if="!isFollowing">
                <button>팔로우하기</button>
            </div>
            <div v-else>
                <button>팔로우 취소하기</button>
            </div>
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
            username: null,
            userId: null,
            currentUserName: localStorage.getItem('username'),
            currentUserId: null,
            isUser: false,
        }
    },
    methods: {
        // User 정보 불러오기
        getUser() {
            axios({
                method: 'get',
                url: `${API_URL}/accounts/${this.username}/`,
                headers: this.setToken(),
            })
            .then(res => {
                console.log(res)})
            .catch(err => {
                console.log(err)
            })
        },
    },
    created() {
        this.getUser()
        
        // 프로필 주인 정보와 접속한 사람의 정보 확인
        // 정보가 같다면 true, 다르다면 false
        if (this.userId === this.currentUserId) {
            return true
        } else {
            return false
        }
    },
}
</script>

<style>

</style>