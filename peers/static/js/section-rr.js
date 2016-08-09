
$(document).ready(function(){                                       
    

    // rr_I1S1 //
    $(document.body).on("click", "#rr_I1S1_desc_yes", function(){

        $("#rr_I1S1_desc").hide();
        $("#rr_I1S1_ques1").show();
        $(this).closest('div.collapsible-body').prev('div.collapsible-header').find('.yes-apply-circle').addClass('active');
    });

    $(document.body).on("click", "#rr_I1S1_ques1_yes", function(){

        $("#rr_I1S1_ques1").hide();
        
        $("#rr_I1S1_ques3").show();
    });

    $(document.body).on("click", "#rr_I1S1_ques1_no", function(){

        $("#rr_I1S1_ques1").hide();
        
        $("#rr_I1S1_fail").show();
    });

    /*$(document.body).on("click", "#rr_I1S1_ques2 #continueq", function(){

        $("#rr_I1S1_ques2").hide();
        
        $("#rr_I1S1_success").show();
    })*/

    $(document.body).on('click','#rr_I1S1_ques3_yes',function() {
       $("#rr_I1S1_ques3").hide(); 
       //for screening
      /* $("#rr_I1S1_success").attr('data-id','rr_I1S1_ques3'); 
       $("#rr_I1S1_success").show();*/
        $('#rr_I1S1_ques3_scr').show();  ///Certificaiton question. 
    }); 

    $(document.body).on("click", "#rr_I1S1_ques3_no", function(){

        $("#rr_I1S1_ques3").hide();
        
        $("#rr_I1S1_fail").show();
    });

    $(document.body).on('click','#rr_I1S1_ques3 #restartq',function() {
        $('#rr_I1S1_ques3').hide();
        
        $("#rr_I1S1_ques1").show();
    });

    $(document.body).on('click','#rr_I1S1_ques3_scr #continueq',function() {
        $('#rr_I1S1_ques3_scr').hide();
        $('#rr_I1S1_ques4').show();
    });

    $(document.body).on('click','#rr_I1S1_ques3_scr #restartq',function() {
        $('#rr_I1S1_ques3_scr').hide();
        $('#rr_I1S1_ques3').show();
    });

    $(document.body).on('click','#rr_I1S1_ques4 #continueq',function() {
        $('#rr_I1S1_ques4').hide();
        if($('#rr_I1S1_ques4_ans').val() < 5) {
             $("#rr_I1S1_fail").show();
        }
        else if($('#rr_I1S1_ques4_ans').val() >=5 && ($('#rr_I1S1_ques4_ans').val() < 99))  
            $('#rr_I1S1_ques5').show();
        else {
        $("#rr_I1S1_success").attr('data-id','rr_I1S1_ques4');    
        $("#rr_I1S1_success").show();
     }
    });

    $(document.body).on('click','#rr_I1S1_ques4 #restartq',function() {
        $('#rr_I1S1_ques4').hide();
        $('#rr_I1S1_ques3_scr').show();
    });

    $(document.body).on('click','#rr_I1S1_ques5_yes',function() {
        $('#rr_I1S1_ques5').hide();
        $('#rr_I1S1_success').attr('data-id','rr_I1S1_ques5');
        $("#rr_I1S1_success").show();
    });

    $(document.body).on('click','#rr_I1S1_ques5_no',function() {
        $('#rr_I1S1_ques5').hide();
         $("#rr_I1S1_fail").show();
        //$('#next-strategy').trigger('click'); 
    });

    $(document.body).on('click','#rr_I1S1_ques5 #restartq',function() {
        $('#rr_I1S1_ques5').hide();
        $('#rr_I1S1_ques4').show();
    });
    /*$(document.body).on("click", "#rr_I1S1_ques2 #restartq", function(){

        $("#rr_I1S1_ques2").hide();
        
        $("#rr_I1S1_ques3").show();
    })*/

    $(document.body).on("click", "#rr_I1S1_success #restartq", function(){

        $("#rr_I1S1_success").hide();
        var div = $('#rr_I1S1_success').attr('data-id');
        $("#"+div).show();
    })

    $(document.body).on("click", "#rr_I1S1_fail #restartq", function(){

        $("#rr_I1S1_fail").hide();
        
        $("#rr_I1S1_ques1").show();
    })
    // rr_I1S1 //
 
    //link to second strategy.    
    $(document.body).on('click','#rr_I1S1_fail #continueq',function() {
       $('#next-strategy').trigger('click');
    });  
    

    // rr_I1S2 //

    $(document.body).on("click", "#rr_I1S2_desc_yes", function(){

        $("#rr_I1S2_desc").hide();
        $("#rr_I1S2_ques1").show();
    })

    

    $(document.body).on("click", "#rr_I1S2_ques1_yes", function(){

        $("#rr_I1S2_ques1").hide();
        
        $("#rr_I1S2_success").show();
    })

    $(document.body).on("click", "#rr_I1S2_ques1_no", function(){

        $("#rr_I1S2_ques1").hide();
        
        $("#rr_I1S2_fail").show();
    })
    

    $(document.body).on("click", "#rr_I1S2_success #restartq", function(){

        $("#rr_I1S2_success").hide();
        
        $("#rr_I1S2_ques1").show();
    })

    $(document.body).on("click", "#rr_I1S2_fail #restartq", function(){

        $("#rr_I1S2_fail").hide();
        
        $("#rr_I1S2_ques1").show();
    })


    // rr_I1S2 //
    
});
