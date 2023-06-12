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
            <iframe width="1000px" height="400px" src="https://www.youtube.com/embed/kihrFxwdMb4?&amp;playlist=kihrFxwdMb4&start=0&mute=1&autoplay=1&loop=1&modestbranding=0&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>

        <div class="popular-movie">
            <div class="prev-button" @click="clickPrevButton">prev</div>
            <div class="popular-movie-list-box">
                <div class="popular-movie-list" :style="{transform: `translate(${this.transformNum}vw)`}">
                    <div v-for="movie in movieList" :key="movie.id" class="popular-movie-box">
                        <img class="popular-movie-img" :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`">
                    </div>
                </div>
            </div>
            <div class="next-button" @click="clickNextButton">next</div>
        </div>

        
        
        <!-- <div class="wrapper">
            <section id="section1">
            <a href="#section3" class="arrow__btn">‹</a>
            <div class="item">
            <img src="https://occ-0-1567-1123.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABRvngexxF8H1-OzRWFSj6ddD-aB93tTBP9kMNz3cIVfuIfLEP1E_0saiNAwOtrM6xSOXvoiSCMsihWSkW0dq808-R7_lBnr6WHbjkKBX6I3sD0uCcS8kSPbRjEDdG8CeeVXEAEV6spQ.webp">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABZEK-7pZ1H5FD4cTyUb9qB_KeyJGz5p-kfPhCFv4GU_3mbdm8Xfsy4IBchlG9PFNdGff8cBNPaeMra72VFnot41nt0y3e8RLgaVwwh3UvyM2H2_MkmadWbQUeGuf811K7-cxJJh7gA.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABQCoK53qihwVPLRxPEDX98nyYpGbxgi5cc0ZOM4iHQu7KQvtgNyaNM5PsgI0vy5g3rLPZdjGCFr1EggrCPXpL77p2H08jV0tNEmIfs_e8KUfvBJ6Ay5nM4UM1dl-58xA6t1swmautOM.webp">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABdYtAqj8CyaJTWq5taD8Ro_UgwH3nne9QpFGVps-2J3IG-leqrfqXFii4jzZn48nPYTkrlwKQEV0R7_cEKlYBPRzdKqNODc-Oz26IL3LlLgFboXibIWXwxzeYxzuqn0I9TpARjeByw.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABbcCX42tsqGbBvO2y9CQv5-7QvYbCfoHtXsuc6NPCtZaKa4l4fBX3XWvUwG9F2A3CTsNpHVmulxBbdXKwK8Q6xGjejd9FoadGkZ7CnGrSl601TOQjzSHJ23NuIPC8j0QMGORL4uRIA.jpg">
            </div>
            <a href="#section2" class="arrow__btn">›</a>
            </section>
            <section id="section2">
            <a href="#section1" class="arrow__btn">‹</a>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABVopDZ5Fy9_fk_HO5WxHTXKKjKhtWFupbSjuvPwfLK_vytzon4EwRUdGgYJ34JwPxOTK_NkV3aXfkULMB0Dcct-FyfqzH-X44VXuRMp4QeBHlvKwWeZFpZlGdItPzmmg4scmwhG7SQ.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABTOj1-116yVcgKWMU2dI3GFR4x0fSkiGsqtLLeLUxRR7STaksjAqBTrYlTfrB8nIGnGvXksi0ewXAhVGg6-pLxpFOIfcpjK-pf8D5xehFZo5a6vJbo4L0AGbrzglbyUoq255QBJgRQ.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/a76057bcfd003711a76fb3985b1f2cf74beee3b8/AAAABd3IBDpxbRcHXvRMFCZeKa2aHLU1P4SJtrACMS9om3yhLjqPlvNlmR_fypPxjtbsbnKaC4JZhPSpDG4r_kdxSHHAltWguMcCB-1Y1OShr2zWfUv7Whf_39fNH5ZJ3_0gxQrs0akmQjQz44_LT7jXH5LMZ7iMBAzac5IEj4m7Fn_5OWEGYnVsDsKG-QTommDooULMDF9bEw.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/a76057bcfd003711a76fb3985b1f2cf74beee3b8/AAAABXSd7bhDddcwkq9XpksoQFCHVx29Sxl_h4hb2n3F2GIt32a4XWcOnctQfgnT5qdolv8UML6_xNB5CJ89h56wueb13mYmEBr0sx5e9iLPdtVcOQAOmKXKWHHXwFvJuCUwuNnL3s8eAQwqLXPVMHMEsujM684rUGrZNF2btN2GRy5-RyEslsxZO93V2Q_H2bWs8A8oayt1h5M.webp">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/a76057bcfd003711a76fb3985b1f2cf74beee3b8/AAAABbXWODpAWqVXcmmjMA7K-2mPkQpvwCLfSdeyhVXzR8A3MSpdSEnnjf4HEJJTYC-TnktU6njTUGAxmzWEYCaJbk4v_ZeL-7QGzmkvYBjg_N-evr2XmcX-Fanoyvu_nimFP4iigPe4O3Vr_WcgplhwkDrJwPUJa84wRLrNAx3TufN5V7cWRP4indqu5HQahvgFEqfL9zjp4g.jpg">
            </div>
            <a href="#section3" class="arrow__btn">›</a>
            </section>
            <section id="section3">
            <a href="#section2" class="arrow__btn">‹</a>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABRr4YxdaABuAuH_3FmSQZn7BCvLp-UUPsXE9MiYpvFP3CSUHV2zOew5oVqKqqdaOd3tbFVS0Uf67uIs7_eZydlCghg4nK0nMatRpPImABwTOhnNzCLCxdKrua7pPIcPCZqBYTeAO5g.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABTyWK1MKaw8GcObtz47R2Tj7wkLJ7qQu9tk6TVpcoyxpzD4B-zZ569bQ5vGrREBL-MWFkGilXUwy7tCDaj2XOGkUB4RsbbFAmp9NgSr6lygMpUGNHSlyfrFbUORsRkrxSIoh_ggOvg.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/a76057bcfd003711a76fb3985b1f2cf74beee3b8/AAAABY7NwkWEJIfXsn6t3Li4bGSCQ1nEErPisI5ZZtXlC-_VRBZOUrhWK5X3vt3t6SR_cpgVhCwxgQqFFDJhk62Kk8hawOnYGZMr0LKeLczMFV2zalCFjkcdLksvT4HB2LEi6LFyruyk3Uu0LmNGsHfC2A8Bly60smr_3sDbz4RruXcklPOG1qYq9wUVu3zfaiwNvqmG4b8aFA.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/a76057bcfd003711a76fb3985b1f2cf74beee3b8/AAAABemXHOga9feFnOux6I2YyACBD94wvM7N3vcTGIfMpQ_BcaXeoeM9XyzdVdamKtxt0SHXZfvsl6czcp3E48tXMLtHBxuQsh1BjHtPGgJDZ81je_FjItINiqzLtir0A30s_e4KR8G3d7AYAPDjZVOY97bNpzNqtkcHcGp7fGnJByVCps1uLfG9U9tK3Ma1A_3JbRt0NiT2_Q.jpg">
            </div>
            <div class="item">
            <img src="https://occ-0-243-299.1.nflxso.net/dnm/api/v5/rendition/a76057bcfd003711a76fb3985b1f2cf74beee3b8/AAAABVxuRB932hvre-XP0gh6ar5ztoR3Oe3QjKHkyvcDnRak2MKXOrx5H7mFQSvggefMFOppwEs7ZCCpiqrJ_CYGvtvYB9NpU4SWUtNO6uV2u-DTID267AcHjHcGvGBQJ1ufddDkxcGOZyi5MlOQ5QUmBun4652FbYUnib3zMYQDgcna_Pvz8y_HO5fbokxezrRR1JZAAiqFSQ.jpg">
            </div>
            <a href="#section1" class="arrow__btn">›</a>
            </section>
        </div> -->


        
        <!-- <div class="gallery">
            <div v-for="movie in movieList" :key="movie.id" class="content_box">
                <div class="movie_box">
                    <div class="img_box">
                        <img class="img_box_img" @click="gotoMovieDetail(movie)" :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`"><br>
                    </div>
                    <div class="content_box_detail">
                        <p class="movie_title" @click="gotoMovieDetail(movie)" >{{ movie.title }}</p>
                    </div>
                </div>
            </div>
        </div> -->
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
            // videoKeyList: ['a8Gx8wiNbs8', '0-wPm99PF9U'],
            videoKey: '',
            video: null,
            transformNum: 0,
        }
    },
    methods: {
        showMovies: function() {
            axios({
                method: 'get',
                url: `${API_URL}/api/movies/`,
            })
            .then(res => {
                this.movieList = res.data
                // localStorage.clear('movieList')
                sessionStorage.setItem('movieList', JSON.stringify(this.movieList))
                // this.test = localStorage.getItem('movieList')
            })
            .catch(err => {
                console.log(err)
            })  
        },
        // 클릭 시 Movie 상세페이지로 이동
        gotoMovieDetail(movie) {
            this.$router.push({ name: 'MovieDetail', params: { id: movie.id, movie: movie }})
            sessionStorage.setItem('moviedetail', JSON.stringify(movie))
        },

        // 토큰
        setToken: function() {
            const token = sessionStorage.getItem('jwt')
            const config = {
                Authorization: `Bearer ${token}`
            }
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
        },
        // prev 버튼 클릭 시 앞으로 이동
        clickPrevButton() {
            this.transformNum += 80
        },
        // next 버튼 클릭 시 뒤로 이동
        clickNextButton() {
            this.transformNum += -80
        },
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
/* 
.carousel_box {
    position: absolute;
    display: flex;
    filter: brightness(70%); 
} */

.video_box {
    padding-bottom: 56.25%; 
    height: 0; 
    overflow: hidden;
    position: relative;
    /* top: -185px; */
    /* display: flex; */
    /* z-index: 0; */
    /* width: 100%; */
}

.video_box iframe,
.video_box object,
.video_box embed {
    position:absolute; 
    top:0; 
    left:0; 
    width:100%; 
    height:100%;
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
    width: 500px;
}

.movie_title {
    color: #dbbf0f;
    text-shadow: black;
    background-color: rgba(39, 39, 39, 0.411);
    border-radius: 7px;
    padding: 0 7px;
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
    /* cover : 가로세로 비율 유지 */
    object-fit: cover;
    width: 350px;
    height: 520px;
    margin-top: 50px;
    margin-left: 20px;
    margin-right: 20px;
    /* transition-delay: 0.01s; */
    transition-duration: 0.4s;
    box-shadow: 10px 10px 30px black;
    border-radius: 5px;
}

.img_box_img:hover {
    width: 370px;
    height: 540px;
    color: black;
    margin: 10px;
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

.popular-movie {
    position: absolute;
    /* top: 40vh; */
    bottom: 3vh;
    background-color: rgba(128, 128, 128, 0.33);
    width: 90%;
    left: 5%;
    overflow: hidden;
    display: flex;
    align-items: center;
}

.popular-movie-list-box{
    width: 100%;
    display: flex;
    align-items: center;
    /* transform: translate(-50%); */
}

.popular-movie-list {
    /* position: relative; */
    display: flex;
    /* width: 100%; */
    /* overflow: hidden; */
    /* grid-template-columns: repeat(6, auto); */
    /* justify-content: space-evenly; */
}

.popular-movie-box {
    background-color: red;
    width: 200px;
}

.popular-movie-img {
    width: 200px;
    /* height: 100%; */
    /* object-fit: fill; */
}

.prev-button {
    position: absolute;
    z-index: 3;
    left: 0;
    background-color: blueviolet;
    font-size: 20px;
}

.next-button {
    position: absolute;
    right: 0;
    background-color: blueviolet;
    font-size: 20px;
}
</style>

