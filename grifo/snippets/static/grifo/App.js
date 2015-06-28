(function() {

    angular.module('Grifo', ['ngRoute', 'ngResource'])
        .config(['$interpolateProvider', function($interpolateProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
        }]);

})();

