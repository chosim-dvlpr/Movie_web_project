<template>
  <div>
    <div v-for="movie in movieList" :key="movie.id" @click="gotoMovieDetail(movie)">
        <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2/${movie.poster_path}`">
        {{ movie.title }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import api_key from '../../../data'

export default {
    name: 'MainView',
    data: function () {
        return {
            api_key: api_key.API_KEY,
            movieList: [],
        }
    },
    methods: {
        showMovies: function() {
            axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko&page=1&sort_by=popularity.desc&api_key=${this.api_key}`
            })
            .then(res => {
                this.movieList = res.data.results
            })
            .catch(err => {
                console.log(err)
            })  
        },
        // 클릭 시 Movie 상세페이지로 이동
        gotoMovieDetail(movie) {
            this.$router.push({ name: 'MovieDetail', params: { movie: movie }})
        }
    },
    mounted() {
        this.showMovies()
    },
}
</script>

<style>

</style>