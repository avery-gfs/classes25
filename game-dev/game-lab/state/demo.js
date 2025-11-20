var rocket = createSprite(200, 200);
rocket.setAnimation("rocket3_1");
rocket.scale = 0.2;

var rocks = createSprite(300, 300);
rocks.setAnimation("rocks_1");
rocks.scale = 0.2;

var ready = createSprite(200, 200);
ready.setAnimation("ready");

var speed = 0;
var state = 0;
var startTime = 0;

function draw() {
  if (state == 0) {
    ready.visible = true;

    if (keyDown("space")) {
      state = 1;
      startTime = World.seconds;
    }

    drawSprites();
  } else if (state == 1) {
    ready.visible = false;
    background("lightblue");

    textSize(40);
    text(3 - World.seconds + startTime, 200, 150);

    if (World.seconds - startTime == 3) {
      state = 2;
      startTime = World.seconds;
    }

    drawSprites();
  } else {
    background("white");

    text(World.seconds - startTime, 20, 20);

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

    if (rocket.isTouching(rocks)) {
      state = 0;
    }

    rocket.setSpeedAndDirection(speed, rocket.rotation);

    drawSprites();
  }
}
