var player = createSprite(200, 350);
player.setAnimation("emoji_04_1");
player.scale = 0.2;

var goal = createSprite(200, 0);
goal.setAnimation("shortcake_1");
goal.scale = 0.1;

var score = 0;

function draw() {
  background("white");

  goal.velocityY = goal.velocityY + 0.5;

  if (keyDown("left")) {
    player.velocityX = -8;
  } else if (keyDown("right")) {
    player.velocityX = 8;
  } else {
    player.velocityX = 0;
  }

  if (goal.y > 400) {
    goal.y = 0;
    goal.x = randomNumber(0, 400);
    goal.velocityY = 5;
  }

  if (goal.isTouching(player)) {
    goal.y = 0;
    goal.velocityY = 5;
    goal.x = randomNumber(0, 400);
    score += 1;
  }

  text(score, 10, 10);

  drawSprites();
}
