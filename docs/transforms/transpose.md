---
weight: 3
draft: false
title: transpose()
---

[Transposes](https://en.wikipedia.org/wiki/Transpose) the quadrille cells.

## Example

(mouse click or press any key to `transpose` the quadrille)  
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
  quadrille.transpose();  
}

function keyPressed() {
  quadrille.transpose();
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
  quadrille.transpose();  
}

function keyPressed() {
  quadrille.transpose();
}
```
{{% /details %}}

{{< callout type="info" >}}  
`transpose()` is useful for performing column transformations using row commands. For instance, `q.transpose().row(col).transpose()` clones column `col`.  
{{< /callout >}}

## Syntax

> `transpose()`