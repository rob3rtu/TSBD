---
weight: 2
draft: false
title: "height"
---

Quadrille height read-write property.

## Example

(mouse click or press any key)  
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(8, 8);
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  // property read
  text('height: ' + quadrille.height, 20, 20);
}

function mouseMoved() {
  // property write
  quadrille.height = quadrille.mouseRow + 1;
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(8, 8);
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  // property read
  text('height: ' + quadrille.height, 20, 20);
}

function mouseMoved() {
  // property write
  quadrille.height = quadrille.mouseRow + 1;
}
```
{{% /details %}}

## Syntax

> quadrille.height = number

> number = quadrille.height