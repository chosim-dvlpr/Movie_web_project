<template>
  <div>
    <h1>여기는 ReviewList</h1>
    <h2>리뷰 리스트 보기</h2>
    <CreateReview @submit-review="addReview" />
    <p v-for="(review, index) in reviewList" :key="index">{{ review }}</p>
  </div>
</template>

<script>
import CreateReview from '@/components/CreateReview.vue'

export default {
    name: 'ReviewList',
    components: {
        CreateReview,
    },
    data() {
        return {
            reviewList: [],
        }
    },
    mounted() {
        // 로컬 스토리지에서 리뷰 불러오기
        const storedReviews = localStorage.getItem('reviewList')
        if (storedReviews) {
            this.reviewList = JSON.parse(storedReviews)
        }
    },
    methods: {
        addReview(event) {
            this.reviewList.push(event)

            // 로컬 스토리지에 데이터 저장
            localStorage.setItem('reviewList', JSON.stringify(this.reviewList))

            // 컴포넌트 데이터 업데이트 후 로컬 스토리지에서 다시 불러오기
            // const storedReviews = localStorage.getItem('reviewList')
            // if (storedReviews) {
            //     this.reviewList = JSON.parse(storedReviews)
            // }
        }
    },
}
</script>

<style>

</style>