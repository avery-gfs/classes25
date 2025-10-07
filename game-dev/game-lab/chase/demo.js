var player = createSprite(200, 200);
player.setAnimation("emoji_09_1");
player.scale = 0.1;

var ghost = createSprite(200, 200);
ghost.setAnimation("halloweenemoji_04_1");
ghost.scale = 0.1;

var speed = 10;
var buffer = speed / 2;

function draw() {
  background("white");
  
  player.x = World.mouseX;
  player.y = World.mouseY;

  if (World.mouseX < ghost.x - buffer) {
    ghost.velocityX = -speed;
  } else if (World.mouseX > ghost.x + buffer) {
    ghost.velocityX = speed;
  } else {
    ghost.velocityX = 0;
  }
  
  if (World.mouseY < ghost.y - buffer) {
    ghost.velocityY = -speed;
  } else if (World.mouseY > ghost.y + buffer) {
    ghost.velocityY = speed;
  } else {
    ghost.velocityY = 0;
  }

  drawSprites();
}
