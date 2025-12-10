let numbers = [];

while (true) {
  let input = prompt("Enter a number (0 stops):");
  let num = Number(input);

  if (num === 0) {
    break;
  }

  numbers.push(num);
}

numbers.sort(function(a, b) {
  return b - a;
});

console.log("Numbers from largest to smallest:");
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}