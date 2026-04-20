---
weight: 1
draft: false
title: width
---

Quadrille width read-write property.

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
  text('width: ' + quadrille.width, 20, 20);
}

function mouseMoved() {
  // property write
  quadrille.width = quadrille.mouseCol + 1;
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
  text('width: ' + quadrille.width, 20, 20);
}

function mouseMoved() {
  // property write
  quadrille.width = quadrille.mouseCol + 1;
}
```
{{% /details %}}

## Syntax

> quadrille.width = number

> number = quadrille.width