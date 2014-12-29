'use strict';

describe('Controller: YummlyCtrl', function () {

  // load the controller's module
  beforeEach(module('funtimesApp'));

  var YummlyCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    YummlyCtrl = $controller('YummlyCtrl', {
      $scope: scope
    });
  }));
});
