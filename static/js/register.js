let nextButton = document.querySelector(".next-button");
console.log(nextButton);
let registerNum = 1;

nextButton.addEventListener("click", function (e) {
  if (registerNum >= 3) {
    e.target.setAttribute("type", "submit");
  }
  document.querySelector(".logo" + String(registerNum)).style =
    "display: none;";
  document.querySelector(".group" + String(registerNum++)).style =
    "display: none;";
  if (registerNum == 3) {
    document.querySelector(".logo" + String(registerNum) + "w").style =
      "display: block;";
    document.querySelector(".group" + String(registerNum)).style =
      "display: flex; flex-direction: column; align-items: center;";
  } else {
    document.querySelector(".logo" + String(registerNum)).style =
      "display: block;";
    document.querySelector(".group" + String(registerNum)).style =
      "display: block;";
  }
});
