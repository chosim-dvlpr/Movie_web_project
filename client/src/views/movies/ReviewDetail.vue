<template>
  <div>
    <h1>여기는 리뷰 디테일 페이지 ~ ! ^.^ </h1>
    <div>
        <h1>review id : {{ this.review.id }}</h1>
        <h1>movie Id : {{ this.review.movie }}</h1>
        <p>제목 : {{ this.review.title }}</p>
        <p>내용 : {{ this.review.content }}</p>
        <p>평점 : {{ this.review.rating }}</p>
        <p>추천 : {{ this.review.recommendation }}</p>
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
        }
    },
    methods: {
        modifyReview() {
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
            
            // this.$emit('modify-review', newReview)
        },
        // modifyReview(review) {
        //     const modifyItem = {
        //         id: review.id,
        //         title: review.title,
        //         content: review.content,
        //         rating: review.rating,
        //         recommendation: review.recommendation,
        //     }
        //     axios({
        //         method: 'put',
        //         url: `${API_URL}/api/movies/reviewdetail/`,
        //         data: modifyItem,
        //     })
        //     .then(res => {
        //         // console.log(res.data)
        //         this.reviewList.push(res.data)
        //         // console.log(this.reviewList)
        //     })
        //     .catch(err => {
        //         console.log(err)
        //     })
        // },
        deleteReview() {
            // const reviewId = this.$route.params.id;
            axios({
                method: 'delete',
                url: `${API_URL}/api/movies/${this.review.id}/reviewdetail/`,
                headers: this.setToken(),
            })
            .then(res => {
                // console.log(res.data)
                this.$router.push({ name: 'ReviewList', params: { id: this.review.movie }})
                this.reviewList.removeItem(res.data)
                // console.log(this.reviewList)
            })
            .catch(err => {
                console.log(err)
            })
        },
        goToReviewList() {
            this.$router.push({ name: 'ReviewList', params: { id: this.review.movie }})
        }
    },
    created() {
        this.title = this.$route.params.review.title
        this.content = this.$route.params.review.content
        this.rating = this.$route.params.review.rating
        this.recommendation = this.$route.params.review.recommendation
        this.reviewId = this.$route.params.review.id
        // console.log(this.reviewId+'여기')
        // console.log(this.$route.params.review.id)
        console.log(this.reviewId)
        axios({
            method: 'get',
            url: `${API_URL}/api/movies/${this.$route.params.review.id}/reviewdetail/`,
        })
        .then(res => {
            this.movieId = res.data.movie.id
            // this.reviewId = res.data.id
            // this.title = res.data.title
            // this.content = res.data.content
            // this.rating = res.data.rating
            // this.recommendation = res.data.recommendation

            // console.log(res)
            // this.reviewList.push(res.data)
            // console.log(this.reviewList)
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>

<style>

</style>