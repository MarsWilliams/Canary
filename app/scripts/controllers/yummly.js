'use strict';

/**
 * @ngdoc function
 * @name funtimesApp.controller:YummlyCtrl
 * @description
 * # YummlyCtrl
 * Controller of the funtimesApp
 */
angular.module('funtimesApp')
  .controller('YummlyCtrl', function ($scope, $http) {
  	var getRecipes = function(searchTerm) {
     if (searchTerm === '') {
        searchTerm = 'peaches';
    }
    $http.get('http://api.yummly.com/v1/api/recipes?_app_id=b3046620&_app_key=8d80241c736a05dc77df52f886388210&allowedAllergy[]=393^Gluten-Free&requirePictures=True&q=' + searchTerm).
    then(function(data) { 
             var results = angular.fromJson(data);
             console.log(data);
             var hits = results.data.matches;
             var yummlyRecipes = [];
             for (var i = 0; i < hits.length; i++) {
                var recipe = {};
                var hit = hits[i];
               	var imageUrl = hit.smallImageUrls[0];
               	var index = imageUrl.indexOf('=');
				recipe.image = imageUrl.slice(0, index);
                recipe.id = hit.id;
               	recipe.url = 'http://www.yummly.com/recipe/' + recipe.id;
                console.log(recipe.url);
                recipe.name = hit.recipeName;
                recipe.ingredients = hit.ingredients;
                recipe.largeImage = '//wit.wurfl.io/w_500/h_500/m_cropbox/' + recipe.image;
                recipe.thumbImage = '//wit.wurfl.io/w_500/h_400/m_cropbox/' + recipe.image;
                
                if (recipe.image !== '') {
                    yummlyRecipes.push(recipe);
                }
             }
             $scope.yummlyRecipes = yummlyRecipes;

        });
    };
	$scope.searchTerm = '';
    $scope.$watch('searchTerm', getRecipes, true);
});