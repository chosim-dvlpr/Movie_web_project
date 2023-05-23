<template>
  <div>
    <h1>여기는 Movie Detail View</h1>
    <h2>영화 디테일을 볼 수 있는 페이지</h2>
    <div>
      <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movieDetail.backdrop_path}`">
      <p>Title : {{ movieDetail.title }}</p>
      <p>개요 : {{ movieDetail.overview }}</p>
      <p>개봉일 : {{ movieDetail.release_date }}</p>
      <hr>
    </div>
    <!-- <p @click="likeMovie">좋아요</p> -->

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

export default {
    name: 'MovieDetail',
    data() {
      return {
        movieDetail: JSON.parse(localStorage.getItem("moviedetail")), // localStorage에 저장
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

</style>