var app = angular.module('peer-app', []);

app.directive("rrCategory", function(){
    return{
        restrict:'E',
        templateUrl:'partials/section-rr.html'
    };
});

app.directive("eeCategory", function(){
    return{
        restrict:'E',
        templateUrl:'partials/section-ee.html'
    };
});

app.directive("ceCategory", function(){
    return{
        restrict:'E',
        templateUrl:'partials/section-cc.html'
    };
});

app.directive("dtCategory", function(){
    return{
        restrict:'E',
        templateUrl:'partials/section-dt.html'
    };
});


