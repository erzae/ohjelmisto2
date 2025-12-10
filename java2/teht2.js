let count = parseInt(prompt("Enter the number of participants:"), 10);


let participants = [];
for (let i = 0; i < count; i++) {
  let name = prompt(`Enter name of participant ${i + 1}:`);
  participants.push(name);
}


participants.sort();


let outputDiv = document.getElementById("output");
let list = document.createElement("ol");

for (let i = 0; i < participants.length; i++) {
  let item = document.createElement("li");
  item.textContent = participants[i];
  list.appendChild(item);
}

outputDiv.appendChild(list);