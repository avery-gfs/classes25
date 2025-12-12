// makeEmoji takes no arguments, and returns a new sprite object

function makeEmoji() {
  var sprite = createSprite(200, 200);
  sprite.setAnimation("emoji_14_1");
  sprite.scale = 0.2;
  sprite.setSpeedAndDirection(5, randomNumber(0, 360));
  return sprite;
}

// We can use makeEmoji to make 4 new sprites

var emojiA = makeEmoji();
var emojiB = makeEmoji();
var emojiC = makeEmoji();
var emojiD = makeEmoji();

// wrapPosition takes a sprite object as an argument, and adjusts
// the sprite's position if the sprite has gone off the edge of the board
// wrapPosition doesn't return any value

function wrapPosition(sprite) {
  if (sprite.x < 0) {
    sprite.x = 400;
  }

  if (sprite.x > 400) {
    sprite.x = 0;
  }

  if (sprite.y < 0) {
    sprite.y = 400;
  }

  if (sprite.y > 400) {
    sprite.y = 0;
  }
}

function draw() {
  background("white");

  // We can give our sprite objects to wrapPosition to
  // have them wrap around the edges of the board

  wrapPosition(emojiA);
  wrapPosition(emojiB);
  wrapPosition(emojiC);
  wrapPosition(emojiD);

  drawSprites();
}
