---
weight: 4
title: fill(predicate, value)
---

Fills cells matching a predicate condition with the specified `value`.

## Example

(move the mouse to fill empty cells in the current row with `🐉`; click to reset)  
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';

Quadrille.cellLength = 40;
let quadrille;

function setup() {
  createCanvas(400, 400);
  reset();
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseMoved() {
  quadrille.fill(({ row, col, value }) => row === quadrille.mouseRow && value === null, '🐉');
}

function mouseClicked() {
  reset();
}

function reset() {
  quadrille = createQuadrille(10, 10, 15, color('purple'));
  quadrille.rand(15, color('orange')).rand(15, color('yellow'));
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}

```js
Quadrille.cellLength = 40;
let quadrille;

function setup() {
  createCanvas(400, 400);
  reset();
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseMoved() {
  quadrille.fill(({ row, col, value }) => row === quadrille.mouseRow && value === null, '🐉');
}

function mouseClicked() {
  reset();
}

function reset() {
  quadrille = createQuadrille(10, 10, 15, color('purple'));
  quadrille.rand(15, color('orange')).rand(15, color('yellow'));
}
```

{{% /details %}}

## Syntax

> `fill(predicate, value)`

## Parameters

| Param       | Description                                                                               |
| ----------- | ----------------------------------------------------------------------------------------- |
| `predicate` | Function: A predicate function `({ row, col, value }) => boolean` selecting cells to fill |
| `value`[^1] | Any: A valid JavaScript value                                                             |

[^1]: If `value` is a function, it is evaluated **per cell**. Use `Quadrille.factory(({ row, col }) => new Object(...))` to generate a new object per cell. For display routines, use a plain function like `({ row, col, options }) => { ... }`. See [`options`]({{< relref display_fns >}}) for available parameters.
