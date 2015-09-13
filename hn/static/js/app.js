var news = angular.module("news", ["newsServices"]).config(function(
            $interpolateProvider, $httpProvider) {

    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");


    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});
