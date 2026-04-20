---
weight: 2
title: clear(predicate)
---

Clears all cells that match a given condition, setting their values to `null`.

## Example

(move the mouse to clear all `🐉` from the current column; click to reset)  
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';

Quadrille.cellLength = 40;
let quadrille;

function setup() {
  createCanvas(400, 400);
  reset();
}

function draw() {
  background('SkyBlue');
  drawQuadrille(quadrille);
}

function mouseMoved() {
  const col = quadrille.mouseCol;
  quadrille.clear(({ col: c, value }) => c === col && value === '🐉');
}

function mouseClicked() {
  reset();
}

function reset() {
  quadrille = createQuadrille(10, 10, 20, '🐉').rand(20, '🐹').rand(20, '🐭');
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
  background('SkyBlue');
  drawQuadrille(quadrille);
}

function mouseMoved() {
  const col = quadrille.mouseCol;
  quadrille.clear(({ col: c, value }) => c === col && value === '🐉');
}

function mouseClicked() {
  reset();
}

function reset() {
  quadrille = createQuadrille(10, 10, 20, '🐉').rand(20, '🐹').rand(20, '🐭');
}
```
{{% /details %}}

## Syntax

> `clear(predicate)`

## Parameters

| Param       | Description                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------------- |
| `predicate` | Function: condition that determines which cells to clear. Receives `{ row, col, value }` as input[^1] |

[^1]: The `value` field may be of any type, including functions or objects.