function hide_loader() {
    setTimeout(hide, 500)
}
function hide() {
    loader = document.getElementById("loaderoverlay");
    loader.style.display = "None";
}