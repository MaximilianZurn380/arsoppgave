let farge = document.body;

let typer = document.getElementById("typebox");

document.getElementById("choose").addEventListener("click", function ()
{
    let chosen = typer.value;
    farge.style.backgroundColor = chosen;
});