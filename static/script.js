let farge = document.body;
let typer = document.getElementById("typebox");

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