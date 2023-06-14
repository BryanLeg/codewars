// Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

// Note: input will never be an empty string

function fakeBin(x) {
    digitBin = [];
    for (let i = 0; i < x.length; i++) {
        if (x[i] < 5) {
            digitBin.push(0);
        } else {
            digitBin.push(1);
        }
    }
    return digitBin.join("");
}

function fakeBin(x) {
    return x
        .split("")
        .map((n) => (n < 5 ? 0 : 1))
        .join("");
}
