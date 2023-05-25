<template>
  <div>
    <p>movieId : {{this.movieId}}</p>
    <!-- <p>{{this.requestMovieList}}</p> -->
    <div v-for="(requestMovie, index) in requestMovieList" :key="index">
        <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${requestMovie.poster_path}`">
        <br>
        <p>{{ requestMovie.title }}</p><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import api_key from '../../data'

// const API_URL = 'http://127.0.0.1:8000'
const API_KEY = api_key.API_KEY

export default {
    name: 'RequestMovie',
    data() {
        return {
            movieId: JSON.parse(localStorage.getItem('moviedetail')).id,
            requestMovieList: [],
        }
    },
    methods: {
        showRequestMovies() {
            axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/movie/${this.movieId}/similar?language=ko&page=1&api_key=${API_KEY}`,
                // data: this.movieId,
                // headers: this.setToken()
            })
            .then(res => {
                this.requestMovieList = res.data.results
                // console.log(this.requestMovieList.results)
            })
            .catch(err => {
                console.log(err)
            })  
        },
        setToken: function() {
            const token = localStorage.getItem('jwt')
            const config = {
                Authorization: `Bearer ${token}`
            }
            return config
        },
    },
    created() {
        this.showRequestMovies()
    }
}
</script>

<style>

</style>