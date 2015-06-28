(function() {

    angular.module('Grifo').factory('Snippet', function SnippetFactory($resource) {
        return $resource('/api/v1/snippets/:id', {id: '@id'}, {
            'update': {method: 'PUT'}
        });
    });

})();