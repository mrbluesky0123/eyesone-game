$(".form-start").submit(function() {
	var data = {
		'userName' : $('#inputUserName').val()
	};
	
	var dataToJson = JSON.stringify(data);
	
	$.ajax({
		url : "/enter",
		method : "post",
		contentType: "application/json",
		data : dataToJson,
		success : function(result) {
			location.href = 'main';
		}
	});
	return false;
});