# 더 추가하고 싶은 것

1. 메인 - 영화 포스터 크기 정렬 | `완료`
2. 메인 - 배경 영상 연속재생 or 재생 목록 불러오기 or 인기 영화 video API 받아온 뒤 연속재생
3. 반응형 페이지 - 화면 비율에 따라
4. 추천 영화 목록 - 최신 영화로 보여주기 (since 2010)



## TIL
- CSS selector는 가능한 구체적으로 만들기 : 영향을 주고자 하는 요소에만 영향을 미치도록
- CSS는 kebab-case로 네이밍
- display grid 참고 : https://studiomeal.com/archives/533
- sessionStorage <-> localStorage
  - localStorage는 브라우저가 종료돼도 데이터가 남아있지만, session의 경우 데이터가 소멸됨
  - 로그인 정보나 영화데이터 정보 저장의 경우, localStorage보다 브라우저가 종료되면 사라지는 sessionStorage를 사용하는 것이 더 나을 것 같다고 판단, -> 전체 코드 수정!
- MainView의 인기 영화 목록 캐러셀 - 버튼 클릭 시 transform으로 내부 박스 이동하기
  - overflow 되는 부분은 가려지도록 (overflow: hidden)
  - transform: translate(00%)
  - 한계 : infinite carousel은 불가

