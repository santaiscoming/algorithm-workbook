function solution(files) {
  return files.sort((a, b) => {
    const reg = /^([^\d]+)(\d{1,5})(.*)$/i;

    const aMatch = a.match(reg);
    const bMatch = b.match(reg);

    const aHead = aMatch[1].toLowerCase();
    const bHead = bMatch[1].toLowerCase();

    if (aHead < bHead) return -1;
    if (aHead > bHead) return 1;

    const aNumber = parseInt(aMatch[2], 10);
    const bNumber = parseInt(bMatch[2], 10);

    if (aNumber < bNumber) return -1;
    if (aNumber > bNumber) return 1;

    return 0;
  });
}