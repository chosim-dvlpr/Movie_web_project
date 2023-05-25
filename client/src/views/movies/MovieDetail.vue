<template>
  <div class="root">
    <div>
      <div class="content_box">
        <p class="background_img"><img :src="`https://www.themoviedb.org/t/p/original${movieDetail.backdrop_path}`" style="width: 3000px;"></p>
        <div class="top_content">
          <div class="img_box">
            <img :src="`https://www.themoviedb.org/t/p/original${movieDetail.poster_path}`">
          </div>
          <div class="detail_box">
            <p id="movie_title">{{ movieDetail.title }}</p>
            <p id="movie_overview">{{ movieDetail.overview }}</p>
            <p>Release Date : {{ movieDetail.release_date }}</p>
            <router-link :to="{ name: 'RequestMovie' }" class="request_movie">RequestMovie</router-link>

            <div v-if="!this.isLike">
              <button @click="likeMovie">좋아요</button>
            </div>
            <div v-else>
              <button @click="likeMovie">좋아요 취소</button>
            </div>
            <div class="video_box">
              <iframe :src="`https://youtube.com/embed/${this.video}`" width="600px" height="450px" frameborder="0"></iframe>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
      
    </div>



    <div class="review_box">
      <h2>Review</h2>
      <!-- <p>movieId : {{ movieDetail.id }}</p> -->
      <!-- 리뷰 모아보기를 버튼 말고 화면에 띄우도록 수정하기 -->
      <button @click="goToReviewList">리뷰 보기</button>
      <button @click="goToReviewCreate">리뷰 작성</button>
    </div>

    <div>
      <button @click="backToMain">뒤로가기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import youtube_api_key from '../../youtube_data'

const API_URL = 'http://127.0.0.1:8000'
const API_KEY = youtube_api_key



export default {
    name: 'MovieDetail',
    data() {
      return {
        movieDetail: JSON.parse(localStorage.getItem("moviedetail")),
        isLike: false,
        videoKeyList: ['a8Gx8wiNbs8', '0-wPm99PF9U'],
        videoKey: '',
        video: '',
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
        const token = localStorage.getItem('jwt')
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
          const url = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${this.videoKeyList[0]}&key=${API_KEY}`
          axios.get(url)
          .then(response => {
              console.log(response)
              this.video = response.data.items[0].id
          })
          .catch(error => {
              console.error(error)
          })
      },
    },
    created() {
      this.getVideo()
    }
    
}
</script>

<style scoped>
/* @import 'material-icons/iconfont/material-icons.css'; */

.root {
  background-repeat : no-repeat;
  background-position: top;
  object-fit: cover;
  /* position: fixed; */
  background-size : cover;
}

/* #movieDetail {
  background-image: url('');
} */

.background_img {
  /* background-repeat : no-repeat; */
  /* background-position: top; */
  /* object-fit: cover; */
  display: flex;
  position: fixed;
  filter: brightness(70%); 
  z-index: 0;
}

.top_content {
  display: flex;
  position: relative;
}

.content_box {
  display: flex;
  /* background-color: bisque; */
  justify-content: space-around;
  }

.img_box {
  float: left;
  margin: 40px;
  background-color: tomato;
  background-image: url('https://www.themoviedb.org/t/p/w300_and_h450_bestv2/8k8tmcx5e6ShpackLnDswBo1tnB.jpg')
}

img {
  width: 600px;

}

.detail_box {
  display: flex;
  flex-direction: column;
  margin: 40px;
  background-color: aquamarine;
  /* width: 40rem; */
  height: calc(600px - 80px);
  padding: 50px;
}

.material-symbols-rounded {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 48
}

.request_movie {
  color: yellow;
}

#movie_title {
  font-size: 30px;
}

.review_box {
  background-color: pink;
}

/* .content_box.video_box {
  position: absolute;
  top: 90px;
} */
</style>