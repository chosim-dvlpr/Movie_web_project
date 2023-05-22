<template>
  <div>
    <h1>여기는 리뷰 디테일 페이지 ~ ! ^.^ </h1>
    <div>
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
            title: null,
            content: null,
            rating: null,
            recommendation: null,
        }
    },
    methods: {
        modifyReview(review) {
            const modifyItem = {
                id: review.id,
                title: review.title,
                content: review.content,
                rating: review.rating,
                recommendation: review.recommendation,
            }
            axios({
                method: 'put',
                url: `${API_URL}/api/movies/reviewdetail/`,
                data: modifyItem,
            })
            .then(res => {
                console.log(res.data)
                this.reviewList.push(res.data)
                // console.log(this.reviewList)
            })
            .catch(err => {
                console.log(err)
            })
        },
        deleteReview() {
            axios({
                method: 'delete',
                url: `${API_URL}/api/movies/reviewdetail/`,
            })
            .then(res => {
                console.log(res.data)
                this.reviewList.push(res.data)
                // console.log(this.reviewList)
            })
            .catch(err => {
                console.log(err)
            })
        },
    },
    created() {
        // this.title = this.$route.params.review.title
        // this.content = this.$route.params.review.content
        // this.rating = this.$route.params.review.rating
        // this.recommendation = this.$route.params.review.recommendation
        axios({
            method: 'get',
            url: `${API_URL}/api/movies/${this.$route.params.review.id}/reviewdetail/`,
        })
        .then(res => {
            this.title = res.data.title
            this.content = res.data.content
            this.rating = res.data.rating
            this.recommendation = res.data.recommendation

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