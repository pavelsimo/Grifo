(function() {

    angular.module('Grifo', ['ngRoute', 'ngResource'])
        .config(['$interpolateProvider', '$httpProvider', '$resourceProvider',
            function($interpolateProvider, $httpProvider, $resourceProvider) {
                $interpolateProvider.startSymbol('{$');
                $interpolateProvider.endSymbol('$}');
                $httpProvider.defaults.xsrfCookieName = 'csrftoken';
                $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
                $httpProvider.defaults.stripTrailingSlashes = false;
                $resourceProvider.defaults.stripTrailingSlashes = false;
            }]);
})();

