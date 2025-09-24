var rocket = createSprite(200, 200);
rocket.setAnimation("rocket3_1");
rocket.scale = 0.2;

var speed = 0;

function draw() {
  background("white");

  if (keyDown("up")) {
    if (speed < 40) {
      speed += 1;
    }
  } else {
    speed *= 0.9;
  }

  if (keyDown("left")) {
    rocket.rotation -= 5;
  }

  if (keyDown("right")) {
    rocket.rotation += 5;
  }

  if (rocket.x < -40) {
    rocket.x = 400;
  }

  if (rocket.x > 440) {
    rocket.x = 0;
  }

  if (rocket.y < -40) {
    rocket.y = 400;
  }

  if (rocket.y > 440) {
    rocket.y = 0;
  }

  rocket.setSpeedAndDirection(speed, rocket.rotation);
  drawSprites();
}
