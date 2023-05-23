<template>
  <div>
    <h1>리뷰 수정 페이지</h1>
    <!-- <p @modify-review="reviewModify"></p> -->
    <!-- <p>리뷰 : {{ this.review }}</p> -->
    <form @submit.prevent="reviewModify">
      <div>
        <label for="title">제목:</label>
        <input type="text" id="title" v-model="title" required>
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea id="content" v-model="content" required></textarea>
      </div>
      <div>
        <label for="rating">평점:</label>
        <input type="number" id="rating" v-model="rating" min="0" max="5" required>
      </div>
      <div>
        <input type="checkbox" id="recommendation" v-model="recommendation">
        <label for="recommendation">이 영화를 추천합니다</label>
      </div>
      <!-- <button type="submit" @click="reviewCreate">작성 완료</button> -->
      <button type="submit">작성 완료</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewModify',
  data() {
        return {
            review: null,
            title: null,
            content: null,
            rating: null,
            recommendation: null,
            movieId: null,
            reviewId: null,
        }
    },
  methods: {
    reviewModify() {
      // this.review = this.$route.params.newReview
      const modifiedReview = {
        title: this.title,
        content: this.content,
        rating: this.rating,
        recommendation: this.recommendation,
        movieId: this.movieId,
        reviewId: this.reviewId,
      }
      console.log('_'+this.reviewId)

      axios({
        method: 'put',
        url: `${API_URL}/api/movies/${this.reviewId}/reviewdetail/`,
        data: modifiedReview,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        // this.$emit('submit-review', this.reviewItem)
        this.$router.push({ name: 'ReviewList', params: { id: this.movieId } })
        localStorage.removeItem('reviewdetail')
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  created() {
    // console.log(this.$router.params.review)
    // this.review = this.$router.params.review
    this.review = this.$route.params.review
    this.title = this.review.title
    this.content = this.review.content
    this.rating = this.review.rating
    this.recommendation = this.review.recommendation
    this.reviewId = this.$route.params.review.reviewId
    console.log(this.review)
  }
}
</script>

<style>

</style>