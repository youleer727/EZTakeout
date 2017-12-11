'use strict';

angular.module('ezTakeoutApp').controller('IndexCtrl', function MainCtrl($scope) {
  var time_val = $scope.time_val;
  var cost_val = $scope.cost_val;
  var foodtype_val = $scope.foodtype_val;
  var baseUrl = '/#!/';
  $scope.selectedItem = 'pizza';
  $scope.select = function(container) {
        $scope.selectedItem = container;
    };
  $scope.redirectUrl = function() {
        // return $scope.data.message.split("").reverse().join("");
      return baseUrl + 'map?' + 'type=' + $scope.selectedItem + '&time=' + $scope.time_val + '&cost=' + $scope.cost_val;
    };
});
