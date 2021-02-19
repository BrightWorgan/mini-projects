const randomNumber1 = Math.floor(Math.random() * 6) + 1;
// const randomNumber1 = Math.ceil(Math.random() * 6);
/* Needed to get a whole random number between 1 and 6 /|\*/

const randomDiceImage = 'dice' + randomNumber1 + ".png";
// const randomDiceImage = `dice${randomNumber1}.png`;
/* In order to get both the number and image to change with every refresh */

const randomImageSource = "images/" + randomDiceImage;

// const randomImageSource = `image/${randomDiceImage}`;
/* In order to keep the source file the same for every inmage change, (could have included this in the above var but course rec. keeping it separate). */

var image1 = document.querySelectorAll("img")[0];

image1.setAttribute("src", randomImageSource);

var randomNumber2 = Math.floor(Math.random() * 6) + 1;

var randomImageSource2 = "images/dice" + randomNumber2 + ".png";

document.querySelectorAll("img")[1].setAttribute("src", randomImageSource2);

if (randomNumber1 > randomNumber2) {
  document.querySelector("h1").innerHTML = "Colin Wins!";
} else if (randomNumber2 > randomNumber1) {
  document.querySelector("h1").innerHTML = "sarah Wins!";
} else {
  document.querySelector("h1").innerHTML = "Looks like it's a freezer dinner tonight!"
};