$(document).ready(function(){

	// $('form input[type="text"], form select, form textarea, form input[type="numeric"]').on('focus', function() {
 //        $(this).removeClass('input-error');
 //    });


	// $('#project-submit').on('click',function(e){
	// 	var email_check = true;
	// 	var contact_check = true;

	// 	$('form input[type="text"], form select, form textarea, form input[type="numeric"] ').each(function(){
	// 		/*if ($(this).attr('id') == "offAddress" || $(this).attr('id') == "nameOfOrg"){*/
	// 		if( $(this).val() == "" ) {
	//             $(this).addClass('input-error');
	//             $('#submit').removeClass('not-active');
	//             email_check = false;
	//             contact_check = false;
	           
	//         }
	//         else {
	//             $(this).removeClass('input-error');
	         
	//             var sEmail = $('#emailId').val();
	//             var sContactNo = $('#contactNo').val();
	//             if (validateEmail(sEmail)) {
				  
	// 			}
	// 			else {
	// 			 $('#emailId').addClass('input-error');
	// 			 email_check = false;
	// 			}
				

	// 			if (validatePhone(sContactNo)) {
				  
	// 			}
	// 			else {
	// 			 $('#contactNo').addClass('input-error');
	// 			 contact_check = false;
	// 			}
	//         }
	   
	// 	});
	//      if (email_check &&  contact_check){
	// 		$('#submit').addClass('not-active');
			
	// 	}
	// 	else{
	// 		e.preventDefault();
	// 		return;
	// 	}
 //    });

	// Function that validates email address through a regular expression.
	// function validateEmail(sEmail) {
	// 	var filter = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
	// 	if (filter.test(sEmail)) {
	// 		return true;
	// 	} else {
	// 		return false;
	// 	}
	// }	

	// function validatePhone(txtPhone) {
	// 	var filter = /^[0-9-+]+$/;
	// 	if (filter.test(txtPhone)) {
	// 		return true;
	// 	} else {
	// 		return false;
	// 	}
	// }

	// $('#city_type, #campus_type, #supply_type' ).on('click', function(){
	// 	var nameId = $(this).attr('page-content');
	// 	$('#city_type, #campus_type, #supply_type').removeClass('active selected');
	// 	$(this).addClass('actve selected'); 	   
	// 	$('.tabContents div').addClass('contentHide').removeClass('contentDisplay');
	// 	$('.tabContents #'+nameId).addClass('contentDisplay').removeClass('contentHide'); 
	// });

	// $('body').on('change', '#electricity',function(){
	// 	var unit = $(this).val();
	// 	$('#cust_load_unit, #annual_elect_unit').html(unit);

	// });
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
	var project_type = "";
	$('.project-type-btn').click(function(){
		$(".project-type-btn").children('span').show();
		$('.project-type-btn').children('i').hide();
		$(this).children('span').hide();
		$(this).children('i').show();
		project_type = $(this).attr('value');
		console.log($(this).attr('value'));
	});
	$('#logout-view').click(function(){
		$.ajax({
			type: 'GET',
			url: "/auth/logout/",
			success: function(response) {
				window.location.href = "/" ;	
			},
			error: function(error) {
			}
		});
		return false;
	});
	$("#project_submit_form").submit(function(event){
		console.log($(this).serialize()+"&project_type="+project_type);
		$.ajax({
			type: 'POST',
			url: "/projects/",
			data: $(this).serialize()+"&project_type="+project_type,
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			},
			success: function(response) {
				console.log(response);
				window.location.href = "/project/"+response['id']+"/information";
				// location.reload();
			},
			error: function(error) {
				console.log(error);
				console.log(error.responseText);
				$("#registererror").html(error.responseText);
			}
		});
		return false;
	});
	function submit_project_specific(project_id) {
          console.log("####################################")
          // $("#project_specific_form").submit(function(event){
          //   url = window.location.pathname;   
            $.ajax({
              type: 'PUT',
              url: "/projects/"+project_id+"/",
              data: $(this).serialize(),
              beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
              },
              success: function(response) {
                console.log(response);
                location.reload();
              },
              error: function(error) {
                console.log(error);
                console.log(error.responseText);
                $("#registererror").html(error.responseText);
              }
            });
              return false;
            // });
          };	
});
$(document.body).on('change','#electric_unit',function() {
	var unit = $(this).val();
	$('#annual-load , #annual-purchased').html(unit);
});