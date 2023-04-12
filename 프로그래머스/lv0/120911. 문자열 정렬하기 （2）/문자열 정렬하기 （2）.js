function solution(my_string) {
    return [...my_string].map((str) => str.toLowerCase())
                         .sort((a, b) => a.localeCompare(b))
                         .join('')
}