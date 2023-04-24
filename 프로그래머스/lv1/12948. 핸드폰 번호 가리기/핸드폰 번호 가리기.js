function solution(phone_number) {
    const lastFourNums = [...phone_number].splice(phone_number.length - 4)

    return [...'*'.repeat(phone_number.length - 4), ...lastFourNums].join('')

}