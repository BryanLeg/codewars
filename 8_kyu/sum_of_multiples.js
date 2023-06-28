function sumMul(n, m) {
    let num = 0;
    for (let i = 0; n * i < m; i++) {
        num += n * i;
    }
    if (num === 0) {
        return "INVALID";
    }
    return num;
}
