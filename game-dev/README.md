## Timing

---

## Functions

Functions help us reduce repetition in our code and build more powerful
programs. You may find that functions you write for one program can be reused in
other projects.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions

```js
function maximum(a, b) {
  if (a > b) {
    return a;
  }

  return b;
}

m = maximum(5, 6);
```

## Functions

```js
function maximum(a, b) {
  if (a > b) {
    return a;
  }

  return b;
}

m = maximum(5, 6);
```

- An **argument** is a value that is passed into a function when it's run.
- A **parameter** is the name of the variable that argument values are assigned
  to inside the function.
- **Calling** a function means giving a function the arguments it needs and
  running the code inside.
- A **return** value is the value that the function gives you back as a result
  when you call it.

## Functions

```js
// maximum takes two numerical arguments, a and b
// and returns the greater of the two numbers
function maximum(a, b) {
  if (a > b) {
    // return ends the function immediately
    return a; // give back the number a as the result
  }

  return b; // give back the number b as the result
}

// Call the maximum function with two arguments and assign the
// result to the variable m
m = maximum(5, 6); // m will equal 6
```

---

## Flappy Bird

- Game over screen
- Bird jump animation
- Parallax scrolling (debug with `camera.zoom`)

## Testing and Feedback

- A design choice you liked
- A suggestion for an improvement
- A question about the code

---

## Flappy Bird

- Random gap
- Scoring
- Collisions
- Boundary detection

---

## Flappy Bird

- Gravity
- Jumping
- Obstacles and movement
- Obstacle looping

---

## Sprites, Images, Colors, Colliders

- Colors
- Alpha
- Editing tools
  - Brush
  - Rotate
  - Flip
  - Fill
  - Crop
  - Mirror
  - Picker
- Why rotate sprite image vs in code?
- Piskel
- Color pallets
- Colliders
- Cropping sprites

---

## Board Games / Card Games

- Cribbage
- Set
- ERS

---

## Chase

- Mouse position
- Continuous vs discrete events
- AI sprite follow player
- Deadzone

---

## Team Building

Hobbies, sports, siblings, future study.

## Platform

- Lateral
- Jumping
- Gravity
- Ground collision
- Platform collision
- Camera tracking

---

## Drive

- Rotation
- `console.log`
- `setSpeedAndDirection`
- `sprite.getSpeed()`
- Exponential friction
- Extra board padding

---

## Bounce

- Multi-user input
- Bouncing Collisions
- Why is ball slower when it moves horizontally?

<br />
<br />

1. Two sprites with separate controls
2. Ball with movement, bouncing off walls
3. Ball bouncing off sprites

---

## Gravity

- Stop movement when button isn't pressed
- Gravity
- Config variables
- Functions

---

## Boundary

- Boundaries
  - Stop
  - Loop
  - Bounce

---

## Review

- What is the purpose of the `draw` function in GameLab?
- How do we decide what code to put before the `draw` function and what to put
  inside it?

## Collisions

- 1D character controls
- Randomized spawning
- Text display
- Declaring variables
- Scoring with counter pattern

---

## Review

- What are the dimensions of the game screen in GameLab?
- Where on the game screen is the coordinate `(0, 0)`?
- What code could we use to adjust the size of a sprite?

## Movement

- Sprite velocity
- `background` and why we need it
- `function draw`
- Multiple sprites
- Sprite position
- Conditionals

---

## Graphing Calculator Story

![](assets/calculator.jpg)

## Demo Projects

- Flappy bird
- Jacky

## Flappy Bird Concepts Brainstorm

## Grading policy

[Link](../shared/grading.md)

## Game Lab Intro

https://studio.code.org/projects/gamelab/new

## Sprites

- World coordinates
- Position
- `createSprite`
- `setAnimation`
- `sprite.scale`
