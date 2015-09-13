function newsCtrl($scope, $rootScope, articleService) {



    $scope.getResourceObject = function() {
        var article = articleService.get({},
            function(data) {
                $scope.articles = data.objects;

            }
        );
        return article.$promise;
    };

     $scope.markRead = function(article) {
        articleService.update_log({
            id: article.id
        }, { action: 1 },
        function() {
            article.is_read = true;
        });
           $scope.getResourceObject();
    };

    $scope.markDeleted = function(article) {
    	articleService.update_log({
    		id: article.id
    	}, {action:2},
    	function() {
    		article.is_deleted= true

    	});
        $scope.getResourceObject();
    }


    $scope.getResourceObject();

}



function RegisterCtrl($scope, $window, newsHttpService) {

    $scope.apiUrl = "/api/v1/registration\\/";
    $scope.user = {
        "first_name": "",
        "last_name": "",
        "email": "",
        "password": "",
    };

    $scope.createUser = function() {
        newsHttpService.post($scope, $scope.user);
        return false;
    };

    $scope.postSuccessCallback = function() {
        window._vis_opt_queue = window._vis_opt_queue || [];
        window._vis_opt_queue.push(function() {_vis_opt_goal_conversion(201);});
        $window.location = "/dashboard/";
    };
}



function loginCtrl($scope, $window, newsHttpService) {

    $scope.apiUrl = "/api/v1/login\\/";
    $scope.user = {
        "email": "",
        "password": "",
    };

    $scope.loginUser = function() {
        newsHttpService.post($scope, $scope.user);
        return false;
    };


    $scope.postSuccessCallback = function(data) {

        var nextUrl = getNextUrl($window.location.search);

        if (nextUrl) {
            $window.location = nextUrl + window.location.hash;
        } else {
            $window.location = data.nextUrl;
        }
    };
}
