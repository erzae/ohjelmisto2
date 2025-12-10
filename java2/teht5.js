let numbers = [];

while (true) {
  let input = prompt("Enter a number:");
  let num = Number(input);

  if (numbers.includes(num)) {
    console.log(`Number ${num} has already been given. Stopping...`);
    break;
  }
  numbers.push(num);
}

numbers.sort(function(a, b) {
  return a - b;
});

console.log("Numbers in ascending order:");
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}