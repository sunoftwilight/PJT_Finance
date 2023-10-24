# 최종 결과

## 넓은 화면

![](C:\Users\v0041\AppData\Roaming\marktext\images\2023-09-09-17-55-45-image.png)

![](C:\Users\v0041\AppData\Roaming\marktext\images\2023-09-09-17-56-04-image.png)

<br>

## 좁은 화면

<img src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-09-09-17-56-45-image.png" title="" alt="" width="261">      <img src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-09-09-17-57-02-image.png" title="" alt="" width="262">

<br>

<br>

# 코드

## HTML 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Google Font 적용 -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bungee+Shade&family=Jua&family=PT+Serif:ital,wght@1,700&family=Rubik+Bubbles&display=swap" rel="stylesheet">
  
  <!-- 1. Bootstrap 적용 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
  
  <link rel="stylesheet" href="style.css">
  <title>sun.ovo Web</title>
</head>
<body>
  <!-- 메뉴 -->
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img class="ms-1 me-2" src="images/falling-star.png" alt="logo" width="30px">
        SUN.OVO
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse text-end" id="navbarSupportedContent">
        <ul class="navbar-nav mb-2 mb-lg-0">

          <li class="nav-item">
            <a class="nav-link" href="#frontpage">Frontpage</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#intro">Intro</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#project">Project</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="#skills">Skills</a>
          </li>
        </ul>
      </div>

    </div>
  </nav>

  <!-- 메인 콘텐츠 -->
  <main id="frontpage" class="ms-0 p-0 frontpage my-5">
    <div class="row">
      <div class="m-4 ms-0 d-flex align-self-center">
        <img class="col-3 ms-4" src="images/rabbit.png" alt="rabbit">
        <div class="flex-column align-self-end">
          <div class="ms-4 my-2 name display-1">Lee Haejin</div>
          <div class="ms-4 fe display-6">FrontEnd Web Developer</div>
        </div>
      </div>
    </div>
  </main>

  <div class="m-3"></div>

  <!-- 자기소개 -->
  <section id="intro" class="intro mx-4 my-5">
    <div class="card">
      <div class="container d-flex mx-0 my-2">
        <div class="row ">
          <img src="images/rabbit-7684132_1280.png" style="width: 10rem;" class="mt-3 card-img-top" alt="proimg">
        </div>
        <div class="row ms-2">
          <div class="card-body col-9 d-flex flex-column justify-content-center">
            <h4 class="card-title">저는,</h4>
            <p class="card-text intro_ex">웹 프론트엔드 개발자를 꿈꾸는 
            <span class="d-block d-sm-inline"><strong class="intro_name">이 해 진</strong> 입니다!</span></p>
          </div>
        </div>  
      </div> 
      <ul class="list-group list-group-flush">
        <li class="list-group-item"><span class="title">Major</span> : 전자공학부</li>
        <li class="list-group-item border-top"><span class="title">Activity</span> : 삼성 청년 SW 아카데미 10기</li>
        <li class="list-group-item border-bottom"><span class="title">E-mail</span> : sixb_0417@hanmail.net</li>
      </ul>

      <div class="card-body card_link">
        <span class="me-2">
          <img class="site-img" src="images/25231.png" alt="github">
          <a href="https://github.com/sunoftwilight" class="card-link link" target="_blank">Github</a>
        </span>
        <span>
          <img class="site-img" src="images/다운로드.png" alt="instagram">
          <a href="https://www.instagram.com/hellosunfy/" class="card-link link" target="_blank">Instagram</a>
        </span>
      </div>
    </div>
  </section>

  <div class="m-5"></div>

  <!-- 기술 스택 -->
  <section id="skills" class="skills my-5">
    <div class="display-5 ms-4 fe container mb-2">Skills</div>
      <div class="row d-flex justify-content-center ms-4">
        <img class="col-3 p-lg-5" src="images/html.png" alt="html">
        <img class="col-3 p-lg-5" src="images/css.png" alt="css">
        <img class="col-3 p-lg-5" src="images/python.png" alt="python">
        <img class="col-3 p-lg-5" src="images/C.png" alt="c">
      </div>
  </section>

  <!-- 꼬리말 -->
  <footer class="footer">Copyright 2023. sun.ovo. All rights reserved.</footer>


  <!-- 반응형 웹을 만드는 방법 ?? -->
  <!-- bootstrap 사용 - But, grid system 사용시 최대 단점 : breakpoint가 정해져 있어 원하는 pixel만큼 움직일 수 없음 -->
  <!-- 따라서 "Media Query"를 사용할 줄 알아야 함!! -->
  <!-- Ex. 470px 미만으로는 웹을 제공하지 않겠다! -->
  <h1 class="not-provided">이 사이트는 470px 사이즈 미만에서 보이지 않습니다.</h1>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</body>
