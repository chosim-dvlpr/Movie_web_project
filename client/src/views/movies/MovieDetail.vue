<template>
  <div>
    <h1>여기는 Movie Detail View</h1>
    <h2>영화 디테일을 볼 수 있는 페이지</h2>
    <p>{{ movieTitle }}</p>
  </div>
</template>

<script>
export default {
    name: 'MovieDetail',
    data() {
      return {
        movieTitle: null,
      }
    },
    mounted() {
      this.movieTitle = this.$route.params.movie.title
    }
    
}
</script>

<style>

</style>