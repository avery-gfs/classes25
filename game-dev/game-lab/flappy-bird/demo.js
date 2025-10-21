var bg = createSprite(330, 200);
bg.setAnimation("sky");
bg.velocityX = -2;

var bird = createSprite(100, 200);
bird.setAnimation("ducky_1");
bird.scale = 0.1;

var topPipe = createSprite(400, -100);
topPipe.setAnimation("pipe");
topPipe.velocityX = -15;

var bottomPipe = createSprite(400, 500);
bottomPipe.setAnimation("pipe");
bottomPipe.velocityX = -15;

var over = createSprite(200, 200);
over.setAnimation("over");
over.visible = false;

var score = 0;

function draw() {
  background("white");

  bird.rotation = bird.velocityY;
  bird.velocityY += 2;

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
  }

  if (bg.x < 62) {
    bg.x = 330;
  }

  drawSprites();
  fill("white");
  textSize(30);
  text(score, 20, 40);
}
