---
weight: 2
title: fill(color1, color2)
---

Fills all cells in the quadrille with a chessboard pattern.

## Example

(click or press any key to toggle between filling and clearing the quadrille)\
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
Quadrille.cellLength = 20;
let board = true;
let quadrille;

function setup() {
  createCanvas(400, 400);
  quadrille = createQuadrille(20, 20);
  quadrille.fill('cyan', 'red');  // create a chessboard pattern with given colors
}

function draw() {
  background('black');
  drawQuadrille(quadrille, { tileDisplay: board ? 0 : Quadrille.tileDisplay });
}

function mouseClicked() {
  board = !board;
  board ? quadrille.fill('cyan', 'red') : quadrille.clear();
}

function keyPressed() {
  board = !board;
  board ? quadrille.fill('cyan', 'red') : quadrille.clear();
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 20;
let board = true;
let quadrille;

function setup() {
  createCanvas(400, 400);
  quadrille = createQuadrille(20, 20);
  quadrille.fill('cyan', 'red');  // create a chessboard pattern with given colors
}

function draw() {
  background('black');
  drawQuadrille(quadrille, { tileDisplay: board ? 0 : Quadrille.tileDisplay });
}

function mouseClicked() {
  board = !board;
  board ? quadrille.fill('cyan', 'red') : quadrille.clear();
}

function keyPressed() {
  board = !board;
  board ? quadrille.fill('cyan', 'red') : quadrille.clear();
}
```
{{% /details %}}

## Syntax

> `fill(color1, color2)`

## Parameters

| Param  | Description                                                                                    |
|--------|------------------------------------------------------------------------------------------------|
| `color1` | [p5.Color](https://p5js.org/reference/#/p5.Color) \| String: The color used for the light squares of the chessboard pattern. Can be a `p5.Color` instance or an HTML color string (e.g., `'red'`, `'#ff0000'`, `'rgb(255,0,0)'`) |
| `color2` | [p5.Color](https://p5js.org/reference/#/p5.Color) \| String: The color used for the dark squares of the chessboard pattern. Can be a `p5.Color` instance or an HTML color string                                                |