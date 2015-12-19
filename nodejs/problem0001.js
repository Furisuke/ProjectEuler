var _ = require('lodash');

var answer = _(_.range(1, 1000))
  .filter(function(n) {
    return (n % 3 == 0) || (n % 5 == 0);
  })
  .sum();

console.log(answer);
