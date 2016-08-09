
$(document).ready(function(){
                                    
    $(document.body).on('click','.parent-accordion-section-title', function(e) {
    // Grab current anchor value
        var currentAttrValue = $(this).attr('data-href');

        if($(this).hasClass('active')) {
            $(this).removeClass('active');
            $(this).siblings('.parent-accordion-section-content').slideUp(300).removeClass('open');
            //plaque.elements.close_parent_accordion_section();
        }else {
            //plaque.elements.close_parent_accordion_section();

            // Add active class to section title
            $(this).addClass('active');
            $(this).find('span.ui-accordion-header-icon').addClass('expanded');
            // Open up the hidden content panel
            $('.accordion ' + currentAttrValue).slideDown(300).addClass('open'); 
        }

        e.preventDefault();
    });

    $(document.body).off("click", ".accordion-section-title").on("click", ".accordion-section-title", function(e){

        intentId = $(this).data("intentid");
        var strategyListDiv = $("#index-banner-"+intentId);
        //  console.log($("#index-banner-"+intentId+" > ul > li").length);
        var currentAttrValue = $(this).attr('data-href');
                 
        if($(this).hasClass('active')) {
            $(this).removeClass('active');
            $(this).siblings('.accordion-section-content').slideUp(300).removeClass('open');
            //plaque.elements.close_accordion_section();
            $(this).find('i').removeClass().addClass("arrow-down");                         
        }else {
            // Add active class to section title
            if($("#index-banner-"+intentId+" > ul > li").length < 1
                || $("#index-banner-"+intentId+" > ul > li.new-custom-added").length > 0){
                var categoryParentId = $(this).parents(".cataegory-div").attr("id");
            }
            
            $(this).addClass('active');
            $(this).find('span.ui-accordion-header-icon').addClass('expanded');
            // Open up the hidden content panel
            $('.accordion ' + currentAttrValue).slideDown(300).addClass('open');
            $(this).find('i').removeClass().addClass("arrow-up");
        }                 
        e.preventDefault();     
    });

    // hover div functionality
        $(document.body).on('mouseenter','div.collapsible-header', function (event) {
            if($('.multiCheckStrategyXYZ').is(':checked')){
                $('.hover-apply-strategy').hide();
            }else{
                if($(this).hasClass('active')){ //|| $(this).parent('li').hasClass('attempted')
                    $(this).children('.hover-apply-strategy').hide();
                    $(this).children('.hover-select-strategy').hide();
                }else{
                    var height = $(this).parent('li').height();
                    $(this).css('position', 'relative');
                    $(this).children('.hover-apply-strategy').css('height', height);
                    $(this).children('.hover-select-strategy').css('height', height);
                    $(this).children('.hover-apply-strategy').show();
                    $(this).children('.hover-select-strategy').show();
                    $(this).children('.hover-apply-strategy').find('.applyStrategy').show();
                    $(this).children('.hover-apply-strategy').find('.notApplyStrategy').show();
                    $(this).children('.hover-apply-strategy').find('.documentStrategy').show();
                    $(this).children('.hover-apply-strategy').find('.starStrategy').show();
                }
                $('div.intent-div').popover('hide');
                $(this).popover({
                    placement:'top', 
                    trigger: 'hover'
                }).popover('show');
            }
        }).on('mouseleave','div.collapsible-header',  function(){
            //$(this).css('position','');
            //$(this).children('.hover-apply-strategy').hide();
            if($(this).children('.hover-apply-strategy').find('.documentStrategy').hasClass('documented')){
                $(this).children('.hover-apply-strategy').find('.documentStrategy').show();
            }else{
                $(this).children('.hover-apply-strategy').find('.documentStrategy').hide();
            }
            if($(this).children('.hover-apply-strategy').find('.applyStrategy').hasClass('applied')){
                //$(this).children('.hover-apply-strategy').find('.applyStrategy').show();
            }else{
                //$(this).children('.hover-apply-strategy').find('.applyStrategy').hide();
            }
            $(this).children('.hover-apply-strategy').find('.applyStrategy').hide();
            $(this).children('.hover-apply-strategy').find('.notApplyStrategy').hide();
            if($(this).children('.hover-apply-strategy').find('.starStrategy').hasClass('favorite')){
                $(this).children('.hover-apply-strategy').find('.starStrategy').show();
            }else{
                $(this).children('.hover-apply-strategy').find('.starStrategy').hide();
            }
            if(!$('.multiCheckStrategyXYZ').is(':checked')){
                $(this).children('.hover-select-strategy').hide();
            }
        });
    // hover div functionality
        
       
    // strategy pop up window
    $(document.body).on('click','div.collapsible-header', function (e) {
        e.stopPropagation();
       /* if($(this).find('span.yes-apply-circle').hasClass('active') && ($(this).hasClass('active')))
            $(this).find('span.yes-apply-circle').removeClass('active');*/
    });
    
    $('.collapsible').collapsible({
        accordion : true
    });
    // strategy pop up window

    $(document.body).on("click", ".back-to-desc", function(){

        $(this).parents(".questionnaire").siblings(".strategy-not-applicable").show();
        $(this).parents(".questionnaire").hide();

    })


 // success screen -  Click on SKIP starts
    $(document.body).on('click', '.strategy-success #continueq', function(event) {

        var object =$(this).closest('.collapsible');
        $panel_headers = object.find('> li > .collapsible-header');

        if (object.hasClass('active')) {
            object.parent().addClass('active');
        }
        else {
            object.parent().removeClass('active');
        }
        if (object.parent().hasClass('active')){
            //$(this).siblings('.hover-apply-strategy').hide();
            //$(this).siblings('.hover-select-strategy').hide();
            object.siblings('.collapsible-body').stop(true,false).slideDown({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
        }
        else{
          object.siblings('.collapsible-body').stop(true,false).slideUp({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
        }
        object.find('.strategy-action-menu').show();
        $panel_headers.not(object).removeClass('active').parent().removeClass('active');
        $panel_headers.not(object).parent().children('.collapsible-body').stop(true,false).slideUp(
          {
            duration: 350,
            easing: "easeOutQuart",
            queue: false,
            complete:
              function() {
                $(this).css('height', '');
              }
          });
        
    });

    // success screen -  Click on SKIP ends

    // close-popout
    $(document.body).on('click', '.strategy-not-applicable .close-popout', function(event) {
        
        if($(this).attr('id') != 'rr_I1S1_desc_no'){
            var object =$(this).closest('.collapsible');
            $panel_headers = object.find('> li > .collapsible-header');
            $($panel_headers).find('span.yes-apply-circle').removeClass('active');
            if (object.hasClass('active')) {
                object.parent().addClass('active');
            }
            else {
                object.parent().removeClass('active');
            }
            if (object.parent().hasClass('active')){
                //$(this).siblings('.hover-apply-strategy').hide();
                //$(this).siblings('.hover-select-strategy').hide();
                object.siblings('.collapsible-body').stop(true,false).slideDown({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
            }
            else{
              object.siblings('.collapsible-body').stop(true,false).slideUp({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
            }
            object.find('.strategy-action-menu').show();
            $panel_headers.not(object).removeClass('active').parent().removeClass('active');
            $panel_headers.not(object).parent().children('.collapsible-body').stop(true,false).slideUp(
              {
                duration: 350,
                easing: "easeOutQuart",
                queue: false,
                complete:
                  function() {
                    $(this).css('height', '');
                  }
              });
        }
        else{
            $('#rr_I1S1_desc').hide();
            $('#rr_I1S1_fail').show();
        }
        
    });
    // close-popout

    // close-popout on fail screen
    $(document.body).on('click', '.strategy-fail #continueq', function(event) {

        var object =$(this).closest('.collapsible');
        $panel_headers = object.find('> li > .collapsible-header');

        if (object.hasClass('active')) {
            object.parent().addClass('active');
        }
        else {
            object.parent().removeClass('active');
        }
        if (object.parent().hasClass('active')){
            //$(this).siblings('.hover-apply-strategy').hide();
            //$(this).siblings('.hover-select-strategy').hide();
            object.siblings('.collapsible-body').stop(true,false).slideDown({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
        }
        else{
          object.siblings('.collapsible-body').stop(true,false).slideUp({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
        }
        object.find('.strategy-action-menu').show();
        $panel_headers.not(object).removeClass('active').parent().removeClass('active');
        $panel_headers.not(object).parent().children('.collapsible-body').stop(true,false).slideUp(
          {
            duration: 350,
            easing: "easeOutQuart",
            queue: false,
            complete:
              function() {
                $(this).css('height', '');
              }
          });
        
    });
    // close-popout on fail screen

    // close-popout on success screen
    $(document.body).on('click', '.complete-credit #completeq', function(event) {

        var object =$(this).closest('.collapsible');
        $panel_headers = object.find('> li > .collapsible-header');

        if (object.hasClass('active')) {
            object.parent().addClass('active');
        }
        else {
            object.parent().removeClass('active');
        }
        if (object.parent().hasClass('active')){
            //$(this).siblings('.hover-apply-strategy').hide();
            //$(this).siblings('.hover-select-strategy').hide();
            object.siblings('.collapsible-body').stop(true,false).slideDown({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
        }
        else{
          object.siblings('.collapsible-body').stop(true,false).slideUp({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
        }
        object.find('.strategy-action-menu').show();
        $panel_headers.not(object).removeClass('active').parent().removeClass('active');
        $panel_headers.not(object).parent().children('.collapsible-body').stop(true,false).slideUp(
          {
            duration: 350,
            easing: "easeOutQuart",
            queue: false,
            complete:
              function() {
                $(this).css('height', '');
              }
          });
        
    });
    // close-popout on success screen

    // success screen -  Click on Next Strategy starts
    $(document.body).off('click', '.strategy-success #next-strategy').on('click', '.strategy-success #next-strategy', function(event) {
        $(this).closest('li').next().find('.collapsible-header').click();                          
    });
    // success screen -  Click on Next Strategy ends
    

    $(document.body).on('click','.applyStrategy .yes-apply-circle',function() {
       var intentid = $(this).parent().data('intentid');
       var style    = intentid+'-active';
       var headerStyle = intentid+'-strategy-applicable'
        if($(this).hasClass(style)) {
            $(this).removeClass(style);
            $(this).closest('div.collapsible-header').removeClass(headerStyle);
            $(this).closest('div.collapsible-header').siblings('.collapsible-body').find('div.questionnaire').hide();
            $(this).closest('div.collapsible-header').siblings('.collapsible-body').find('div.strategy-not-applicable').show();
            
        } else{
            $(this).addClass(style);
            $(this).closest('div.collapsible-header').addClass(headerStyle);
            $('div.strategy-not-applicable .button-group .yes').trigger('click');
        }
        $(this).closest('li.strategy-system').addClass('active');
        $(this).closest('div.collapsible-header').siblings('.collapsible-body').stop(true,false).slideDown({ duration: 350, easing: "easeOutQuart", queue: false, complete: function() {$(this).css('height', '');}});
    });
});
