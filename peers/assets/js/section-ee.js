
$(document).ready(function(){                                       
    

    var x1 = "";
    var x2 = "";

    var x3 = "";
    var x4 = "";
    var x5 = "";
    var x6 = "";

    var per="";

    // ee_I1S1 //
    $(document.body).on("click", "#ee_I1S1_desc_yes", function(){

        $("#ee_I1S1_desc").hide();
        $("#ee_I1S1_ques1").show();
    })
    

    $(document.body).on("click", "#ee_I1S1_ques1_yes", function(){

        $("#ee_I1S1_ques1").hide();
        
        $("#ee_I1S1_ques2").show();

        x1 = $("#x1").val();
        x2 = $("#x2").val();
    })

    $(document.body).on("click", "#ee_I1S1_ques1_no", function(){

        $("#ee_I1S1_ques1").hide();
        
        $("#ee_I1S1_fail").show();
    })

    $(document.body).on("click", "#ee_I1S1_ques2 #continueq", function(){

        x3 = $("#x3").val();
        x4 = $("#x4").val();
        x5 = $("#x5").val();
        x6 = $("#x6").val();

        per = (((x3+x4+x5+x6)/(x1+x2))*100).toFixed(2);

        if(isNaN(per)){
            per = 0;
        }

        $("#per").html(per+" %");

        if(per>5){
            $("#project_total_points").html("<b>"+2+"</b>/2");
        }

        if(per>0 && per<=5){
            $("#project_total_points").html("<b>"+1+"</b>/2");
        }


        $("#ee_I1S1_ques2").hide();        
        $("#ee_I1S1_success").show();        

        console.log(per);
    })

    $(document.body).on("click", "#ee_I1S1_ques2 #restartq", function(){

        $("#ee_I1S1_ques2").hide();
        
        $("#ee_I1S1_ques1").show();
    })

    $(document.body).on("click", "#ee_I1S1_success #restartq", function(){

        $("#ee_I1S1_success").hide();
        
        $("#ee_I1S1_ques2").show();
    })

    $(document.body).on("click", "#ee_I1S1_fail #restartq", function(){

        $("#ee_I1S1_fail").hide();
        
        $("#ee_I1S1_ques1").show();
    })
    // ee_I1S1 //

    $(document.body).on("click",'#ee_I2S1_desc_yes',function() {
        $('#ee_I2S1_desc').hide();
        $('#ee_I2S1_ques1').show();
    });
    
    $(document.body).on("click",'#ee_I1S1_ques1_yes',function() {
        $('#ee_I2S1_ques1').hide();
        $('#ee_I2S1_ques2').show();
    });

    $(document.body).on("click",'#ee_I1S1_ques1_no',function() {
         $('#ee_I2S1_ques1').hide();
         $('#ee_I2S1_fail').show();
    });


    $(document.body).on('click','#ee_I2S1_ques1 #continueq',function() {
        $('#ee_I2S1_ques1').hide();
        $('#ee_I2S1_ques2').show();
    });

    $(document.body).on('click','#ee_I2S1_ques1 #restartq',function() {
        $('#ee_I2S1_ques1').hide();
        $('#ee_I2S1_desc').show();
    });

    $(document.body).on('click','#ee_I2S1_ques2 #continueq',function() {
        $('#ee_I2S1_ques2').hide();
        $('#ee_I2S1_ques3').show();
    });

    $(document.body).on('click','#ee_I2S1_ques2 #restartq',function() {
        $('#ee_I2S1_ques2').hide();
        $('#ee_I2S1_ques1').show();
    });

    $(document.body).on('click','#ee_I2S1_ques3 #continueq',function() {

    });

    $(document.body).on('click','#ee_I2S1_ques3 #restartq',function() {
        
    });

});
