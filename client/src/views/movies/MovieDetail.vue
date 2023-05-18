<template>
  <div>
    <h1>여기는 Movie Detail View</h1>
    <h2>영화 디테일을 볼 수 있는 페이지</h2>
    <div>
      <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2/${moviePoster}`">
      <p>Title : {{ movieTitle }}</p>
      <p>개요 : {{ movieOverview }}</p>
      <p>개봉일 : {{ movieReleaseDate }}</p>
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
        movieTitle: null,
        movieImage: null,
        movieOverview: null,
        movieReleaseDate: null,
      }
    },
    methods: {
      backToMain() {
        this.$router.push({ name: 'MainView' })
      }
    },
    mounted() {
      this.movieTitle = this.$route.params.movie.title
      this.moviePoster = this.$route.params.movie.poster_path
      this.movieOverview = this.$route.params.movie.overview
      this.movieReleaseDate = this.$route.params.movie.release_date
    }
    
}
</script>

<style>

</style>