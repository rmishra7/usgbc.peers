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
	$('#logout').click(function(){
		$.ajax({
			type: 'GET',
			url: "/auth/logout/",
			success: function(response) {
				window.location.href = "/" ;	
			},
			error: function(error) {
				$("#forgoterror").html(error.responseText);
			}
		});
		return false;
	});
	$("#add_new_bld").click(function(){
		$('.addNewBuilding').modal('show');
	});
	$("#project_submit_form").submit(function(event){
		$.ajax({
			type: 'POST',
			url: "/projects/",
			data: $(this).serialize(),
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(response) {
				location.reload();
			},
			error: function(error) {
				console.log(error);
				console.log(error.responseText);
				$("#registererror").html(error.responseText);
			}
		});
		return false;
	})
});