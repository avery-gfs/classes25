var player = createSprite(200, 200);
player.setAnimation("xmasemoji_13_1");
player.scale = 0.1;

var platform = createSprite(200, 300);
platform.setAnimation("animation_1");

function draw() {
  background("white");

  player.collide(platform);

  if (keyDown("space")) {
    player.velocityY = -5;
  }

  if (keyDown("left")) {
    player.velocityX = -5;
  } else if (keyDown("right")) {
    player.velocityX = 5;
  } else {
    player.velocityX = 0;
  }

  if (keyDown("space")) {
    player.velocityY = -15;
  }

  if (player.y > 380) {
    player.y = 380;
  }

  player.velocityY += 1;

  camera.x = player.x;

  drawSprites();
}
