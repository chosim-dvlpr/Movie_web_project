<template>
  <div>
    <h1>여기는 Article View</h1>
    <h2>게시글 리스트 보기</h2>
    <CreateArticle @submit-article="addArticleList" />
    <p>{{ childArticle }}</p>
    <p v-for="(article, index) in articleList" :key="index">{{ article }}</p>
  </div>
</template>

<script>
import CreateArticle from '@/components/CreateArticle.vue'

export default {
    name: 'ArticleView',
    components: {
        CreateArticle,
    },
    data() {
        return {
            articleList: [],
            childArticle: null,
        }
    },
    methods: {
        addArticleList(event) {
            this.articleList.push(event)
        }
    }

}
</script>

<style>

</style>