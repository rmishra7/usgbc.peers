
$(document).ready(function(){                                       
    

    // dt_I1S1 //
    $(document.body).on("click", "#dt_I1S1_desc_yes", function(){

        $("#dt_I1S1_desc").hide();
        $("#dt_I1S1_ques1").show();
    })
    

    $(document.body).on("click", "#dt_I1S1_ques1_yes", function(){

        $("#dt_I1S1_ques1").hide();
        
        $("#dt_I1S1_ques3").show();
    })

    $(document.body).on("click", "#dt_I1S1_ques1_no", function(){

        $("#dt_I1S1_ques1").hide();
        
        $("#dt_I1S1_fail").show();
    })

    $(document.body).on("click", "#dt_I1S1_ques2 #continueq", function(){

        $("#dt_I1S1_ques2").hide();
        
        $("#dt_I1S1_success").show();
    })

    $(document.body).on("click", "#dt_I1S1_ques3 #continueq", function(){
        $("#dt_I1S1_ques3").hide();

        $("#dt_I1S1_ques2").show();
    })

    $(document.body).on("click", "#dt_I1S1_ques3 #restartq", function(){
        $("#dt_I1S1_ques3").hide();

        $("#dt_I1S1_ques1").show();
    })

    //link to second strategy.    
    $(document.body).on('click','#dt_I1S1_fail #continueq',function() {
       $('#next-strategy').trigger('click');
    });

    $(document.body).on("click", "#dt_I1S1_ques2 #restartq", function(){

        $("#dt_I1S1_ques2").hide();
        
        $("#dt_I1S1_ques3").show();
    })

    $(document.body).on("click", "#dt_I1S1_success #restartq", function(){

        $("#dt_I1S1_success").hide();
        
        $("#dt_I1S1_ques2").show();
    })

    $(document.body).on("click", "#dt_I1S1_fail #restartq", function(){

        $("#dt_I1S1_fail").hide();
        
        $("#dt_I1S1_ques1").show();
    })
    // dt_I1S1 //


    

    // dt_I1S2 //

    $(document.body).on("click", "#dt_I1S2_desc_yes", function(){

        $("#dt_I1S2_desc").hide();
        $("#dt_I1S2_ques1").show();
    })

    

    $(document.body).on("click", "#dt_I1S2_ques1_yes", function(){

        $("#dt_I1S2_ques1").hide();
        
        $("#dt_I1S2_success").show();
    })

    $(document.body).on("click", "#dt_I1S2_ques1_no", function(){

        $("#dt_I1S2_ques1").hide();
        
        $("#dt_I1S2_fail").show();
    })
    

    $(document.body).on("click", "#dt_I1S2_success #restartq", function(){

        $("#dt_I1S2_success").hide();
        
        $("#dt_I1S2_ques1").show();
    })

    $(document.body).on("click", "#dt_I1S2_fail #restartq", function(){

        $("#dt_I1S2_fail").hide();
        
        $("#dt_I1S2_ques1").show();
    })

    // dt_I1S2 //



    // dt_I1S3 //

    $(document.body).on("click", "#dt_I1S3_desc_yes", function(){

        $("#dt_I1S3_desc").hide();
        $("#dt_I1S3_ques1").show();
    })    

    $(document.body).on("click", "#dt_I1S3_ques1_yes", function(){

        $("#dt_I1S3_ques1").hide();
        
        $("#dt_I1S3_success").show();
    })

    $(document.body).on("click", "#dt_I1S3_ques1_no", function(){

        $("#dt_I1S3_ques1").hide();
        
        $("#dt_I1S3_fail").show();
    })
    

    $(document.body).on("click", "#dt_I1S3_success #restartq", function(){

        $("#dt_I1S3_success").hide();
        
        $("#dt_I1S3_ques1").show();
    })

    $(document.body).on("click", "#dt_I1S3_fail #restartq", function(){

        $("#dt_I1S3_fail").hide();
        
        $("#dt_I1S3_ques1").show();
    })

    // dt_I1S3 //


    // dt_I1S4 //

    $(document.body).on("click", "#dt_I1S4_desc_yes", function(){

        $("#dt_I1S4_desc").hide();
        $("#dt_I1S4_ques1").show();
    })

    

    $(document.body).on("click", "#dt_I1S4_ques1_yes", function(){

        $("#dt_I1S4_ques1").hide();
        
        $("#dt_I1S4_success").show();
    })

    $(document.body).on("click", "#dt_I1S4_ques1_no", function(){

        $("#dt_I1S4_ques1").hide();
        
        $("#dt_I1S4_fail").show();
    })
    

    $(document.body).on("click", "#dt_I1S4_success #restartq", function(){

        $("#dt_I1S4_success").hide();
        
        $("#dt_I1S4_ques1").show();
    })

    $(document.body).on("click", "#dt_I1S4_fail #restartq", function(){

        $("#dt_I1S4_fail").hide();
        
        $("#dt_I1S4_ques1").show();
    })

    // dt_I1S4 //


    // dt_I1S5 //

    $(document.body).on("click", "#dt_I1S5_desc_yes", function(){

        $("#dt_I1S5_desc").hide();
        $("#dt_I1S5_ques1").show();
    })
    

    $(document.body).on("click", "#dt_I1S5_ques1_yes", function(){

        if($("#section-dt input:checkbox:checked").length <7){
            $("#dt_I1S5_ques1").hide();        
            $("#dt_I1S5_fail").show();
        }
        else{

            $("#dt_I1S5_ques1").hide();
            $("#dt_I1S5_success").show();
        }
    })

    $(document.body).on("click", "#dt_I1S5_ques1_no", function(){

        $("#dt_I1S5_ques1").hide();
        
        $("#dt_I1S5_fail").show();
    })
    

    $(document.body).on("click", "#dt_I1S5_success #restartq", function(){

        $("#dt_I1S5_success").hide();
        
        $("#dt_I1S5_ques1").show();
    })

    $(document.body).on("click", "#dt_I1S5_fail #restartq", function(){

        $("#dt_I1S5_fail").hide();
        
        $("#dt_I1S5_ques1").show();
    })

    // dt_I1S5 //
    
});
