function getAge(inputString) {
    for (let i = 0; i < inputString.length; i++) {
        return isNaN(inputString[i]) ? "" : Number(inputString[i]);
    }
}
