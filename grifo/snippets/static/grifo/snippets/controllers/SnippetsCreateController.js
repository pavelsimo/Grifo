(function() {

    angular.module('Grifo').controller('SnippetsCreateController', function($scope, $location, Snippet, SnippetCategory) {
        $scope.snippet = new Snippet();
        $scope.categories = SnippetCategory.query();
        $scope.isSubmitting = false;

        $scope.saveSnippet = function(snippet) {
            $scope.isSubmitting = true;
            snippet.$save().finally(function() {
                $scope.isSubmitting = false;
                $location.path('/snippets');
            });
        };

    });

})();