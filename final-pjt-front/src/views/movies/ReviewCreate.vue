<template>
  <div class="review_create">
    <div class="input_box">
    <div style="align-items:center; margin:auto;">
    <h2>리뷰 작성</h2>
    </div>
    <form @submit.prevent="reviewCreate">
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
      <button type="submit">작성 완료</button>
    </form>
    </div>
    <br>
    <button @click="goToMovieDetail">뒤로가기</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ReviewCreate',
    data() {
        return {
            title: null,
            content: null,
            rating: null,
            recommendation: null,

            reviewList: [],
            movieId: JSON.parse(sessionStorage.getItem("moviedetail")).id,
            user: sessionStorage.getItem("username")
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
      // 리뷰 작성
      reviewCreate() {
        // console.log(this.user)
          const reviewItem = {
              movie_id: this.movieId,
              id: this.reviewId,
              title: this.title,
              content: this.content,
              rating: this.rating,
              recommendation: `${this.recommendation}`,
              user_id: this.user,
          }
          // console.log('_'+reviewItem)
          // reviewItem에 값이 들어간다면 (입력된다면) axios 실행
          if (reviewItem.title) {
              // console.log('axios 실행')
              // this.newPost.push(reviewItem)
              // console.log(this.newPost)
              axios({
                  method: 'post',
                  url: `${API_URL}/api/movies/${this.movieId}/reviewcreate/`,
                  data: reviewItem,
                  headers: this.setToken()
              })
              .then(res => {
                  this.movieId = res.data.movie.id
                  this.$router.push({ name: 'ReviewList', params: { id: this.movieId } })
              })
              .catch(err => {
                  console.log(err)
              })
          } else {
              alert('내용을 입력해주세요.')
          }
      },
      // 영화 리스트로 돌아가기
      goToMovieDetail() {
        this.$router.push({ name: 'MovieDetail', params: { id: this.movieId, movieId: this.movieId }})
      },
    },

    // 데이터 받기
    created() {
      // this.movieId = this.$route.params.id
    }
}
</script>

<style>
.review_create {
  position: relative;
  top: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input_box {
  display: flex;
  align-items: flex-end;
  flex-direction: column;
  margin: 5px;
}

.input_box > form {
  margin: 3px;
}

form > div {
  margin: 3px;
  display:flex;
  align-items:center;
}
</style> 