</html>y="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</body>
</html>
```

<br>

## CSS 코드

```css
# 스크롤바 색상 변
body::-webkit-scrollbar{width: 16px;}
body::-webkit-scrollbar-track {background-color:#f1f1f1;}
body::-webkit-scrollbar-thumb {background-color:#fdf4c9;border-radius: 10px;}
body::-webkit-scrollbar-thumb:hover {background: #ffe985;}
body::-webkit-scrollbar-button:start:decrement,::-webkit-scrollbar-button:end:increment {
width:16px;height:16px;background:#fdf4c9;}

.navbar {
  background-color: #ffe985 !important;
  font-family: 'PT Serif', serif;
}

.frontpage {
  display: flex;
}

.name {
  font-family: 'Rubik Bubbles', cursive;
  color: #e6c121;
}

.fe {
  font-family: 'Jua', sans-serif;
  color: rgb(77, 77, 77);
}

.intro {
  font-family: 'Jua', sans-serif;
}

.intro_ex {
  font-size: large;
}

.intro_name {
  color: rgb(231, 158, 0);
  font-size: x-large;
}

.title {
  color: rgb(247, 184, 10);
  font-weight: bold;
  text-shadow: #756002;
}

.link {
  color: rgb(231, 158, 0);
}

.site-img {
  width: 15px;
  height: 15px;
  margin-bottom: 5px;
}


.project {
  height: 300px;
}

.skills {
  height: 300px;
}

.footer {
  height: 50px;
  color: rgb(119, 119, 119);
  position: fixed;
  font-weight: bold;
  text-shadow: #464646;
  bottom: 0;
  width: 100%;    /* 한 행 다 쓰기 */
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'PT Serif', serif;
}

/* 1. not-provided 클래스는 기본적으로 보이지 않도록 설정 */
.not-provided {
  display: none;
}

/* 2. 470px 이하에서는, not-provided만 보이도록 설정 */
@media (max-width: 470px) {
  main,
  #
  section,
  nav,
  footer {
    display: none;
  }
  
  .not-provided {
    display: block;
  }
}
```

<br>

<br>

# 어려웠던 부분

1. **작은 화면에서 네비게이터 토글 글씨 오른쪽 정렬** <br>
   
   ![](C:\Users\v0041\AppData\Roaming\marktext\images\2023-09-09-18-10-18-image.png)

        => 텍스트 하나하나가 line 전체를 모두 포함하고 있으므로 각 페이지별 요소들을 묶어 justify-content-end를 통해 오른쪽 정렬을 하면 될 것이라 생각했다. 하지만, 이는 공간 배치에 대한 명령어이므로 화면에 변화가 없었다. <br>

        => 이후 block으로 설정하여 justify-content-end를 적용해보았으나 결과는 동일했다. <br>

        => 요소 각각이 모두 text이므로 단순히 text-end를 설정하면 되는 문제였다. <br>

<br>

2. **메인 콘텐츠 사진과 이름(희망 직무)을 나란히 놓으면서, 이름은 아래쪽 정렬하기** <br>
   
   => align-self와 align-item, align-content 각각의 명령어에 대한 구분이 아직 명확하게 되지 않은 느낌이다. 어떤 상황에 어떤것을 써야할 지 경험적으로 찾아나갔는데, 개념의 정립이 다시 필요할 거 같다.

<br>

<br>

# 새롭게 배운 부분 (개념 Remind)

**1. align-content** <br>

=> 요소들을 교차 축을 기준으로 여러 행을 정렬 <br>

=> 요소들이 위치할 공간을 분배하는 역할 <br>

=> 여러 행을 정렬하므로 한줄 짜리 행 or nowrap 상태에는 효과가 없음 <br>

<br>

**2. align-items** <br>

=> 요소들이 위치한 해당 행을 교차 축을 기준으로 정렬 <br>

<br>

**3. align-self** <br>

=> 해당 요소 하나만 교차 축을 기준으로 정렬








