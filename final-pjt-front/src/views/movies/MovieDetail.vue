<template>
  <div class="root">
    <div>
      <div class="content_box">
        <div class="background-img-box"><img class="background-img" :src="`https://www.themoviedb.org/t/p/original${movieDetail.backdrop_path}`"></div>
        <div class="top_content">
          <div class="detail_box">
            <p id="movie_title">{{ movieDetail.title }}</p>
            <p id="movie_overview">{{ movieDetail.overview }}</p>
            <p>개봉일 : {{ movieDetail.release_date }}</p>
            <div v-if="!this.isLike">
              <span class="if-you-like-movie-box"><p class="if-you-like-movie" >이 영화가 마음에 든다면? </p><i @click="likeMovie" class="far fa-heart fa-lg" style="color: #ff0000;"></i></span>
            </div>
            <div v-else>
              <span class="if-you-like-movie-box"><p class="if-you-like-movie" >이 영화가 마음에 든다면? </p><i @click="likeMovie" class="fas fa-heart fa-lg" style="color: #ff0000;"></i></span>
            </div>
            <!-- <div class="video_box">
              <iframe :src="`https://youtube.com/embed/${this.video}`" width="600px" height="450px" frameborder="0"></iframe>
            </div> -->
          </div>
          <div class="title_box">
            <div class="title_box_detail">
              <img src="@/assets/사다리.png" class="ladder-img">
              <div style="display:flex; justify-content:center; align-items:center; flex-direction:column; margin:auto;">
                <p style="font-size:40px; padding-top:45px; position:relative; right:10px;">{{ movieDetail.original_title }}</p>
                <p style="font-size:25px; padding-bottom:45px; position:relative; right:10px;">VOTE : {{ movieDetail.vote_average}}</p>
              </div>
            </div>
          </div>
        </div>


        <!-- <div class="request_movie_box">
          <p>추천 영화</p>
          <div class="request_movie">
            <div class="request_movie_item" v-for="(requestMovie, index) in requestMovieList" :key="index">
                <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${requestMovie.poster_path}`">
                <p>{{ requestMovie.title }}</p><br>
            </div>
          </div>
        </div> -->


      </div>
      <!-- 스와이프 기능 넣어보기 -->
      <div class="card" style="margin-top:15rem; left: 3rem; width: 10rem; flex-direction:row; display:flex; position:absolute; background-color:transparent;">
        <div class="card-img-top" style="margin:10px; background-color:rgba(71, 71, 71, 0.356); height:340px; box-shadow:1px 1px 5px black; box-radius:5px;" v-for="(requestMovie, index) in requestMovieList" :key="index">
          <img style="width:10rem;" :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${requestMovie.poster_path}`">
          <div class="card-body">
            <h5 class="card-title" style="color:white; margin-top:13px;">{{ requestMovie.title }}</h5>
          </div>
        </div>
      </div>
    </div>

    <div class="review-button">
      <button @click="goToReviewList">리뷰 보기</button>
      <button @click="goToReviewCreate">리뷰 작성</button>
      <button class="back-to-main" @click="backToMain">뒤로가기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import youtube_api_key from '../../youtube_data'
// import RequestMovie from '@/components/RequestMovie.vue'
import api_key from '../../data'

const API_URL = 'http://127.0.0.1:8000'
const Y_API_KEY = youtube_api_key
const API_KEY = api_key.API_KEY



