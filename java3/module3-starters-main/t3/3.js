const names = ["John", "Paul", "Jones"];

const target = document.getElementById("target");

let listItems = "";
for (let i = 0; i < names.length; i++) {
  listItems += `<li>${names[i]}</li>`;
}

target.innerHTML = listItems;