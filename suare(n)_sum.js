// Complete the square sum function so that it squares each number passed into it and then sums the results together.

// For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.

function squareSum(numbers) {
  const sumSquares = numbers.reduce(
    (prevValue, currentValue) => prevValue + Math.pow(currentValue, 2),
    0
  );
  return sumSquares;
}

console.log(squareSum([1, 2, 2]));
