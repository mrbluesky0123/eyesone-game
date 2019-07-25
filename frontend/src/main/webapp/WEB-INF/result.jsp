<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<html class="h-100">
 <head>
 	<meta charset="utf-8">
 	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 	<meta name="description" content="">
 	<meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
 	<meta name="generator" content="Jekyll v3.8.5">
 	<title>도저히 아이즈원 게임이라고 타이틀 못달겠다</title>

	<link rel="stylesheet" href="/webjars/bootstrap/4.3.1/css/bootstrap.min.css">

	<link rel="stylesheet" type="text/css" href="/webjars/animate.css/3.5.2/animate.min.css">
	<link rel="stylesheet" type="text/css" href="/static/css/main.css">

 </head>
  <body class="d-flex flex-column h-100">
  <header>
 	 <!-- Fixed navbar -->
	<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="#">아이즈원 게임입니다...</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    	<div class="collapse navbar-collapse" id="navbarCollapse">
      		<ul class="navbar-nav mr-auto">
				<li class="nav-item">
				    <a id="userNameId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">사용자명 :  ${userName} </a>
				 </li>
				 <li class="nav-item">
				    <a id="levelId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">최종 난이도 : ${level} </a>
				 	<input id="levelNumber" type="hidden" value="${level} "/>
           			<input id="sessionId" type="hidden" value="${sessionId }" />
		   			<input id="userName" type="hidden" value="${userName }" />
		   			<input id ="timeSec" type="hidden" value="${clearTime} " />
				    
				 </li>
				 <li class="nav-item">
				   <a id="timeLapseId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">경과 시간 : ${clearTime} </a>
				 </li>

			</ul>
		</div>
 	</nav>
</header>

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
    <h1 id="stopWatchId" class="mt-5">랭킹 현황</h1>
   
    <table id="resultTable" class="table">
	 <thead>
	   <tr>
	      <th>rank</th>
	      <th>점수</th>
	      <th>닉네임</th>
	      <th>time</th>
	   </tr>
	 </thead>
	 <tbody>
	 
	 
	 </tbody> 
	</table>
  </div>
  <input id="continueBtn" type="button" class="btn btn-lg btn-primary btn-block" value="재도전" onclick="onClickContinueBtn()"/>
  <input id="newGameBtn" type="button" class="btn btn-lg btn-primary btn-block" value="처음으로" onclick="onClickNewGameBtn()"/>
  <input id="myScore" type="hidden"  /> 
</main>

	
	
<footer class="footer mt-auto py-3">
  <div class="container">
    <span class="text-muted"></span>
    <h3>SNS 공유하기</h3>
    <div class="row">
		
		<!-- 카카오 버튼  -->
		<a id="kakao-link-btn" href="javascript:sendLinkKakao();">
		<img src="//developers.kakao.com/assets/img/about/logos/kakaolink/kakaolink_btn_medium.png"/>
		</a>
		<p>&nbsp;&nbsp;&nbsp;&nbsp; </p>
	   <!-- facebook -->
		<a href="javascript:sharefacebook('http://localhost:8010/result')" >
		<img src="/static/img/fb.png" width="70px" />
		</a>

	</div>
  </div>
</footer>

	<script src="/webjars/jquery/3.4.1/jquery.min.js"></script>
	<script src="/webjars/bootstrap/4.3.1/js/bootstrap.min.js"></script>
	<script src="/webjars/bootstrap-notify/3.1.3/bootstrap-notify.min.js"></script>
	
	<script src="/webjars/sockjs-client/1.1.5/dist/sockjs.min.js"></script>
	<script src="/webjars/stomp-websocket/2.3.3/stomp.min.js"></script>
	<script src="/static/js/result.js"></script>
	
		

</body>

	<script>
	function sharefacebook(url){
		window.open("https://www.facebook.com/sharer/sharer.php?u=" + url);
	}
	</script>
	<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>
	<!-- 카카오 공유 내용 설정 로직 -->
	<script type='text/javascript'>
	 
	 
	  //<![CDATA[
	    // // 사용할 앱의 JavaScript 키를 설정해 주세요.
	    Kakao.init('f6b1425ca7fe6126b623fa4a1672dfcc');
	    // // 카카오링크 버튼을 생성합니다. 처음 한번만 호출하면 됩니다.
function sendLinkKakao(){	    
debugger;
	  var world = '';
	  var user = $("#userName").val();
	  var sco = $("myScore").val();
	  
	  world = user+'님이 '+sco+'점을 획득했습니다. 도전하시겠습니까?' 
      console.log(world);
	  
	    Kakao.Link.sendDefault({
	      		    
	      container: '#kakao-link-btn',
	      objectType: 'feed',
	      content: {
	        title: 'IZ*ONE 키보드 게임',
	        description: world ,
	        imageUrl: 'https://i.redd.it/obceohfe3jh21.jpg',
	        link: {
	          mobileWebUrl: 'http://localhost:8010/result',
	          webUrl: 'http://localhost:8010/result'
	        }
	      },
	      social: {
	        likeCount: 286,
	        commentCount: 45,
	        sharedCount: 845
	      },
	      buttons: [
	        {
	          title: '웹으로 보기',
	          link: {
	            mobileWebUrl: 'http://localhost:8010/result',
	            webUrl: 'http://localhost:8010/result'
	          }
	        },
	        {
	          title: '앱으로 보기',
	          link: {
	            mobileWebUrl: 'http://localhost:8010/result',
	            webUrl: 'http://localhost:8010/result'
	          }
	        }
	      ]
	    });
	  //]]>
	}		  
	</script>

    
</html>
