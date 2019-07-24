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
           <a id="userNameId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">사용자명 :  ${userName}  </a>
        	
        </li>
        <li class="nav-item">
           <a id="levelId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">현재 난이도 : ${level} </a>
           <input id="levelNumber" type="hidden" />
           <input id="sessionId" type="hidden" value="${sessionId }" />
		   <input id="userName" type="hidden" value="${userName }" />
		   <input id ="timeSec" type="hidden" />
        </li>
        <li class="nav-item">
           <a id="timeLapseId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true"> </a>
        </li>

      </ul>
    </div>
  </nav>
</header>

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
    <h1 id="stopWatchId" class="mt-5">게임 준비중 입니다</h1>
    <p id="contentId" class="lead"></p>
    
    <form class="form-answer">
		<input id="answerId" class="form-control" placeholder="정답 입력" required autofocus>
		<br>
		<button id="form-answer-submit" class="btn btn-lg btn-primary btn-block" type="submit">입력</button>
	</form>
	
	<form class="form-hidden" method="POST" >
		<input type="hidden" id="sessionIdToResult">
		<input type="hidden" id="userNameToResult">
		<input type="hidden" id="levelToResult">
		<input type="hidden" id="clearTimeToResult">
		<input type="submit" id="btnToResult" hidden="true" >
	</form>
   
  </div>
</main>


<footer class="footer mt-auto py-3">
  <div class="container">
    <span class="text-muted"></span>
  </div>
</footer>


	<script src="/webjars/jquery/3.4.1/jquery.min.js"></script>
	<script src="/webjars/bootstrap/4.3.1/js/bootstrap.min.js"></script>
	<script src="/webjars/bootstrap-notify/3.1.3/bootstrap-notify.min.js"></script>
	
	<script src="/webjars/sockjs-client/1.1.5/dist/sockjs.min.js"></script>
	<script src="/webjars/stomp-websocket/2.3.3/stomp.min.js"></script>
	<script src="/static/js/main.js"></script>
</body>
    
</html>
