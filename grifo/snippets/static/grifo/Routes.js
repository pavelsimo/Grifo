(function() {
    angular.module('Grifo').config(function($routeProvider) {
        $routeProvider
            .when('/', {
                redirectTo: '/snippets'
            })
            .when('/snippets', {
                templateUrl: '/static/grifo/snippets/partials/index.html',
                controller:  'SnippetsController'
            })
            .when('/snippets/new', {
                templateUrl: '/static/grifo/snippets/partials/edit.html',
                controller:  'SnippetsCreateController'
            })
            .when('/snippets/:id', {
                templateUrl: '/static/grifo/snippets/partials/show.html',
                controller:  'SnippetsShowController'
            })
            .when('/snippets/:id/edit', {
                templateUrl: '/static/grifo/snippets/partials/edit.html',
                controller:  'SnippetsEditController'
            });
    });
})();