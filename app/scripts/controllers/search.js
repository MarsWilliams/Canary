'use strict';

/**
 * @ngdoc function
 * @name funtimesApp.controller:SearchCtrl
 * @description
 * # SearchCtrl
 * Controller of the funtimesApp
 */
angular.module('funtimesApp')
    .controller('SearchCtrl', function($scope, $http) {
        var getRecipes = function(searchTerm) {
            console.log('the search controller was called');
            if (searchTerm === '') {
                searchTerm = 'pie';
            }
            $http.get('http://' + 'localhost:9200' + '/recipes/_search?q=' + searchTerm).
            then(function(data) {
                var results = angular.fromJson(data);
                var hits = results.data.hits.hits;
                var recipes = [];
                var recipeImages = ['hello'];
                for (var i = 0; i < hits.length; i++) {
                    var recipe = {};
                    var hit = hits[i];
                    recipe.id = hit._id;
                    var image = hit._source.image;
                    if (recipeImages.indexOf(image) === -1) {
                        recipeImages.push(image);
                        recipe.image = image;
                        recipe.largeImage = '//wit.wurfl.io/w_600/h_600/m_cropbox/' + hit._source.image;
                        recipe.thumbImage = '//wit.wurfl.io/w_500/h_400/m_cropbox/' + hit._source.image;
                        recipe.name = hit._source.name;
                        recipe.url = hit._source.url;
                        if (recipe.image !== '') {
                            recipes.push(recipe);
                        }

                    }
                }
                $scope.recipes = recipes;

            });

        };

        $scope.searchTerm = '';
        $scope.$watch('searchTerm', getRecipes, true);
    });