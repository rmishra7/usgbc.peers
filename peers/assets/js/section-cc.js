$(document).ready(function(){ 

    // ce_I1S1 //
    $(document.body).on("click", "#cc_I1S1_desc_yes", function(){

        $("#cc_I1S1_desc").hide();
        $("#cc_I1S1_ques1").show();
    });


    $(document.body).on("click", "#cc_I1S1_ques1_yes", function(){

        $("#cc_I1S1_ques1").hide();
        
        $("#cc_I1S1_success").show();
    });

    $(document.body).on("click", "#cc_I1S1_ques1_no", function(){

        $("#cc_I1S1_ques1").hide();
        
        $("#cc_I1S1_fail").show();
    });


    $(document.body).on("click", "#cc_I1S1_success #restartq", function(){

        $("#cc_I1S1_success").hide();
        
        $("#cc_I1S1_ques1").show();
    });

    $(document.body).on("click", "#cc_I1S1_fail #restartq", function(){

        $("#cc_I1S1_fail").hide();
        
        $("#cc_I1S1_ques1").show();
    });
    // ce_I1S1 //


    // ce_I1S2 //
    $(document.body).on("click", "#cc_I1S2_desc_yes", function(){

        $("#cc_I1S2_desc").hide();
        $("#cc_I1S2_ques1").show();
    });


    $(document.body).on("click", "#cc_I1S2_ques1_yes", function(){

        $("#cc_I1S2_ques1").hide();
        
        $("#cc_I1S2_success").show();
    });

    $(document.body).on("click", "#cc_I1S2_ques1_no", function(){

        $("#cc_I1S2_ques1").hide();
        
        $("#cc_I1S2_fail").show();
    });


    $(document.body).on("click", "#cc_I1S2_success #restartq", function(){

        $("#cc_I1S2_success").hide();
        
        $("#cc_I1S2_ques1").show();
    });

    $(document.body).on("click", "#cc_I1S2_fail #restartq", function(){

        $("#cc_I1S2_fail").hide();
        
        $("#cc_I1S2_ques1").show();
    });
    // ce_I1S2 //


    // ce_I1S3 //
    $(document.body).on("click", "#cc_I1S3_desc_yes", function(){

        $("#cc_I1S3_desc").hide();
        $("#cc_I1S3_ques1").show();
    });


    $(document.body).on("click", "#cc_I1S3_ques1_yes", function(){

        

        if($("#section-cc input:checkbox:checked").length <7){
            $("#cc_I1S3_ques1").hide();        
            $("#cc_I1S3_fail").show();
        }
        else{

            $("#cc_I1S3_ques1").hide();
            $("#cc_I1S3_success").show();
        }

    });

    $(document.body).on("click", "#cc_I1S3_ques1_no", function(){

        
    });


    $(document.body).on("click", "#cc_I1S3_success #restartq", function(){

        $("#cc_I1S3_success").hide();
        
        $("#cc_I1S3_ques1").show();
    });

    $(document.body).on("click", "#cc_I1S3_fail #restartq", function(){

        $("#cc_I1S3_fail").hide();
        
        $("#cc_I1S3_ques1").show();
    });
    // ce_I1S2 //


    // ce_I1 Tooltip //
    $(document.body).on('mouseenter','#parent-section-ce p.intent-title',function(event) {
        $(this).popover({
            placement:'top', 
            trigger: 'hover'
        }).popover('show');
    });
    // ce_I1 Tooltip //
});