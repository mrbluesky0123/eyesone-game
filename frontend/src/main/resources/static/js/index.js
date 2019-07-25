$(".form-start").submit(function() {
	var data = {
		'user_name' : $('#inputUserName').val()
	};
	
	var dataToJson = JSON.stringify(data);
	
	console.log("data===>"+ data);

	$.ajax({
		url : "http://eyesone-rank-service:5000/score/register_user",
		method : "post",
		contentType: "application/json",
		data : dataToJson,
		success : function(result) {
		debugger;
			console.log("result===>"+ result.response_body);
			
			location.href = '/main/'+ result.response_body + '/'+$('#inputUserName').val()
		}
	    ,error: function(request, status, error){

	    }

	});
	return false;
});