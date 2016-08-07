$(document).ready(function(){
	var csrftoken = getCookie('csrftoken');
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	};
	$("#login_form").submit(function(event){
		$("#loginerror").html("");
		$.ajax({
			type: 'POST',
			url: "/auth/login/",
			data: $(this).serialize(),
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(response) {
				window.location.href="/dashboard/";
			},
			error: function(error) {
				$("#loginerror").html(error.responseJSON.non_field_errors);
			}
		});
		return false;
	});

	$("#register_form").submit(function(event){
		$("#registererror").html("");
		$.ajax({
			type: 'POST',
			url: "/auth/register/",
			data: $(this).serialize(),
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(response) {
				$(".form").html("<p>An email with activation link have been sent to the email address.</p>")
			},
			error: function(error) {
				$("#registererror").html(error.responseText);
			}
		});
		return false;
	});
});