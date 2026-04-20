---
weight: 1
draft: false
title: mouseRow
---

Read-only property that retrieves the quadrille row under the current mouse position.

{{< callout type="warning" >}}
1. The `mouseRow` property isn't constrain to lie in [0..[height]({{< ref "height" >}})].
2. If the quadrille isn't currently being drawn use [screenRow]({{< ref "screen_row" >}}) instead.
{{< /callout >}}

## Example

{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(8, 4);
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  text('mouseRow: ' + quadrille.mouseRow, 20, 20);
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(8, 4);
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  text('mouseRow: ' + quadrille.mouseRow, 20, 20);
}
```
{{% /details %}}

## Syntax

> number = quadrille.mouseRow