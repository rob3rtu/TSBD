---
weight: 2
draft: false
title: mouseCol
---

Read-only property that retrieves the quadrille col under the current mouse position.

{{< callout type="warning" >}}
1. The `mouseCol` property isn't constrain to lie in [0..[width]({{< ref "width" >}})].
2. If the quadrille isn't currently being drawn use [screenCol]({{< ref "screen_col" >}}) instead.
{{< /callout >}}

## Example

{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(4, 8);
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  text('mouseCol: ' + quadrille.mouseCol, 20, 20);
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(4, 8);
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  text('mouseCol: ' + quadrille.mouseCol, 20, 20);
}
```
{{% /details %}}

## Syntax

> number = quadrille.mouseCol