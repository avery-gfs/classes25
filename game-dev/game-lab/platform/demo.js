var player = createSprite(200, 200);
player.setAnimation("xmasemoji_13_1");
player.scale = 0.1;

var platform = createSprite(200, 300);
platform.setAnimation("animation_1");

function draw() {
  background("white");

  player.collide(platform);

  if (keyDown("left")) {
    player.velocityX = -5;
  } else if (keyDown("right")) {
    player.velocityX = 5;
  } else {
    player.velocityX = 0;
  }

  if (keyDown("space")) {
    player.velocityY = -12;
  }

  player.velocityY += 1;

  if (player.y > 380) {
    player.y = 380;
  }

  camera.x = player.x;

  drawSprites();
}
