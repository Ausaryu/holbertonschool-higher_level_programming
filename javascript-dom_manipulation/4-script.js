const ul = document.querySelector(".my_list");
const add_item = document.querySelector("#add_item");

add_item.addEventListener("click" , function () {
    const new_list = document.createElement("li");
    new_list.textContent = "Item";

    ul.appendChild(new_list);
})