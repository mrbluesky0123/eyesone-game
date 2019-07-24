$(document).ready(function() {
	var messageList = $("#messages");
	var socket = new SockJS('/stomp');
	var stompClient = Stomp.over(socket);
	stompClient.connect({}, function(frame) {

		stompClient.subscribe("/topic/browser", function(data) {
			var message = data.body;
			messageList.append("<li>" + message + "</li>");
		});
	});
});
/*       $("#submitBtn").off().on('click', function () {
 $.ajax({
 url : '/send/message?message='+$('#message').val(),
 type : 'get'
 });
 });*/

