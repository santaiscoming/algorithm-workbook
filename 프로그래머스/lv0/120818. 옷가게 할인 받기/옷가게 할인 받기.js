const discountMap = new Map([
  [500000, 20],
  [300000, 10],
  [100000, 5],
]);

function solution(price) {
  for (let [priceRef, discountRate] of discountMap) {
    if (price >= priceRef) return Math.floor(price - (price / 100) * discountRate);
  }
  return Math.floor(price);
}
