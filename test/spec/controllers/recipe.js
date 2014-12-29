'use strict';

describe('Controller: RecipeCtrl', function () {

  // load the controller's module
  beforeEach(module('funtimesApp'));

  var RecipeCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    RecipeCtrl = $controller('RecipeCtrl', {
      $scope: scope
    });
  }));
});
