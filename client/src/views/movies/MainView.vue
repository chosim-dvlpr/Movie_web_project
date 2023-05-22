<template>
    <div>
        <div v-for="movie in movieList" :key="movie.id">
            <span @click="gotoMovieDetail(movie)">
                <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.backdrop_path}`"><br>
                <p>title : {{ movie.title }}</p>
                <p>overview : {{ movie.overview }}</p>
            </span>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
// import { mapState } from 'vuex'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MainView',
    data: function () {
        return {
            movieList: [],
            test: '',
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
                this.movieList = res.data
                console.log(this.movieList)
                // localStorage.clear('movieList')
                localStorage.setItem('movieList', JSON.stringify(this.movieList))
                this.test = localStorage.getItem('movieList')
                console.log(this.test+'_')
            })
            .catch(err => {
                console.log(err)
            })  
        },
        // 클릭 시 Movie 상세페이지로 이동
        gotoMovieDetail(movie) {
            // console.log(movie)
            this.$router.push({ name: 'MovieDetail', params: { id: movie.id, movie: movie }})
            localStorage.setItem('moviedetail', JSON.stringify(movie))
        },

        // 토큰
        setToken: function() {
            const token = localStorage.getItem('jwt')
            const config = {
                Authorization: `Bearer ${token}`
            }
            // console.log(config)
            return config
        },
    },
    created() {
        this.showMovies()
    },
    // computed: {
    //     ...mapState({
    //         movieList: state => state.movieList
    //     })
    // }
}
</script>

<style>

</style>