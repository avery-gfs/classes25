console.log("Game Dev Info");

console.log({
  name: "Avery Nortonsmith",
  email: "anortonsmith@germantownfriends.org",
});

const description = `
Decades of grassroots research has confirmed: video games are fun. But besides being fun, they're also a great way to learn about software engineering, computer graphics, 2D and 3D design, physics, and much more! In this class, we will explore game programming and design in its many forms. We'll start by creating 2D games using JavaScript, and learn about core game programming concepts. After that, we'll look at multiplayer games and text-based games. Finally, we'll explore 3D game programming using Godot.
`;

console.log(description.replaceAll("\n", " ").trim());

const topics = [
  "User input and events",
  "Gravity and physics",
  "Game state and logic",
  "Colors",
  "Audio",
  "Simple game AI",
  "2D and 3D graphics",
  "Textures and lighting",
  "Text based games",
  "Multiplayer",
  "Randomness",
  "Sprite design and pixel art",
  "The ethics of game design",
];

console.log(topics.map((topic) => `• ${topic}`).join("\n"));

var wallSpeed = -15;
var gravity = 2;

var bg = createSprite(330, 200);
bg.setAnimation("sky");
bg.velocityX = -2;

var bird = createSprite(100, 200);
bird.setAnimation("ducky_1");
bird.scale = 0.1;

var topPipe = createSprite(400, -100);
topPipe.setAnimation("pipe");

var bottomPipe = createSprite(400, 500);
bottomPipe.setAnimation("pipe");

var over = createSprite(200, 200);
over.setAnimation("over");
over.visible = false;

var score = 0;

function draw() {
  background("white");

  topPipe.velocityX = wallSpeed;
  bottomPipe.velocityX = wallSpeed;
  bird.rotation = bird.velocityY;

  bird.velocityY += gravity;

  if (keyWentDown("space") || mouseWentDown("leftButton")) {
    bird.velocityY = -15;
  }

  if (topPipe.x < 0) {
    topPipe.x = 400;
    bottomPipe.x = 400;
    topPipe.y = randomNumber(-200, 0);
    bottomPipe.y = topPipe.y + 600;
    score += 1;
  }

  if (
    bird.isTouching(topPipe) ||
    bird.isTouching(bottomPipe) ||
    bird.y > 400 ||
    bird.y < 0
  ) {
    over.visible = true;
    wallSpeed = 0;
  }

  if (bg.x < 62) {
    bg.x = 330;
  }

  drawSprites();
  fill("white");
  textSize(30);
  text(score, 20, 40);
}
