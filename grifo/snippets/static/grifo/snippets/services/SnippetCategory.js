(function() {

    angular.module('Grifo').factory('SnippetCategory', function SnippetCategoryFactory($resource) {
        return $resource('/api/v1/categories/:id', {}, {});
    });

})();