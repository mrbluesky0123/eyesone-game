<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="UTF-8"%>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>스프링부트 웹소켓 메시징</title>
    <link rel="stylesheet" href="/webjars/bootstrap/4.3.1/dist/css/bootstrap.min.css">
    
    
	<link rel="stylesheet" type="text/css" href="/static/css/test.css"/>
</head>
<body>
    <div>
        <form id="frm" method="get" onsubmit="return false;">
            <h3>메시지 : <input id="message" type="text" name="message"></h3>
            <ol id="messages"></ol>
            <input type="button" id="submitBtn" value="메시지보내기">
        </form>
    </div>


	<script src="/webjars/jquery/3.4.1/dist/jquery.min.js"></script>
	<script src="/webjars/bootstrap/3.3.4/dist/js/bootstrap.min.js"></script>
	
	<script src="/webjars/sockjs-client/1.1.5/dist/sockjs.min.js"></script>
	<script src="/webjars/stomp-websocket/2.3.3/stomp.min.js"></script>

	<script src="/static/js/test.js"></script>

</body>
</html>