<template>
  <div>
    <h1>여기는 리뷰 디테일 페이지 ~ ! ^.^ </h1>
    <div>
        <h1>review id : {{ this.reviewId }}</h1>
        <h1>movie Id : {{ this.movieId }}</h1>
        <p>제목 : {{ this.title }}</p>
        <p>내용 : {{ this.content }}</p>
        <p>평점 : {{ this.rating }}</p>
        <p>추천 : {{ this.recommendation }}</p>
        <button @click="modifyReview">리뷰 수정하기</button>
        <button @click="deleteReview">리뷰 삭제하기</button>
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
                reviewId: this.reviewId,
                title: this.title,
                content: this.content,
                rating: this.rating,
                recommendation: this.recommendation,
                movieId: this.movieId,
            }
            console.log()
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
                url: `${API_URL}/api/movies/reviewdetail/`,
            })
            .then(res => {
                // console.log(res.data)
                this.reviewList.remove(res.data)
                // console.log(this.reviewList)
            })
            .catch(err => {
                console.log(err)
            })
        },
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