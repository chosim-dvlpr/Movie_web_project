<template>
    <div class="wrapped">
        <!-- <div class="video_box"> -->
          <!-- 배경 video : 랜덤 영상 재생 -->
          <!-- <iframe :src="videoSource" width="1980px" height="2000px" frameborder="0"></iframe> -->
          <!-- <iframe width="1000px" height="2000px" src="https://www.youtube.com/embed/a8Gx8wiNbs8?controls=0&autoplay=1&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;" allowfullscreen></iframe> -->
        <!-- </div> -->
        <div class="carousel_box">
            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                    <img src="https://www.themoviedb.org/t/p/w300_and_h450_bestv2/kHen25Yk0DnaB2pqaB1mcZDKqMv.jpg" class="d-block w-100" alt="..." style="width:100px;">
                    </div>
                    <div class="carousel-item">
                    <img src="https://www.themoviedb.org/t/p/w300_and_h450_bestv2/wXNihLltMCGR7XepN39syIlCt5X.jpg" class="d-block w-100" alt="...">
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>
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
* {
    background-color: black;
}

.carousel_box {
    width: 500px;
}
/* .wrapped {
    position: absolute;
    margin: 5px;
    width: 100%;
} */

button {
    background-color: white;
    border: 1px solid #dbbf0f;
    border-radius: 10px;
    margin: 5px;
}


.gallery {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    /* grid-template-columns: repeat(3, 1fr);
    grid-column-end: 0px; */
}

.content_box {
    background-color: rgb(0, 0, 0);
    width: 500px;
    /* display: flex; */
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