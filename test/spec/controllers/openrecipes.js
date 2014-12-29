'use strict';

describe('Controller: OpenrecipesCtrl', function () {

  // load the controller's module
  beforeEach(module('funtimesApp'));

  var OpenrecipesCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    OpenrecipesCtrl = $controller('OpenrecipesCtrl', {
      $scope: scope
    });
  }));
});
