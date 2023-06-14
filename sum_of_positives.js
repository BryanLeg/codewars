// You get an array of numbers, return the sum of all of the positives ones.

// Example [1,-4,7,12] => 1 + 7 + 12 = 20

// Note: if there is nothing to sum, the sum is default to 0.

const arr = [1, -4, 7, 12];

function positiveSum(arr) {
  const sumPosValues = arr.reduce(
    (prevValue, currentValue) =>
      currentValue > 0 ? prevValue + currentValue : prevValue,
    0
  );
  return sumPosValues;
}

console.log(positiveSum(arr));
