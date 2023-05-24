<template>
  <div>
    <h1>여기는 Movie Detail View</h1>
    <h2>영화 디테일을 볼 수 있는 페이지</h2>
    <div>
      <div class="content_box">
        <div class="img_box">
          <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movieDetail.poster_path}`">
        </div>
        <div class="detail_box">
          <p>Title : {{ movieDetail.title }}</p>
          <p>개요 : {{ movieDetail.overview }}</p>
          <p>개봉일 : {{ movieDetail.release_date }}</p>
          <hr>
        </div>
      </div>
    </div>
    <div>
      <div v-if="this.isLike">
        <button @click="likeMovie">좋아요</button>
      </div>
      <div v-else>
        <button @click="likeMovie">좋아요 취소</button>
      </div>
    </div>
    <div>
      <h2>Review</h2>
      <!-- <p>movieId : {{ movieDetail.id }}</p> -->
      <!-- 리뷰 모아보기를 버튼 말고 화면에 띄우도록 수정하기 -->
      <button @click="goToReviewList">리뷰 보기</button>
      <button @click="goToReviewCreate">리뷰 작성</button>
    </div>

    <div>
      <button @click="backToMain">뒤로가기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieDetail',
    data() {
      return {
        movieDetail: JSON.parse(localStorage.getItem("moviedetail")), // localStorage에 저장
        isLike: false,
      }
    },
    methods: {
      backToMain() {
        this.$router.push({ name: 'MainView' })
      },
      goToReviewCreate() {
        this.$router.push({ name: 'ReviewCreate', params: { id: this.movieDetail.id }})
        // console.log(this.movieDetail.id)
      },
      goToReviewList () {
        this.$router.push({ name: 'ReviewList', params: { id: this.movieDetail.id }})
      },
      setToken: function() {
        const token = localStorage.getItem('jwt')
        const config = {
            Authorization: `Bearer ${token}`
        }
        return config
      },
      likeMovie() {
        axios({
            method: 'post',
            url: `${API_URL}/api/movies/${this.movieDetail.id}/like/`,
            data: this.movieDetail.id,
            headers: this.setToken()
        })
        .then(res => {
            this.isLike = res.data.isLike
        })
        .catch(err => {
            console.log(err)
        })  
      }
    },
    created() {
      // this.movieDetail = this.$route.params.movie.Detail
      // this.movieDetail = localStorage.getItem('movie')
      // console.log(this.movieDetail)
      // this.moviePoster = this.$route.params.movie.backdrop_path
      // this.movieOverview = this.$route.params.movie.overview
      // this.movieReleaseDate = this.$route.params.movie.release_date
      // this.movieId = this.$route.params.movie.id
    }
    
}
</script>

<style>
.content_box {
  }

.img_box {
  float: left;
}

img {
  width: 400px;

}

.detail_box {
  display: flex;
  flex-direction: column;
}
</style>