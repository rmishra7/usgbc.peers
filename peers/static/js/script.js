$('body').on('click', '#add_new_bld', function(event){
	$('.addNewBuilding').modal('show');	
	PageSelect('GeneralInfo');
});

 function PageSelect (pageName) {
    $.ajax({
      url: 'templates/'+pageName+'.html',

    }).done(function(data) {
      page_content = data;
      $(' form.modal-show').html(page_content);
      /*$( ".addNewBuilding" ).html('');
      $( ".addNewBuilding" ).append(page_content);*/
    });    
};

$('form.login-form input[type="text"], form.login-form select, form.login-form textarea').on('focus', function() {
        $(this).removeClass('input-error');
    });


$('#submit ').on('click',function(e){
	var email_check = true;
	var contact_check = true;

	 $('form.login-form input[type="text"], form.login-form select, form.login-form textarea').each(function(){
		/*if ($(this).attr('id') == "offAddress" || $(this).attr('id') == "nameOfOrg"){*/
			if( $(this).val() == "" ) {
	            $(this).addClass('input-error');
	            $('#submit').removeClass('not-active');
	            email_check = false;
	            contact_check = false;
	           
	        }
	        else {
	            $(this).removeClass('input-error');
	         
	            var sEmail = $('#emailId').val();
	            var sContactNo = $('#contactNo').val();
	            if (validateEmail(sEmail)) {
				  
				}
				else {
				 $('#emailId').addClass('input-error');
				 email_check = false;
				}
				

				if (validatePhone(sContactNo)) {
				  
				}
				else {
				 $('#contactNo').addClass('input-error');
				 contact_check = false;
				}
	        }
	   
		});
	     if (email_check &&  contact_check){
			$('#submit').addClass('not-active');
			
		}
		else{
			e.preventDefault();
			return;
		}	 
	 	
    });

	// Function that validates email address through a regular expression.
	function validateEmail(sEmail) {
	var filter = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
	if (filter.test(sEmail)) {
	return true;
	}
	else {
	return false;
	}
	}	

	function validatePhone(txtPhone) {
    /*var a = document.getElementById(txtPhone).value;*/
    var filter = /^[0-9-+]+$/;
    if (filter.test(txtPhone)) {
        return true;
    }
    else {
        return false;

    }
}

$('.tabs li' ).on('click', function(){
  	   var nameId = $(this).attr('page-content');
  	   $('.tabs li').removeClass('active selected');
  	   $(this).addClass('actve selected'); 	   
  	   $('.tabContents div').addClass('contentHide').removeClass('contentDisplay');
  	   $('.tabContents #'+nameId).addClass('contentDisplay').removeClass('contentHide');
  	  
  	}); 
 
	