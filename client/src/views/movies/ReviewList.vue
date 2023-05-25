<template>
  <div class="review">
    <h1>ReviewList</h1>
    <br>
    <span v-for="(review, index) in reviewList[0]" :key="index">
      <span v-if="checkMovieId(index)">
        <span @click="goToReviewDetail(review)">
            <!-- <p>review id : {{ review.id }}</p>
            <p>movie id : {{ review.movie }}</p> -->
            <p>리뷰 제목 : {{ review.title }}</p>
            <p>내용 : {{ review.content }}</p>
            <p>평점 : {{ review.rating }}</p>
            <p>이 영화를 추천합니다 : </p>
            <p v-if="review.recommendation">
              <i class="fas fa-star fa-lg" style="color: #ffd700;"></i>
            </p>
            <p v-if="review.recommendation===null"><i class="far fa-star fa-lg" style="color: #ffd700;"></i></p>
            
            <hr>
          </span>
      </span>
    </span>
    <p v-if="!this.checkMovieIdCount">리뷰가 없어요</p>
    <button @click="goToMovieDetail">뒤로가기</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ReviewList',
    data() {
        return {
          reviewList: [],
          movieDetail: JSON.parse(localStorage.getItem('moviedetail')),
          checkMovieIdCount: false,
          // reviewList: localStorage.getItem('reviewList'),
          // reviewList: this.$route.params.reviewList
        }
    },
    methods: {
      goToReviewDetail(review) {
        // console.log(review.id)
        this.$router.push({ name: 'ReviewDetail', params: { id: review.id, review: review }})
        localStorage.setItem('reviewdetail', JSON.stringify(review))
      },
      goToMovieDetail(movieId) {
        this.$router.push({ name: 'MovieDetail', params: { id: movieId, movieId: movieId }})
        // this.$router.push({ name: 'MovieDetail', params: { id: movieId }})
      },
      
      checkMovieId(index) {
        // console.log(index)
        // console.log((this.reviewList)[0][index].movie)
        // console.log(this.movieDetail)
        if ((this.reviewList)[0][index].movie === (this.movieDetail.id)) {
          this.checkMovieIdCount = true
          return true
        }
      },
      checkMovieIdCountDef() {
        this.checkMovieIdCount ++
      }
    },
    mounted() {
      this.movieId = this.$route.params.id
      // console.log(this.id)
    },
    getters: {
    },
    created() {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/reviewlist/`,
      })
      .then(res => {
          // console.log('+'+res)
          this.reviewList.push(res.data)
          localStorage.setItem('reviewList', JSON.stringify(this.reviewList[0]))
      })
      .catch(err => {
          console.log(err)
      })
    }
    // mounted() {
    //     // 로컬 스토리지에서 리뷰 불러오기
    //     const storedReviews = localStorage.getItem('reviewList')
    //     if (storedReviews) {
    //         this.reviewList = JSON.parse(storedReviews)
    //     }
    // },
    // methods: {
    //     addReview(event) {
    //         const newPost = {
    //             title: event.title,
    //             content: event.content,
    //             rating: event.rating,
    //             recommendation: event.recommendation,
    //         }
    //         this.reviewList.push(newPost)
    //         console.log(this.reviewList)

    //         // 로컬 스토리지에 데이터 저장
    //         localStorage.setItem('reviewList', JSON.stringify(this.reviewList))

    //         // 컴포넌트 데이터 업데이트 후 로컬 스토리지에서 다시 불러오기
    //         const storedReviews = localStorage.getItem('reviewList')
    //         if (storedReviews) {
    //             this.reviewList = JSON.parse(storedReviews)
    //         }
    //     }
    // },
}
</script>

<style>
.review {
  position: relative;
  top: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

button {
  background-color: beige;
}

button:hover {
  transition-duration: 0.1s;
  background-color: #FFD700;
}
</style>