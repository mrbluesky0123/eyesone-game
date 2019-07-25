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
		debugger;
		var data = {
			'content' : $('#contentId').text(),
			'answer' : $('#answerId').val()
			
		};
debugger;		
		console.log("궁금=========>"+ $('#contentId').val() );
		var dataToJson = JSON.stringify(data);
		
		console.log("정답 입력 버튼이 클릭되었습니다.");
		
		$.ajax({
			url : "http://eyesone-game-service/game/checkAnswer",
			method : "post",
			contentType: "application/json",
			data : dataToJson,
			success : function(result) {
debugger;							
				console.log("=====정답 확인 결과 main.js ======");
				
				if (result){
					$('#answerId').attr('disabled','true');
					$('#form-answer-submit').attr('disabled','true');
					$('#contentId').text('');
					$('#stopWatchId').text('정답입니다! 긴장하세요. 잠시후 게임이 시작됩니다.');
					
					setTimeout(function(){
						
						var level = $('#levelNumber').val();
						
						level++;
						
						getContent(level)
					},2000);
				}else{
					
					var userName = $('#userName').val();
					var sessionId = $('#sessionId').val();
					var clearTime = $('#timeSec').val();
					var level = $('#levelNumber').val();
					
					endGame(sessionId, userName, level, clearTime);
					
				}
			
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


function timeout1(){
	
}

//추후 url 변경 필요
function getContent(level){
debugger;	
	console.log("level ==> "+ level);
	
	$.ajax({
		url : "http://eyesone-game-service/game/getQuestion/" + level,
		method : "get",
		success : function(res) {
		debugger;	
			console.log("=====문제 받는 곳 main.js ======");
			
			$('#answerId').focus();
			$('#stopWatchId').text('5초 안에 입력하세요!');
			$('#levelId').text('현재 난이도 : ' + res.level);
			$('#levelNumber').val(res.level);
			$('#contentId').text(res.content);
			$('#answerId').val('');
			$('#answerId').attr('disabled',false);
			$('#form-answer-submit').attr('disabled',false);
			
			
		}
		,error: function(request, status, error){
	    	debugger;
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




//endGame
function endGame(sessionId, userName, level, clearTime ){
	debugger;
	   var data = {
			'session_id' : sessionId,    
			'user_name' : userName,
			'score' : Number(level),
			'clear_time' : Number(clearTime)
	   }
	   
	   var dataToJson = JSON.stringify(data); 
	   
	   console.log("endGame====2====>"+ dataToJson);
	   
		$.ajax({
			url : "http://eyesone-rank-service/score/sendresult"  ,
			method : "post",
			contentType: "application/json",
			data : dataToJson,
			success : function(res) {
			debugger;	
				console.log("===== 유저 점수 요청 ======");
				console.log("점수요청 res" + res);
				
//				$('#sessionIdToResult').val(data.session_id);
//				$('#sessionIdToResult').val(data.user_name);
//				$('#sessionIdToResult').val(data.score);
//				$('#sessionIdToResult').val(data.clear_time);
				
				//location.href = '/result'
			    location.href = '/result/'+ data.session_id + '/'+data.user_name+'/'+data.score+'/'+data.clear_time
							
			}
			,error: function(request, status, error){

			}
		});
	}

//경과시간 타이머 계산 
function printTime(){
	
	console.log("타이머 들어오나");
	
	var outTime = $("#timeLapseId");
	var outTimeSec = $("#timeSec");
	
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
		outTimeSec.val(setTime);
	}
	
	minusCount();
	setInterval(minusCount,1000);
			
}
//answerId
//
//timeLapseId
//
//levelId
//
//userNameId