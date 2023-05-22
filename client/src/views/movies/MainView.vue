<template>
  <div>
    <div v-for="movie in movieList" :key="movie.id">
        <span @click="gotoMovieDetail(movie)">
            <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.backdrop_path}`"><br>
            <p>{{movie.backdrop_path}}</p>
            <p>title : {{ movie.title }}</p>
            <p>overview : {{ movie.overview }}</p>
        </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MainView',
    data: function () {
        return {
            movieList: [],
        }
    },
    methods: {
        showMovies: function() {
            axios({
                method: 'get',
                // url: `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko&page=1&sort_by=popularity.desc&api_key=${this.api_key}`
                url: `${API_URL}/api/movies/`, // back server urls.py와 맞추기
                // headers: this.setToken()
            })
            .then(res => {
                console.log(res.data)
                this.movieList = res.data
            })
            .catch(err => {
                console.log(err)
            })  
        },
        // 클릭 시 Movie 상세페이지로 이동
        gotoMovieDetail(movie) {
            this.$router.push({ name: 'MovieDetail', params: { id: movie.id, movie: movie }})
        },

        // 토큰
        setToken: function() {
            const token = localStorage.getItem('jwt')
            const config = {
                Authorization: `Bearer ${token}`
            }
            console.log(config)
            return config
        },
    },
    created() {
        this.showMovies()
    },
}
</script>

<style>

</style>