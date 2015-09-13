angular.module("newsServices", ["ngResource"])

    .config(function($httpProvider) {
        $httpProvider.defaults.headers.post["Content-Type"] = "application/json;";
    })

    .factory("newsHttpService", function($resource) {
        var service = {
            "post" :function(scope, data) {
                var post = $resource(scope.apiUrl, {}, {
                    "post" : {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        }
                    }

                });
                post.post(data, function(data, code) {
                    scope.postSuccessCallback(data, code);
                }, function(data) {
                    appendFieldErrors(data.data, scope);
                });
            }
        };

        return service;
    })


    .factory("articleService", function($resource) {
        var url = "/api/v1/news/:id",
            articles = $resource(url, {
                id: "@id"
            }, {
                update: {
                    method: "PUT"
                },
                update_log: {
                    url: url + "/update_log/",
                    method:"POST",
                }

            });

        return articles;
    })
