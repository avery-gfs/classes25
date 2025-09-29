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
    rocket.rotationSpeed = -5;
  } else if (keyDown("right")) {
    rocket.rotationSpeed = 5;
  } else {
    rocket.rotationSpeed = 0;
  }

  if (rocket.x < -25) {
    rocket.x = 425;
  }

  if (rocket.x > 425) {
    rocket.x = -25;
  }

  if (rocket.y < -25) {
    rocket.y = 425;
  }

  if (rocket.y > 425) {
    rocket.y = -25;
  }

  // console.log(rocket.rotation, speed);

  rocket.setSpeedAndDirection(speed, rocket.rotation);
  drawSprites();
}
