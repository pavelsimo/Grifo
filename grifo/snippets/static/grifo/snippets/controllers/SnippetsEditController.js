(function() {

    angular.module('Grifo').controller('SnippetsEditController', function($scope, $routeParams, $location, Snippet, SnippetCategory) {
        $scope.snippet = {};
        $scope.isUpdating = false;
        $scope.categories = SnippetCategory.query();

        Snippet.get({id: $routeParams.id}, function(snippet) {
            $scope.snippet = snippet;
        });

        $scope.saveSnippet = function(snippet) {
            $scope.isUpdating = true;
            snippet.$update().finally(function() {
                $scope.isUpdating = false;
                $location.path("/snippets/" + snippet.id);
            });
        };

    });

})();