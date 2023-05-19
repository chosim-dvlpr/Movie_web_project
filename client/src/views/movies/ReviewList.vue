<template>
  <div>
    <h1>여기는 ReviewList</h1>
    <h2>리뷰 리스트 페이지</h2>
    <hr>    
    <p>{{ this.reviewList }}</p>
    <span v-for="(review, index) in reviewList" :key="index">
        <p>리뷰 제목 : {{ review.title }}</p>
        <p>내용 : {{ review.content }}</p>
        <p>평점 : {{ review.rating }}</p>
        <p>이 영화를 추천합니다 : {{ review.recommendation }}</p>
        <hr>
    </span>
  </div>
</template>

<script>
export default {
    name: 'ReviewList',
    data() {
        return {
            reviewList: [],
            // reviewList: this.$route.params.reviewList
        }
    },
    mounted() {
      this.reviewList = this.$route.params.reviewList
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

</style>