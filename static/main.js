var burgerToggle = document.querySelector(".navbar-burger");
var navbarMenu = document.querySelector(".navbar-menu");
var uploadButton = document.querySelector(".upload");
var modal = document.querySelector(".modal");
var modalForm = document.getElementById("uploadForm");
var progressBar = document.getElementById("progress");
var abortUpload = document.getElementById("abortUpload");

burgerToggle.addEventListener("click", () => {
  navbarMenu.classList.toggle("is-active");
  burgerToggle.classList.toggle("is-active");
});

uploadButton.addEventListener("click", () => {
  modal.classList.add("is-active");
  removeResponseText();
});

function closeModal() {
  modal.classList.remove("is-active");
}

function removeResponseText() {
  var responseText = document.getElementById("responseText");
  if (responseText) {
    responseText.classList.add("is-hidden");
  }
}

function showProgressBar() {
  progressBar.classList.remove("is-hidden");
  abortUpload.classList.remove("is-hidden");
}

function removeProgressBar() {
  progressBar.value = 0;
  progressBar.classList = "progress is-link is-hidden mt-3";
  abortUpload.classList.add("is-hidden");
  uploadForm.reset();
}

htmx.on("#uploadForm", "htmx:xhr:progress", function (evt) {
  htmx
    .find("#progress")
    .setAttribute("value", (evt.detail.loaded / evt.detail.total) * 100);
});
