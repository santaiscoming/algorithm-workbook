process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    Array.from({length: b}, () => {
        console.log('*'.repeat(a))
    })
});