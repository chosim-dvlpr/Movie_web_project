<template>
    <div class="wrapped">
        <div class="gallery">
            <div v-for="movie in movieList" :key="movie.id" class="content_box">
                <div @click="gotoMovieDetail(movie)" class="movie_box">
                    <div class="img_box">
                        <img class="img_box_img" :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`"><br>
                    </div>
                    <div class="content_box_detail">
                        <p class="movie_title">{{ movie.title }}</p>
                        <!-- <p class="movie_overview">{{ movie.overview }}</p> -->
                    </div>
                </div>
            </div>
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
        }
    },
    methods: {
        showMovies: function() {
            axios({
                method: 'get',
                url: `${API_URL}/api/movies/`, // back server urls.py와 맞추기
                // headers: this.setToken()
            })
            .then(res => {
                this.movieList = res.data
                // console.log(this.movieList)
                // localStorage.clear('movieList')
                localStorage.setItem('movieList', JSON.stringify(this.movieList))
                // this.test = localStorage.getItem('movieList')
                // console.log(this.test+'_')
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

<style scoped>
* {
    background-color: black;
}
.wrapped {
    margin: 5px;
}

button {
    background-color: white;
    border: 1px solid #dbbf0f;
    border-radius: 10px;
    margin: 5px;
}


.gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-column-end: 0px;
}

.content_box {
    background-color: rgb(0, 0, 0);
    width: 500px;
    display: flex;
}

.movie_title {
    color: #dbbf0f;
    font-weight: bold;
    font-size: 20px;
    margin: 3px;
}

.movie_overview {
    width: 300px;
    margin: auto;
    color: beige;
    background-color: rgba(128, 128, 128, 0.096);
    text-align: center;
}

.img_box {
    margin-left: 20px;
}

.img_box_img {
    object-fit: cover;
    width: 350px;
    margin-top: 50px;
    margin-left: 20px;
    margin-right: 20px;
    transition-delay: 0.1s;
    transition-duration: 1s;
}

.img_box_img:hover {
    width: 370px;
}

.content_box_detail {
    display: flex;
    position: relative;
    flex-direction: column;
    align-items: center;
}

.movie_box {
    display: flex;
    flex-direction: column;
}

</style>