export default {
    name: 'MovieDetail',
    // component: {
    //   RequestMovie,
    // },
    data() {
      return {
        movieDetail: JSON.parse(sessionStorage.getItem("moviedetail")),
        isLike: false,
        videoKeyList: ['a8Gx8wiNbs8', '0-wPm99PF9U'],
        videoKey: '',
        video: '',

        movieId: JSON.parse(sessionStorage.getItem('moviedetail')).id,
        requestMovieList: [],
      }
    },
    methods: {
      backToMain() {
        this.$router.push({ name: 'MainView' })
      },
      goToReviewCreate() {
        this.$router.push({ name: 'ReviewCreate', params: { id: this.movieDetail.id }})
        // console.log(this.movieDetail.id)
      },
      goToReviewList () {
        this.$router.push({ name: 'ReviewList', params: { id: this.movieDetail.id }})
      },
      setToken: function() {
        const token = sessionStorage.getItem('jwt')
        const config = {
            Authorization: `Bearer ${token}`
        }
        return config
      },
      likeMovie() {
        axios({
            method: 'post',
            url: `${API_URL}/api/movies/${this.movieDetail.id}/like/`,
            data: this.movieDetail.id,
            headers: this.setToken()
        })
        .then(res => {
            this.isLike = res.data.isLike
        })
        .catch(err => {
            console.log(err)
        })  
      },
      // 유튜브 video
      getVideo() {
          const url = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${this.videoKeyList[0]}&key=${Y_API_KEY}`
          axios.get(url)
          .then(response => {
              this.video = response.data.items[0].id
          })
          .catch(error => {
              console.error(error)
          })
      },

      // 추천 영화
      showRequestMovies() {
            axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/movie/${this.movieId}/similar?language=ko&page=1&api_key=${API_KEY}`,
            })
            .then(res => {
                this.requestMovieList.push(res.data.results[0])
                this.requestMovieList.push(res.data.results[1])
                this.requestMovieList.push(res.data.results[2])
                this.requestMovieList.push(res.data.results[3])
                this.requestMovieList.push(res.data.results[4])
            })
            .catch(err => {
                console.log(err)
            })  
        },
    },
    created() {
      this.getVideo()
      this.showRequestMovies()
    }
}
</script>

<style scoped>
/* @import 'material-icons/iconfont/material-icons.css'; */
button {
  background-color: beige;
}

button:hover {
  transition-duration: 0.1s;
  background-color: #FFD700;
}

.root {
  background-repeat : no-repeat;
  background-position: top;
  object-fit: cover;
  background-size : cover;
  color: rgb(129, 129, 129);
}

/* #movieDetail {
  background-image: url('');
} */

.background-img-box {
  /* background-repeat : no-repeat; */
  /* background-position: top; */
  object-fit: cover;
  /* display: flex; */
  position: absolute;
  filter: brightness(50%); 
  top: 150px;
  left: 0;
  width: 100%;
}

.background-img {
  object-fit: cover;
  width: 100%;
}

.top_content {
  display: flex;
  position: relative;
  width: 100%;
  top: 160px;
  align-items: center;
}

.content_box {
  display: flex;
  justify-content: space-around;
  }

.img_box {
  float: left;
  margin: 40px;
  background-color: transparent;
}

.ladder-img {
  border-radius: 20px;
  width:15%; 
  height:270px; 
  border-radius:0; 
  display:flex; 
  margin-left:30px;
}

.detail_box {
  display: flex;
  flex-direction: column;
  position: relative;
  left: 0;
  padding: 30px;
  /* padding-left: 380px; */
  width: 60%;
  /* height: 1000px; */
  /* transform: skew(-20deg); */
  background: rgba(71, 71, 71, 0.356);
  box-shadow: 1px 1px 40px black;
  /* top: 160px; */
}

.material-symbols-rounded {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}


#movie_title {
  font-size: 60px;
  color: #FFD700;
  font-weight: bold;
}

#movie_overview {
  padding: 50px;
  padding-left: 150px;
  font-size: 17px;
}

.request_movie_box {
  background-color: rgba(71, 71, 71, 0.24);
  border: 1px solid black;
  box-shadow: 1px 1px 1px black;
  width: 800px;
  display: flex;
  position: absolute;
  top: 770px;
  left: 50px;
  flex-direction: column;
}

.request_movie {
  display: flex;
  margin: 5px;
}

.request_movie_item {
  margin: 10px;
}

.request_movie_item > img {
  width: 120px;
}

.video_box {
  padding: 50px;
}

/* .content_box.video_box {
  position: absolute;
  top: 90px;
} */

.title_box_detail {
  background-color: #FFD700;
  width: 450px;
  height: 270px;
  position: relative;
  /* top: 600px; */
  /* right: 170px; */
  left: 50%;
  border-radius: 3px;
  display: flex;
  box-shadow: 10px 10px 50px black;
  color:black; 
  font-weight:bold;
}

.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}

.back-to-main {
  position: relative;
  margin-top: 5px;
}

.review-button {
  width:10rem; 
  position:absolute; 
  left:10rem;
}

.if-you-like-movie-box {
  display: flex;
  justify-content: center;
}

.if-you-like-movie {
  background-color: rgba(128, 128, 128, 0.592);
  color: black;
  margin-right: 10px;
}
</style>