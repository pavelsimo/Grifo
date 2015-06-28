(function() {

    angular.module('Grifo').controller('SnippetsShowController', function($scope, $routeParams, $location, Snippet) {
        $scope.snippet = {};
        $scope.isDeleting = false;

        Snippet.get({id: $routeParams.id}, function(snippet) {
            $scope.snippet = snippet;
        });

        $scope.deleteSnippet = function(snippet) {
            $scope.isDeleting = true;
            snippet.$remove()
            .then(function() {
                $location.path('/snippets');
            })
            .finally(function() {
                $scope.isDeleting = false;
            });
        };
    });

})();