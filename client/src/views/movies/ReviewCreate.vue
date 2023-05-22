<template>
  <div>
    <h2>리뷰 작성</h2>
    <h3>여기는 ReviewCreate 페이지</h3>
    <p>movie id : {{ this.movieId }}</p>
    <form @submit.prevent="reviewCreate">
    <!-- <form> -->
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
    <hr>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ReviewCreate',
    data() {
        return {
            // post: {
            //     title: '',
            //     content: '',
            //     rating: null,
            //     recommendation: false
            // },
            title: null,
            content: null,
            rating: null,
            recommendation: null,

            reviewList: [],
            movieId: null,
        }
    },
    methods: {
        // submitReview() {
        //   const newPost = {
        //     title: this.title,
        //     content: this.content,
        //     rating: this.rating,
        //     recommendation: this.recommendation
        //   }

        //   console.log(this.$route.params.movieId)
        //   this.reviewList.push(newPost)
        //   this.$emit('submit-review', this.reviewList)
        //   this.$router.push({ name: 'ReviewList', params: { id: this.movieId } })
        // },

        // django 연결
        reviewCreate() {
            const reviewItem = {
                title: this.title,
                content: this.content,
                rating: this.rating,
                recommendation: `${this.recommendation}`
            }
            console.log('_'+reviewItem)
            // reviewItem에 값이 들어간다면 (입력된다면) axios 실행
            if (reviewItem.title) {
                console.log('axios 실행')
                // this.newPost.push(reviewItem)
                // console.log(this.newPost)
                axios({
                    method: 'post',
                    url: `${API_URL}/api/movies/${this.movieId}/reviewcreate/`,
                    data: reviewItem,
                })
                .then(res => {
                    console.log(res)
                    this.$emit('submit-review', this.reviewItem)
                    this.$router.push({ name: 'ReviewList', params: { id: this.movieId } })
                })
                .catch(err => {
                    console.log(err)
                })
            } else {
                alert('내용을 입력해주세요.')
            }
        }
    },

    // 데이터 받기
    mounted() {
      this.movieId = this.$route.params.id
    }
}
</script>

<style>

</style> 