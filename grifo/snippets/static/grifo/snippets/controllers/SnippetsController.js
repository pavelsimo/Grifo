(function() {

    angular.module('Grifo').controller('SnippetsController', function($scope, Snippet) {
        $scope.snippets = Snippet.query();
    });

})();