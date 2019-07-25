$(document).ready(function() {
	
	var socket = new SockJS('/stomp');
	var stompClient = Stomp.over(socket);
	stompClient.connect({}, function(frame) {
		stompClient.subscribe("/topic/browser", function(data) {
			notify(data.body);
		});
	});
	
	var userName = $('#userName').val();
	var sessionId = $('#sessionId').val();
	var clearTime = $('#timeSec').val();
	var level = $('#levelNumber').val();
	
	result(sessionId, userName, level, clearTime);
	
});

//랭킹 정보 받아 오는 곳
function result(sessionId, userName, level, clearTime){
debugger;	
	var data = {
			'session_id' : sessionId,    
			'user_name' : userName,
			'score' : Number(level),
			'clear_time' : Number(clearTime)
	   }
	   
	var dataToJson = JSON.stringify(data); 
	
	console.log("result.js result()===>" + dataToJson);
	
	var html = '';
	
	$.ajax({
		url : "http://eyesone-rank-service:5000/score/getrankdata",
		method : "post",
		contentType: "application/json",
		data : dataToJson,
			success : function(result) {
				debugger;
				
			    
				//받아온 결과 result 화면 테이블에 출력
				for(i=0; i < result.response_body.length; i ++){
debugger;				  	
					if(result.response_body[i].requested == true)
					{
						html += '<tr style="color:red;">';
						html += '<td style="color:red;">' + result.response_body[i].rank + '</td>';
						html += '<td style="color:red;">' + result.response_body[i].score + '</td>';
						html += '<td style="color:red;">' + result.response_body[i].user_name + '</td>';
						html += '<td style="color:red;">' + result.response_body[i].clear_time + '</td>';
						html += '</tr style="color:red;">';
						
						$("#myScore").val(result.response_body[i].score);
					}
					else
					{
						html += '<tr>';
						html += '<td>' + result.response_body[i].rank + '</td>';
						html += '<td>' + result.response_body[i].score + '</td>';
						html += '<td>' + result.response_body[i].user_name + '</td>';
						html += '<td>' + result.response_body[i].clear_time + '</td>';
						html += '</tr>';
					}
					
					
				
				}	
				
				$("#resultTable tbody").append(html);
				
			}
		})
	
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

function onClickNewGameBtn(){
	location.href = '/';
}

function onClickContinueBtn(){
	var sessionChk = false;
	debugger;
	$.ajax({
		url : "http://eyesone-rank-service:5000/score/checkrestartable/"+$('#sessionId').val(),
		method : "get",
		contentType: "application/json",
		success : function(res) {
			debugger;	
			console.log("===== Session Check 요청 ======");
			// Session ID check
			if(res.response_code == "0000"){
				// Go to main
				location.href = '/main/'+ $('#sessionId').val() + '/'+$('#userName').val();
			}else{
				alert("Session expired!!");
				location.href = '/';
			}
		}
		,error: function(request, status, error){
			debugger;
		}
	});
	
	

}
//answerId
//
//timeLapseId
//
//levelId
//
//userNameId
