let dogs = [];
for (let i = 0; i < 6; i++) {
  let name = prompt(`Enter the name of dog ${i + 1}:`);
  dogs.push(name);
}

dogs.sort().reverse();

let outputDiv = document.getElementById("output");
let list = document.createElement("ul");

for (let i = 0; i < dogs.length; i++) {
  let item = document.createElement("li");
  item.textContent = dogs[i];
  list.appendChild(item);
}

outputDiv.appendChild(list);