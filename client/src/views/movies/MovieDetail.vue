<template>
  <div>
    <h1>여기는 Movie Detail View</h1>
    <h2>영화 디테일을 볼 수 있는 페이지</h2>
    <div>
      <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${moviePoster}`">
      <p>Title : {{ movieTitle.title }}</p>
      <p>개요 : {{ movieOverview }}</p>
      <p>개봉일 : {{ movieReleaseDate }}</p>
      <hr>
    </div>

    <div>
      <h3>리뷰 모아보기</h3>
      <p>movieId : {{ this.movieId }}</p>
      <!-- 리뷰 모아보기를 버튼 말고 화면에 띄우도록 수정하기 -->
      <button @click="goToReviewList">리뷰 보기</button>
      <button @click="goToReviewCreate">리뷰작성</button>
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
        // movie: null,
        // movieTitle: null,
        movieTitle: JSON.parse(localStorage.getItem("moviedetail")) || "",
        moviePoster: null,
        movieOverview: null,
        movieReleaseDate: null,
        movieId: null,
      }
    },
    methods: {
      backToMain() {
        this.$router.push({ name: 'MainView' })
      },
      goToReviewCreate() {
        this.$router.push({ name: 'ReviewCreate', params: { id: this.movieId }})
      },
      goToReviewList () {
        this.$router.push({ name: 'ReviewList', params: { id: this.movieId }})
      }
    },
    created() {
      // this.movieTitle = this.$route.params.movie.title
      // this.movieTitle = localStorage.getItem('movie')
      console.log(this.movieTitle)
      this.moviePoster = this.$route.params.movie.backdrop_path
      this.movieOverview = this.$route.params.movie.overview
      this.movieReleaseDate = this.$route.params.movie.release_date
      this.movieId = this.$route.params.movie.id
    }
    
}
</script>

<style>

</style>