var emojiA = createSprite(200, 200);
emojiA.setAnimation("emoji_14_1");
emojiA.scale = 0.2;
emojiA.setSpeedAndDirection(5, randomNumber(0, 360));

var emojiB = createSprite(200, 200);
emojiB.setAnimation("emoji_14_1");
emojiB.scale = 0.2;
emojiB.setSpeedAndDirection(5, randomNumber(0, 360));

var emojiC = createSprite(200, 200);
emojiC.setAnimation("emoji_14_1");
emojiC.scale = 0.2;
emojiC.setSpeedAndDirection(5, randomNumber(0, 360));

var emojiD = createSprite(200, 200);
emojiD.setAnimation("emoji_14_1");
emojiD.scale = 0.2;
emojiD.setSpeedAndDirection(5, randomNumber(0, 360));

function draw() {
  background("white");

  if (emojiA.x < 0) {
    emojiA.x = 400;
  }

  if (emojiA.x > 400) {
    emojiA.x = 0;
  }

  if (emojiA.y < 0) {
    emojiA.y = 400;
  }

  if (emojiA.y > 400) {
    emojiA.y = 0;
  }

  if (emojiB.x < 0) {
    emojiB.x = 400;
  }

  if (emojiB.x > 400) {
    emojiB.x = 0;
  }

  if (emojiB.y < 0) {
    emojiB.y = 400;
  }

  if (emojiB.y > 400) {
    emojiB.y = 0;
  }

  if (emojiC.x < 0) {
    emojiC.x = 400;
  }

  if (emojiC.x > 400) {
    emojiC.x = 0;
  }

  if (emojiC.y < 0) {
    emojiC.y = 400;
  }

  if (emojiC.y > 400) {
    emojiC.y = 0;
  }

  if (emojiD.x < 0) {
    emojiD.x = 400;
  }

  if (emojiD.x > 400) {
    emojiD.x = 0;
  }

  if (emojiD.y < 0) {
    emojiD.y = 400;
  }

  if (emojiD.y > 400) {
    emojiD.y = 0;
  }

  drawSprites();
}
