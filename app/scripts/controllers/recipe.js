'use strict';

/**
 * @ngdoc function
 * @name funtimesApp.controller:RecipeCtrl
 * @description
 * # RecipeCtrl
 * Controller of the funtimesApp
 */
angular.module('funtimesApp')
    .controller('RecipeCtrl', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
    var getRecipes = function () {
        $http.get('http://' + 'localhost:9200' + '/recipes/_search?q=_id:' + $routeParams.recipeID).
        then(function (data) {
            var results = angular.fromJson(data);
            var hits = results.data.hits.hits;
            var recipe = {};
            var hit = hits[0];
            recipe.id = hit._id;
            console.log(recipe.id);
            recipe.image = hit._source.image;
            console.log(recipe.image);
            recipe.largeImage = recipe.largeImage = '//wit.wurfl.io/w_800/h_800/m_cropbox/' + hit._source.image;
            recipe.thumbImage = '//wit.wurfl.io/w_250/h_250/m_cropbox/' + hit._source.image;
            recipe.name = hit._source.name;
            recipe.description = hit._source.description;
            recipe.servings = hit._source.servings.split('Servings:')[1];
            var ingredients = hit._source.ingredients;
            console.log(ingredients);
            var ingredientList = [];
            var flourList = [];
            for (var item in ingredients) {
                    var ingredient = {};
                    ingredient.name = item;
                    ingredient.quantity = ingredients[item].quantity;
                    ingredient.unit = ingredients[item].unit;
                    ingredient.flour = ingredients[item].flour;
                    ingredient.gluten = ingredients[item].gluten;
                    var subname = ingredients[item].substitute;
                    if (subname !== 'no substitute needed' && subname !== 'flour ratio') {
                        var substitute = {};
                        substitute.name = subname;
                        substitute.quantity = ingredients[item].quantity;
                        substitute.unit = ingredients[item].unit;
                        substitute.glutenClass = '{good: yay}';
                        substitute.hide = 'custom';
                        ingredient.substitute = substitute;
                        console.log(ingredient.substitute);
                    }
                if (ingredient.flour !== 'Safe') {
                        var normalizedUnits = {
                            'tbsp.': 1 / 16,
                            'tbsp': 1 / 16,
                            'T': 1 / 16,
                            'T.': 1 / 16,
                            'tablespoon': 1 / 16,
                            'tablespoons': 1 / 16,
                            'tbs.': 1 / 16,
                            'tbs': 1 / 16,
                            'tsp.': 1 / 48,
                            'tsp': 1 / 48,
                            't': 1 / 48,
                            't.': 1 / 48,
                            'teaspoon': 1 / 48,
                            'teaspoons': 1 / 48,
                            'cups': 1,
                            'cup': 1,
                            'c.': 1,
                            'c': 1
                        };
                        console.log(ingredient);
                        var flour = {};
                        var amounts =  ingredient.quantity.split(' ');
                        var normalizedAmount = 0;
                        for (var amount = 0; amount < amounts.length; amounts++) {
                            normalizedAmount = normalizedAmount + eval(amounts[amount]);
                        }
                        var weight = ingredient.flour.weight;
                        if (ingredient.unit in normalizedUnits) {
                            ingredient.weight = (weight * (normalizedAmount * normalizedUnits[ingredient.unit]));
                            console.log(ingredient.weight);
                        }
                        try {
                            var protein = {};
                            protein.kind = ingredient.flour.type.protein.type;
                            protein.weight = ingredient.flour.type.protein.weight * ingredient.weight;
                            if (protein.kind) {
                                flour.protein = protein;
                            }
                        } catch (e) {
                            console.log('protein not present');
                        }
                        try {
                            var fat = {};
                            fat.kind = ingredient.flour.type.fat.type;
                            fat.weight = ingredient.flour.type.fat.weight * ingredient.weight;
                            if (fat.kind) {
                                flour.fat = fat;
                            }
                        } catch (e) {
                            console.log('fat not present');
                        }
                        try {
                            var lightness = {};
                            lightness.kind = ingredient.flour.type.lightness.type;
                            lightness.weight = ingredient.flour.type.lightness.weight * ingredient.weight;
                            if (lightness.kind) {
                                flour.lightness = lightness;
                            }
                        } catch (e) {
                            console.log('lightness not present');
                        }
                        try {
                            var stickiness = {};
                            stickiness.kind = ingredient.flour.type.stickiness.type;
                            stickiness.weight = ingredient.flour.type.stickiness.weight * ingredient.weight;
                            if (stickiness.kind) {
                                flour.stickiness = stickiness;
                            }
                        } catch (e) {
                            console.log('stickiness not present');
                        }
                        try {
                            var density = {};
                            density.kind = ingredient.flour.density.type;
                            density.weight = ingredient.flour.type.density.weight * ingredient.weight;
                            if (density.kind) {
                                flour.density = density;
                            }
                        } catch (e) {
                            console.log('density not present');
                        }
                        try {
                            var texture = {};
                            texture.kind = ingredient.flour.texture.type;
                            texture.weight = ingredient.flour.type.texture.weight * ingredient.weight;
                            if (texture.kind) {
                                flour.texture = texture;
                            }
                        } catch (e) {
                            console.log('texture not present');
                        }
                        try {
                            var starch = {};
                            starch.kind = ingredient.flour.type.starch.type;
                            starch.weight = ingredient.flour.type.starch.weight * ingredient.weight;
                            if (starch.kind) {
                                flour.starch = starch;
                            }
                        } catch (e) {
                            console.log('starch not present');
                        }
                        try {
                            var binder = {};
                            binder.kind = ingredient.flour.type.binder.type;
                            binder.amount = ingredient.flour.type.binder.weight * (normalizedAmount * normalizedUnits[ingredient.unit]);
                            console.log(binder.amount);
                            if (binder.amount > 1) {
                                binder.unit = 'teaspoons';
                            } else {
                                binder.unit = 'teaspoon';
                            }
                            if (binder.kind) {
                                flour.binder = binder;
                            }
                        } catch (e) {
                            console.log('binder not present');
                        }
                        try {
                            var leavener = {};
                            leavener.kind = ingredient.flour.leavener.type;
                            leavener.amount = ingredient.flour.type.leavener.weight * (normalizedAmount * normalizedUnits[ingredient.unit]);
                            if (leavener.amount > 1) {
                                leavener.unit = 'teaspoons';
                            } else {
                                leavener.unit = 'teaspoon';
                            }
                            if (leavener.kind) {
                                flour.leavener = leavener;
                            }
                        } catch (e) {
                            console.log('leavener not present');
                        }
                        flour.glutenClass = '{good: yay}';
                        flour.hide = 'notVisible';
                        if (flour !== {}) {
                            flour.hide = 'custom';
                            flourList.push(flour);
                        }
                    }
                    if (ingredient.name) {
                        ingredientList.push(ingredient);
                    }
                }
                   for (var g = 0; g < ingredientList.length; g++) {
                    if (ingredientList[g].gluten === 'gluten here!') {
                        ingredientList[g].glutenClass = '{gluten: warning}';
                        ingredientList[g].show = 'custom';
                    } else {
                        ingredientList[g].glutenClass = '{neutral: safe}';
                        ingredientList[g].show = 'aOkay';
                    }
                }
                for (var mes = 0; mes < ingredientList.length; mes++) {
                    if (ingredientList[mes].gluten === 'gluten here!') {
                        $scope.dataContent =  'Canary found gluten in this recipe! Click "Swap!" to remove it.';
                        break;                                  
                    } else {
                         $scope.dataContent = 'Canary is singing! There is no gluten in this recipe.';
                    }
                }
                var instructions = hit._source.instructions;
                recipe.calories = hit._source.calories;
                recipe.fatContent = hit._source.fatContent;
                recipe.saturatedFatContent = hit._source.saturatedFatContent;
                recipe.cholesterolConent = hit._source.cholesterolConent;
                recipe.sodiumContent = hit._source.sodiumContent;
                recipe.carbohydrateContent = hit._source.carbohydrateContent;
                recipe.fiberContent = hit._source.fiberContent;
                recipe.sugarContent = hit._source.sugarContent;
                recipe.proteinContent = hit._source.proteinContent;
                recipe.keywords = hit._source.keywords;
                recipe.url = hit._source.url;
                $scope.recipe = recipe;
                if (flourList.length > 0) {
                    $scope.flours = flourList;
                }
                $scope.ingredients = ingredientList;
                $scope.instructions = instructions;
                $scope.custom = true;
                $scope.notVisible = true;
                $scope.aOkay = true;
                $scope.toggleCustom = function() {
                    $scope.custom = $scope.custom === false ? true : false;
                };
            });
        };
        $scope.isCollapsed = false;
        $scope.searchTerm = '';
        $scope.$watch('searchTerm', getRecipes, true);
    }]);