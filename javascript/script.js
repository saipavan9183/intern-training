// Theme Toggle
const themeBtn = document.getElementById("theme-toggle");

themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme");
    document.body.classList.toggle("light-theme");
});


// Add Skills to List

const itemInput = document.getElementById("item-input");
const addBtn = document.getElementById("add-btn");
const itemList = document.getElementById("item-list");

let items = [];

function renderItems() {
    itemList.innerHTML = "";

    items.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = item;
        itemList.appendChild(li);
    });
}

addBtn.addEventListener("click", () => {
    const value = itemInput.value.trim();

    if (value === "") return;

    items.push(value);
    renderItems();

    itemInput.value = "";
    itemInput.focus();
});


// Fetch Random Quote

const quoteBtn = document.getElementById("fetch-quote");
const quote = document.getElementById("quote");

quoteBtn.addEventListener("click", async () => {
    try {
        const response = await fetch("https://api.quotable.io/random");
        const data = await response.json();

        quote.innerHTML = `"${data.content}"<br><strong>- ${data.author}</strong>`;
    } catch (error) {
        quote.textContent = "Unable to fetch quote.";
        console.error(error);
    }
});