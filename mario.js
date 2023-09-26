let n = 4
let i = 0
let str = ''
while (i < n) {
  i++

  for (let x = 0; x < n - i; x++) {
    str += '#'
  }
  console.log(str)
}
