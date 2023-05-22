<template>
  <div>
    <h1>여기는 ReviewList</h1>
    <h2>리뷰 리스트 페이지</h2>
    <hr>    
    <p>movie id : {{ this.movieId }}</p>
    <!-- <p>{{ this.reviewList[0] }}</p> -->
    <!-- <p>{{ this.reviewList }}</p> -->
    <span v-for="(review, index) in reviewList[0].filter((word) => word.movie === this.movieId)" :key="index">
      <span @click="goToReviewDetail(review)">
          <p>리뷰 제목 : {{ review.title }}</p>
          <p>내용 : {{ review.content }}</p>
          <p>평점 : {{ review.rating }}</p>
          <p>이 영화를 추천합니다 : {{ review.recommendation }}</p>
          <!-- <button @click="modifyReview">리뷰 수정하기</button>
          <button @click="deleteReview">리뷰 삭제하기</button> -->
          <hr>
      </span>
    </span>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ReviewList',
    data() {
        return {
            reviewList: [],
            movieId: null,
            // reviewList: this.$route.params.reviewList
        }
    },
    methods: {
      goToReviewDetail(review) {
        this.$router.push({ name: 'ReviewDetail', params: { id:review.id, review:review }})
      }
      
    },
    mounted() {
      this.movieId = this.$route.params.id
      console.log(this.id)
    },
    created() {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/reviewlist/`,
    })
    .then(res => {
        console.log(res.data)
        this.reviewList.push(res.data)
        // console.log(this.reviewList)
    })
    .catch(err => {
        console.log(err)
    })
    }
    // mounted() {
    //     // 로컬 스토리지에서 리뷰 불러오기
    //     const storedReviews = localStorage.getItem('reviewList')
    //     if (storedReviews) {
    //         this.reviewList = JSON.parse(storedReviews)
    //     }
    // },
    // methods: {
    //     addReview(event) {
    //         const newPost = {
    //             title: event.title,
    //             content: event.content,
    //             rating: event.rating,
    //             recommendation: event.recommendation,
    //         }
    //         this.reviewList.push(newPost)
    //         console.log(this.reviewList)

    //         // 로컬 스토리지에 데이터 저장
    //         localStorage.setItem('reviewList', JSON.stringify(this.reviewList))

    //         // 컴포넌트 데이터 업데이트 후 로컬 스토리지에서 다시 불러오기
    //         const storedReviews = localStorage.getItem('reviewList')
    //         if (storedReviews) {
    //             this.reviewList = JSON.parse(storedReviews)
    //         }
    //     }
    // },
}
</script>

<style>

</style>