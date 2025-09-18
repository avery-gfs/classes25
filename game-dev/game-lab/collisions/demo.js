var player = createSprite(200, 350);
player.setAnimation("emoji_04_1");
player.scale = 0.2;
player.velocityX = -3;

var goal = createSprite(200, 0);
goal.setAnimation("shortcake_1");
goal.scale = 0.1;
goal.velocityY = 6;

var score = 0;

function draw() {
  background("white");

  if (keyDown("left")) {
    player.velocityX = -3;
  }

  if (keyDown("right")) {
    player.velocityX = 3;
  }

  if (player.x < 0) {
    player.x = 400;
  }

  if (player.x > 400) {
    player.x = 0;
  }

  if (goal.y > 400) {
    goal.y = 0;
    goal.x = randomNumber(0, 400);
  }

  if (goal.isTouching(player)) {
    goal.y = 0;
    goal.x = randomNumber(0, 400);
    score += 1;
  }

  text(score, 10, 10);

  drawSprites();
}
