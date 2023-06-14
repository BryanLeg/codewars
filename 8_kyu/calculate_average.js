// Write a function which calculates the average of the numbers in a given list.

// Note: Empty arrays should return 0.

function findAverage(array) {
  sumArray = array.reduce((prevVal, currVal) => prevVal + currVal, 0);

  return array.length > 0 ? sumArray / array.length : 0;
}
