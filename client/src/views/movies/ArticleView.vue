<template>
  <div>
    <h1>여기는 Article View</h1>
    <h2>게시글 리스트 보기</h2>
    <CreateArticle @submit-article="addArticleList" />
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
    mounted() {
        // 로컬 스토리지에서 게시글 불러오기
        const storedArticles = localStorage.getItem('articleList')
        if (storedArticles) {
            this.articleList = JSON.parse(storedArticles)
        }
    },
    methods: {
        addArticleList(event) {
            this.articleList.push(event)

            // 로컬 스토리지에 데이터 저장
            localStorage.setItem('articleList', JSON.stringify(this.articleList))

            // 컴포넌트 데이터 업데이트 후 로컬 스토리지에서 다시 불러오기
            // const storedArticles = localStorage.getItem('articleList')
            // if (storedArticles) {
            //     this.articleList = JSON.parse(storedArticles)
            // }
        }
    },
}
</script>

<style>

</style>