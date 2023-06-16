<template>
  <div class="review_detail">
    <h1>Review Detail</h1>
    <br>
    <div>
        <div>
            <p>제목 : {{ this.review.title }}</p>
            <p>작성자 : <button @click="goToProfile">{{ this.userName }}</button></p>
            <p>내용 : {{ this.review.content }}</p>
            <p>평점 : {{ this.review.rating }}</p>
            <p style="color:#FFD700;" v-if="review.recommendation">
                이 영화를 추천합니다.
            </p>
            <hr>
        </div>
        <div>
            <h2>Comments</h2>
            <input type="text" v-model="comment" @keyup.enter="submitComment">
            <button @click="submitComment">작성</button>
            <div>
                <span v-for="commentObject in this.commentList" :key="commentObject.id">
                    <p class="comment-detail" >{{ commentObject.user.username }} : {{ commentObject.content }}
                    <button @click="deleteComment(commentObject.id)">삭제</button></p>
                </span>
            </div>
        </div>
        <hr>
        <div>
            <button @click="modifyReview">리뷰 수정하기</button>
            <button @click="deleteReview">리뷰 삭제하기</button>
        </div>
        <br>
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
            review: JSON.parse(sessionStorage.getItem("reviewdetail")) || "",
            reviewList: JSON.parse(sessionStorage.getItem("reviewList")) || "",
            reviewId: null,
            title: null,
            content: null,
            rating: null,
            recommendation: null,
            movieId: null,

            // user
            userName: null,
            currentUserName: sessionStorage.getItem("username"),
            userId: null,

            // comment
            comment: null,
            commentList: [],
        }
    },
    methods: {
        setToken: function() {
        const token = sessionStorage.getItem('jwt')
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
                })
                .then(res => {
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
                this.commentList = res.data
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
                })
                .then(() => {
                    alert('댓글이 삭제되었습니다!')
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
            sessionStorage.setItem('profile_user', this.userName)
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
.review_detail {
    position: relative;
    top: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: white;
}

button {
    background-color: beige;
    border-radius: 4%;
}

button:hover {
    transition-duration: 0.1s;
    background-color: #FFD700;
}

.comment-detail {
    margin-top: 5px;
}
</style>