$(document).ready(function() {
	var socket = new SockJS('/stomp');
	var stompClient = Stomp.over(socket);
	stompClient.connect({}, function(frame) {
		stompClient.subscribe("/topic/browser", function(data) {
			notify(data.body);
		});
	});
	
  
	
	$(".form-answer").submit(function() {
		var data = {
			'content' : $('#inputUserName').val(),
			'answer' : $('#answerId').val()
		};
		
		var dataToJson = JSON.stringify(data);
		
		$.ajax({
			url : "/정답메소드",
			method : "post",
			contentType: "application/json",
			data : dataToJson,
			success : function(result) {
				$('#answerId').attr('disabled','true');
				$('#form-answer-submit').attr('disabled','true');
				$('#contentId').text('');
				$('#stopWatchId').text('정답입니다! 긴장하세요. 잠시후 게임이 시작됩니다.');
				setTimeout(getContent(level),2000);
			}
		});
		return false;
	});

	$("#answerId").keydown(function(key) {

		if (key.keyCode == 13) {
			$('#form-answer-submit').submit();
		}

	});
});


function getContent(level){
	$.ajax({
		url : "/문제요청메소드?level=" + level,
		method : "get",
		success : function(res) {
			$('#answerId').focus();
			$('#stopWatchId').text('2초안에 입력하세요!');
			$('#levelId').text('현재 난이도 : ' + res.level);
			$('#contentId').text(res.content);
			$('#answerId').attr('disabled','false');
			$('#form-answer-submit').attr('disabled','false');
		}
	});
}


function notify(message){
	  $.notify({
	        icon: '/static/img/rankChange.png',
	        title: '기록 갱신!',
	        message: message
	    },{
	        type: 'minimalist',
	        delay: 5000,
	        icon_type: 'image',
	        template:
	        '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
	        '<img data-notify="icon" class="img-circle pull-left">' +
	        '<span data-notify="title">{1}</span>' +
	        '<span data-notify="message">{2}</span>' +
	        '</div>'
	    });
}
//answerId
//
//timeLapseId
//
//levelId
//
//userNameId