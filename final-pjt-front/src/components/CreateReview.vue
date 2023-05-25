<template>
  <div>
    <h2>리뷰 작성</h2>
    <h3>여기는 CreateReview 페이지</h3>
    <form @submit.prevent="submitReview">
      <div>
        <label for="title">제목:</label>
        <input type="text" id="title" v-model="post.title" required>
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea id="content" v-model="post.content" required></textarea>
      </div>
      <div>
        <label for="rating">평점:</label>
        <input type="number" id="rating" v-model="post.rating" min="0" max="5" required>
      </div>
      <div>
        <input type="checkbox" id="recommendation" v-model="post.recommendation">
        <label for="recommendation">이 영화를 추천합니다</label>
      </div>
      <button type="submit">작성 완료</button>
    </form>
    <hr>
    <hr>
  </div>
</template>

<script>
export default {
    name: 'CreateReview',
    data() {
        return {
            post: {
                title: '',
                content: '',
                rating: null,
                recommendation: false
            }
        }
    },
    methods: {
        submitReview() {
            // console.log(this.post)
            // this.$router.push({ name: 'MainView' })
            this.$emit('submit-review', this.post)
        }
    }
}
</script>

<style>

</style>