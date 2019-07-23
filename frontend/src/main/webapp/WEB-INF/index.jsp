<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="UTF-8"%>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>스프링부트 웹소켓 메시징</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sockjs-client/1.1.5/sockjs.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/stomp.js/2.3.3/stomp.min.js"></script>
</head>
<body>
    <div>
        <form id="frm" method="get" onsubmit="return false;">
            <h3>메시지 : <input id="message" type="text" name="message"></h3>
            <ol id="messages"></ol>
            <input type="button" id="submitBtn" value="메시지보내기">
        </form>
    </div>

<script >
    $(document).ready(function () {
        var messageList = $("#messages");
        var socket = new SockJS('/stomp');
        var stompClient = Stomp.over(socket);
        stompClient.connect({}, function (frame) {
        	
            stompClient.subscribe("/topic/browser", function (data) {
                var message = data.body;
                messageList.append("<li>" + message +"</li>");
                });
            });
        });
/*       $("#submitBtn").off().on('click', function () {
            $.ajax({
                url : '/send/message?message='+$('#message').val(),
                type : 'get'
            });
    });*/
</script>
</body>
</html>