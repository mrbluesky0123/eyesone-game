$(document).ready(function() {
	
	var socket = new SockJS('/stomp');
	var stompClient = Stomp.over(socket);
	stompClient.connect({}, function(frame) {
		stompClient.subscribe("/topic/browser", function(data) {
			notify(data.body);
		});
	});
	  
	//정답 입력 버튼 크릭시 이벤트
	$(".form-answer").submit(function() {
		var data = {
			'content' : $('#inputUserName').val(),
			'answer' : $('#answerId').val()
		};
		
		var dataToJson = JSON.stringify(data);
		
		console.log("정답 입력 버튼이 클릭되었습니다.");
		
		$.ajax({
			url : "http://localhost:8080/checkAnswer",
			method : "post",
			contentType: "application/json",
			data : dataToJson,
			success : function(result) {
				console.log("=====정담 확인 결과 main.js ======");
				
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
	
	printTime();
	//timerId = setInterval(PrintTime, 1000);
	
});

//추후 url 변경 필요
function getContent(level){
debugger;	
	console.log("level ==> "+ level);
	
	$.ajax({
		url : "http://10.250.172.243:8080/getQuestion/?level=" + level,
		method : "get",
		success : function(res) {
			
			console.log("=====문제 받는 곳 main.js ======");
			
			$('#answerId').focus();
			$('#stopWatchId').text('2초안에 입력하세요!');
			$('#levelId').text('현재 난이도 : ' + res.level);
			$('#contentId').text(res.content);
			$('#answerId').attr('disabled','false');
			$('#form-answer-submit').attr('disabled','false');
		}
		,error: function(request, status, error){
	    	debugger;
	    },
	    complete : function(result){
	    	debugger;
	    	$('#answerId').focus();
			$('#stopWatchId').text('2초안에 입력하세요!');
			$('#levelId').text('현재 난이도 : ' + "1");
			$('#contentId').text("가나다");
			$('#answerId').attr('disabled','false');
			$('#form-answer-submit').attr('disabled','false');
	    }
	});
}

//사자후
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


//경과시간 타이머 계산 
function printTime(){
	
	console.log("타이머 들어오나");
	
	var outTime = $("#timeLapseId");
	
	var setTime = 0;
	var time = "";
	
	function minusCount() {
		
		setTime ++;
		
		m = Math.floor(setTime / 60);
        s = setTime % 60 ;
        
        if(m == 0){
        	
        	if(s == 1){
        		
        		getContent(1);
        	}
        	
        	time = s + "초";
        }
        else{
        	time = m+"분" + " : " + s +"초";
        }
		
		outTime.text("경과 시간 : "+ time);
	}
	
	minusCount();
	setInterval(minusCount,300);
			
	if(setTime < 0){
		alert("종료");
	}
		
}
//answerId
//
//timeLapseId
//
//levelId
//
//userNameId