---
weight: 2
draft: false
title: rotate()
---

π/2 clockwise rotation of the quadrille cells.

## Example

(mouse click or press any key to `rotate` the quadrille)  
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
let quadrille;

function setup() {
  createCanvas(4 * Quadrille.cellLength, 4 * Quadrille.cellLength);
  quadrille = createQuadrille(4, 4, 3, '🚀');
  quadrille.rand(4, '🐒');
}

function draw() {
  background('orange');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  quadrille.rotate();  
}

function keyPressed() {
  quadrille.rotate();
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
let quadrille;

function setup() {
  createCanvas(4 * Quadrille.cellLength, 4 * Quadrille.cellLength);
  quadrille = createQuadrille(4, 4, 3, '🚀');
  quadrille.rand(4, '🐒');
}

function draw() {
  background('orange');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  quadrille.rotate();  
}

function keyPressed() {
  quadrille.rotate();
}
```
{{% /details %}}

## Syntax

> `rotate()`