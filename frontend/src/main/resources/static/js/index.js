$(".form-start").submit(function() {
	var data = {
		'user_name' : $('#inputUserName').val()
	};
	
	var dataToJson = JSON.stringify(data);
	
	console.log("data===>"+ data);
debugger;	
	$.ajax({
		url : "http://198.13.47.188:5000/score/register_user",
		method : "post",
		contentType: "application/json",
		data : dataToJson,
		success : function(result) {
			debugger;
//			qwww123qasde124wewwwwwwibrht
			console.log("result===>"+ result.response_body);
			location.href = '/main'
//			location.href = '/main?sessionId='+ result.response_body;
		}
	    ,error: function(request, status, error){
	    	debugger;
	    },
	    complete : function(result){
	    	debugger;
	    	result = "qwww123qasde124wewwwwwwibrht";
	    	console.log("data===>" + data);
	    	location.href = '/main';
	    }
	});
	return false;
});