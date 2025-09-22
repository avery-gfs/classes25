var ballSpeed = 5;

var ball = createSprite(200, 200);
ball.setAnimation("soccer_bw_1");
ball.scale = 0.1;
ball.velocityX = -ballSpeed;
ball.velocityY = -ballSpeed;

var player1 = createSprite(370, 200);
player1.setAnimation("chick_1_1");
player1.scale = 0.1;

var player2 = createSprite(30, 200);
player2.setAnimation("cuteanimals_rooster_hello_1");
player2.scale = 0.1;

function draw() {
  background("white");
  
  if (keyDown("up")) {
    player1.velocityY = -4;
  } else if (keyDown("down")) {
    player1.velocityY = 4;
  } else {
    player1.velocityY = 0;
  }  
  
  if (keyDown("w")) {
    player2.velocityY = -4;
  } else if (keyDown("s")) {
    player2.velocityY = 4;
  } else {
    player2.velocityY = 0;
  }
  
  if (player1.isTouching(ball)) {
    ball.velocityX = -ballSpeed;
    ball.velocityY = player1.velocityY * 2;
  }
    
  if (player2.isTouching(ball)) {
    ball.velocityX = ballSpeed;
    ball.velocityY = player2.velocityY * 2;
  }
  
  if (ball.x < 0) {
    ball.velocityX *= -1;
    ball.x = 0;
  }
    
  if (ball.x > 400) {
    ball.x = 400;
    ball.velocityX *= -1;
  }
    
  if (ball.y < 0) {
    ball.y = 0;
    ball.velocityY *= -1;
  }
    
  if (ball.y > 400) {
    ball.y = 400;
    ball.velocityY *= -1;
  }
  
  drawSprites();
}
