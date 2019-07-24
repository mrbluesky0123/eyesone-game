<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<html class="h-100">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>Sticky Footer Navbar Template · Bootstrap</title>

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
           <a id="userNameId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">사용자명 : </a>
        </li>
        <li class="nav-item">
           <a id="levelId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">현재 난이도 : </a>
        </li>
        <li class="nav-item">
          <a id="timeLapseId" class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">경과 시간 : </a>
        </li>

      </ul>
    </div>
  </nav>
</header>

<!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
    <h1 id="stopWatchId" class="mt-5">게임 준비중 입니다</h1>
   
    <table id="resultTable" class="table">
	 <thead>
	   <tr>
	      <th>rank</th>
	      <th>난이도</th>
	      <th>닉네임</th>
	      <th>time</th>
	   </tr>
	 </thead>
	 <tbody>
	 </tbody> 
	</table>
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
	<script src="/static/js/result.js"></script>
</body>
    
</html>