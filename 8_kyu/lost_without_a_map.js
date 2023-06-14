// Given an array of integers, return a new array with each value doubled.

// For example:

// [1, 2, 3] --> [2, 4, 6]

array = [1, 2, 3];

function maps(x) {
  doubledValues = x.map((nb) => nb * 2);
  return doubledValues;
}

console.log(maps(array));
