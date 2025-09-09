var player = createSprite(200, 350);
player.setAnimation("emoji_04_1");
player.scale = 0.2;
player.velocityX = -3;

var goal = createSprite(200, 0);
goal.setAnimation("shortcake_1");
goal.scale = 0.1;
goal.velocityY = 6;

function draw() {
  background("white");
  
  if (goal.y > 400) {
    goal.y = 0;
  }
  
  if (player.x < 0) {
    player.x = 400;
  }
  
  drawSprites();
}

