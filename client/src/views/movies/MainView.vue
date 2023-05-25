<template>
    <div class="wrapped">
        <!-- <div class="video_box"> -->
          <!-- 배경 video : 랜덤 영상 재생 -->
          <!-- <iframe :src="videoSource" width="1980px" height="2000px" frameborder="0"></iframe> -->
          <!-- <iframe width="1000px" height="2000px" src="https://www.youtube.com/embed/a8Gx8wiNbs8?controls=0&autoplay=1&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;" allowfullscreen></iframe> -->
        <!-- </div> -->
        <!-- <div class="carousel_box" style="width:100%;">
            <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="https://www.themoviedb.org/t/p/original/jMTvYnFr89K0RxO9K2sz4poWCCc.jpg" class="d-block" style="width:1920px;">
                    </div>
                    <div class="carousel-item">
                        <img src="https://www.themoviedb.org/t/p/original/1ySuP1UAiVj7QDnQwivJkSZNTxH.jpg" class="d-block" style="width:1920px;">
                    </div>
                    <div class="carousel-item">
                        <img src="https://www.themoviedb.org/t/p/original/u4SDPknBWEEOCzPJvL0NwApkQSR.jpg" class="d-block" style="width:1920px;">
                    </div>
                </div>
            </div>
        </div> -->
        <div class="video_box">
            <iframe width="2000px" height="1500px" src="https://www.youtube.com/embed/d9MyW72ELq0?controls=0&amp;start=1&mute=1&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>



        <div class="gallery">
            <div v-for="movie in movieList" :key="movie.id" class="content_box">
                <div @click="gotoMovieDetail(movie)" class="movie_box">
                    <div class="img_box">
                        <img class="img_box_img" :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`"><br>
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
import youtube_api_key from '../../youtube_data'

const API_URL = 'http://127.0.0.1:8000'
const API_KEY = youtube_api_key

export default {
    name: 'MainView',
    data: function () {
        return {
            movieList: [],
            videoKeyList: ['a8Gx8wiNbs8', '0-wPm99PF9U'],
            videoKey: '',
            video: null,
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

        // 유튜브 video
        getVideo() {
            const url = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${this.videoKeyList[0]}&key=${API_KEY}`
            axios.get(url)
            .then(response => {
                console.log(response)
                this.video = response.data.items[0]
            })
            .catch(error => {
                console.error(error)
            })
        },
        videoSource() {
            return `https://youtube.com/embed/${this.videoKeyList[0]}`
        },
        embedUrl() {
            if (this.video) {
                return `https://www.youtube.com/embed/${this.video.id}`;
            }
            return '';
        }
    },
    created() {
        this.showMovies()
        this.getVideo()
    },
    mounted() {
        
    },
    // computed: {
    //     ...mapState({
    //         movieList: state => state.movieList
    //     })
    // }
    
}
</script>

<style scoped>
.wrapped {
    position: relative;
    top: 200px;
}

nav {
    z-index: 3;
}


.carousel_box {
    position: absolute;
    display: flex;
    filter: brightness(70%); 
    /* background-color: blueviolet; */
}

.video_box {
    position: absolute;
    top: -360px;
    left: -100px;
    display: flex;
    z-index: 0;
    /* justify-content: center; */
}

button {
    background-color: white;
    border: 1px solid #dbbf0f;
    border-radius: 10px;
    margin: 5px;
}


.gallery {
    position: absolute;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    /* grid-template-columns: repeat(3, 1fr);
    grid-column-end: 0px; */
}

.content_box {
    /* background-color: rgb(0, 0, 0); */
    width: 500px;
    /* display: flex; */
}

.movie_title {
    color: #dbbf0f;
    text-shadow: black;
    /* text-decoration-color: black; */
    font-weight: bold;
    font-size: 20px;
    margin: 10px;
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
    transition-duration: 0.7s;
    box-shadow: 10px 10px 30px black;
    border-radius: 5px;
}

.img_box_img:hover {
    width: 370px;
    color: black;
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

/* .video_box {
  object-fit: fill;
  display: flex;
  position: absolute;
  background-color: red;
  flex-direction: column;
} */

/* .video_box {
    position: relative;
    top: 0px;
    left: 0px;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -1;
    overflow: hidden;
    background-color: aqua;
    background-attachment: fixed;
} */
</style>