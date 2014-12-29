'use strict';

/**
 * @ngdoc overview
 * @name funtimesApp
 * @description
 * # funtimesApp
 *
 * Main module of the application.
 */
angular
  .module('funtimesApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'SearchCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .when('/recipedetail/:recipeID', {
        templateUrl: 'views/recipe.html',
        controller: 'RecipeCtrl'
      })
      .when('/yummly', {
        templateUrl: 'views/yummly.html',
        controller: 'YummlyCtrl'
      })
      .when('/use strict', {
        templateUrl: 'views/use strict.html',
        controller: 'UseStrictCtrl'
      })
      .when('/openrecipes', {
        templateUrl: 'views/openrecipes.html',
        controller: 'OpenrecipesCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
