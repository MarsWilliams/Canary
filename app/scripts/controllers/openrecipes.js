'use strict';

/**
 * @ngdoc function
 * @name funtimesApp.controller:OpenrecipesCtrl
 * @description
 * # OpenrecipesCtrl
 * Controller of the funtimesApp
 */
angular.module('funtimesApp')
  .controller('OpenrecipesCtrl', function($scope, $http) {
        var getRecipes = function(searchTerm) {
            if (searchTerm === '') {
                searchTerm = 'peaches gluten-free';
            }
            $http.get('http://' + 'localhost:9200' + '/openrecipes/_search?q=' + searchTerm).
            then(function(data) {
                var results = angular.fromJson(data);
                var hits = results.data.hits.hits;
                var openRecipes = [];
                var recipeImages = ['hello'];
                for (var i = 0; i < hits.length; i++) {
                    var recipe = {};
                    var hit = hits[i];
                    console.log(hit);
                    recipe.id = hit._id;
                    var image = hit._source.image;
                    if (recipeImages.indexOf(image) === -1) {
                        recipeImages.push(image);
                        recipe.image = image;
                        recipe.largeImage = '//wit.wurfl.io/w_1500/h_1500/m_cropbox/' + hit._source.image;
                        recipe.thumbImage = '//wit.wurfl.io/w_250/h_250/m_cropbox/' + hit._source.image;
                        recipe.name = hit._source.name;
                        recipe.description = hit._source.description;
                        recipe.servings = hit._source.recipeYield;
                        recipe.ingredients = hit._source.ingredients;
                        recipe.source = hit._source.source;
                        recipe.url = hit._source.url;

                        if (recipe.image !== '') {
                            openRecipes.push(recipe);
                        }
                    }
                }
                $scope.openRecipes = openRecipes;

            });
        };
        $scope.isCollapsed = false;
        $scope.searchTerm = '';
        $scope.$watch('searchTerm', getRecipes, true);
        $scope.colors = ['red lighten-5', 'red lighten-4', 'blue lighten-5', 'blue lighten-4', 'light-green lighten-5', 'light-green lighten-4', 'deep-orange lighten-5', 'deep-orange lighten-4'];
        console.log($scope.colors);
    });