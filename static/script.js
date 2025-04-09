let farge = document.body;
let typer = document.getElementById("typebox");

let container = document.getElementById("container");
let textAdd = document.getElementById("linetext");

let hideMenu = document.getElementById("hidemenu");
let toggleMenu = document.getElementById("togglemenu")

document.getElementById("choose").addEventListener("click", function ()
{
    let chosen = typer.value;
    farge.style.backgroundColor = chosen;
});

toggleMenu.addEventListener("click", function ()
{
    if (hideMenu.style.display === "none")
    {
        hideMenu.style.display = "block";
        toggleMenu.textContent = "Close line menu";
    } else {
        hideMenu.style.display = "none";
        toggleMenu.textContent = "Make a new line";
    }
});

document.getElementById("addText").addEventListener("click", function ()
{
    let userText = textAdd.value;
    let selectedType = document.getElementById("texttype").value;
    if (userText != "")
    {
        let newText = document.createElement(selectedType);
        newText.textContent = userText;
        container.appendChild(newText);
        textAdd.value = "";
    }
})