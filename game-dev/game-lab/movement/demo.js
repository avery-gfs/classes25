var player = createSprite(200, 350);
player.setAnimation("emoji_04_1");
player.scale = 0.2;
player.velocityX = -3;

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

  drawSprites();
}
