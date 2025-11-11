var reset = createSprite(300, 300);
reset.setAnimation("animation_1");

var witch = createSprite(100, 100);
witch.setAnimation("monster_07_1");
witch.scale = 0.2;

var start = World.seconds;

function draw() {
  background("white");
  textSize(20);
  text(World.seconds - start, 300, 200);

  if (mousePressedOver(reset)) {
    start = World.seconds;
    witch.y = 100;
    witch.velocityY = 0;
  }

  if (World.seconds - start >= 5) {
    witch.velocityY += 1;
  }

  drawSprites();
}
