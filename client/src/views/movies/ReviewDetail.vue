<template>
  <div>
    <h1>여기는 리뷰 디테일 페이지 ~ ! ^.^ </h1>
    <div>
        <div>
            <h1>review id : {{ this.review.id }}</h1>
            <h1>movie Id : {{ this.review.movie }}</h1>
            <p>제목 : {{ this.review.title }}</p>
            <p>작성자 : <span @click="goToProfile">{{ this.userName }}</span></p>
            <p>내용 : {{ this.review.content }}</p>
            <p>평점 : {{ this.review.rating }}</p>
            <p>추천 : {{ this.review.recommendation }}</p>
            <hr>
        </div>
        <div>
            <h2>Comments</h2>
            <input type="text" v-model="comment" @keyup.enter="submitComment">
            <button @click="submitComment">작성</button>
            <div>
                <span v-for="commentObject in this.commentList" :key="commentObject.id">
                    <p>{{ commentObject.user.username }} : {{ commentObject.content }}
                    <button @click="deleteComment(commentObject.id)">삭제</button></p>
                </span>
            </div>
        </div>
        <hr>
        <div>
            <button @click="modifyReview">리뷰 수정하기</button>
            <button @click="deleteReview">리뷰 삭제하기</button>
        </div>
        <button @click="goToReviewList">뒤로가기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ReviewDetail',
    data() {
        return {
            review: JSON.parse(localStorage.getItem("reviewdetail")) || "",
            reviewList: JSON.parse(localStorage.getItem("reviewList")) || "",
            reviewId: null,
            title: null,
            content: null,
            rating: null,
            recommendation: null,
            movieId: null,

            // user
            userName: null,
            currentUserName: localStorage.getItem("username"),
            userId: null,

            // comment
            comment: null,
            commentList: [],
        }
    },
    // mounted() {
    //     this.getComments()
    // },
    methods: {
        setToken: function() {
        const token = localStorage.getItem('jwt')
        const config = {
            Authorization: `Bearer ${token}`
        }
        return config
        },
        // 리뷰 수정
        modifyReview() {
            if (this.userName === this.currentUserName) {
                const newReview = {
                    reviewId: this.review.id,
                    movieId: this.review.movie,
                    title: this.review.title,
                    content: this.review.content,
                    rating: this.review.rating,
                    recommendation: this.review.recommendation,
                }
                // console.log(getUserId())
                this.$router.push({ name: 'ReviewModify', params: { id: this.reviewId, review: newReview }})
            } else {
                alert('수정할 수 없습니다!')
            }
        },

        // 리뷰 삭제
        deleteReview() {
            if (this.userName === this.currentUserName) {
                axios({
                    method: 'delete',
                    url: `${API_URL}/api/movies/${this.review.id}/reviewdetail/`,
                    // headers: this.setToken(),
                })
                .then(res => {
                    // console.log(res.data)
                    alert('리뷰가 삭제되었습니다!')
                    this.$router.push({ name: 'ReviewList', params: { id: this.review.movie }})
                    this.reviewList.removeItem(res.data)
                })
                .catch(err => {
                    console.log(err)
                })
            } else {
                alert('삭제할 수 없습니다!')
            }
        },

        // 리뷰 리스트로 이동
        goToReviewList() {
            this.$router.push({ name: 'ReviewList', params: { id: this.review.movie }})
        },
        // 댓글 불러오기
        getComments() {
            axios({
                method: 'get',
                url: `${API_URL}/api/movies/${this.review.id}/reviewdetail/commentlist/`,
                headers: this.setToken(),
            })
            .then(res => {
                console.log("***************************"+JSON.stringify(res.data))
                this.commentList = res.data
                console.log(this.commentList)
            })
            .catch(err => {
                console.log(err)
            })
        },
        // 댓글 입력
        submitComment() {
            const newComment = {
                content: this.comment,
            }
            axios({
                method: 'post',
                url: `${API_URL}/api/movies/${this.review.id}/reviewdetail/comment/`,
                data: newComment,
                headers: this.setToken(),
            })
            .then(res => {
                const commentItem = res.data.content
                const user = { "username" : res.data.user.username }
                const newCommentItemUserName = {
                    content: commentItem,
                    user: user
                }
                this.commentList.push(newCommentItemUserName)
                this.comment = ''
                this.getComments()
            })
            .catch(err => {
                console.log(err)
            })
        },

        // 댓글 삭제
        deleteComment(comment_pk) {
            // if (this.userName === this.currentUserName) {
                axios({
                    method: 'delete',
                    url: `${API_URL}/api/movies/comment/${comment_pk}`,
                    // headers: this.setToken(),
                })
                .then(() => {
                    alert('리뷰가 삭제되었습니다!')
                    // console.log(res)
                    // this.$router.push({ name: 'ReviewList', params: { id: this.review.movie }})
                    // this.commentList.removeItem(res.data)

                    console.log(this.commentList)
                    this.getComments()
                })
                .catch(err => {
                    console.log(err)
                })
            // } else {
            //     alert('삭제할 수 없습니다!')
            // }
        },

        // 프로필로 이동
        goToProfile() {
            this.$router.push({ name: 'UserProfile' })
        },
    },
    created() {
        this.getComments(),
        axios({
            method: 'get',
            url: `${API_URL}/api/movies/${this.review.id}/reviewdetail/`,
        })
        .then(res => {
            // console.log('_'+JSON.stringify(res.data.user.username))
            this.movieId = JSON.stringify(res.data.movie.id)
            this.userName = JSON.stringify(res.data.user.username).replace(/"/g, '')
            this.userId = JSON.stringify(res.data.user.id)
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>

<style>

</style>