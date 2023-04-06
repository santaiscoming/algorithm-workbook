function solution(n, k) {
    const kkochi = n * 12000;
    const drink = k * 2000;
    const service = parseInt(n / 10) * 2000
    const totalPrice = kkochi + drink - service;
    return totalPrice;
}