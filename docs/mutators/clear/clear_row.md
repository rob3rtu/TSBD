---
weight: 4
title: clear(row)
---

Clears an entire row in the quadrille, setting each cell in the row to empty (i.e., `null`).

## Example

(click on a row to clear it; press any key to reset)\
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
Quadrille.cellLength = 20;
let quadrille;

function setup() {
  createCanvas(400, 400);
  reset();
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  const row = quadrille.mouseRow;
  quadrille.clear(row);
}

function keyPressed() {
  reset();
}

function reset() {
  quadrille = createQuadrille(20, 20, 100, color('red'));
  quadrille.rand(100, color('lime')).rand(100, color('blue'));
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 20;
let quadrille;

function setup() {
  createCanvas(400, 400);
  reset();
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  const row = quadrille.mouseRow;
  quadrille.clear(row);
}

function keyPressed() {
  reset();
}

function reset() {
  quadrille = createQuadrille(20, 20, 100, color('red'));
  quadrille.rand(100, color('lime')).rand(100, color('blue'));
}
```
{{% /details %}}

## Syntax

> `clear(row)`

## Parameters

| Param     | Description                                                          |
|-----------|----------------------------------------------------------------------|
| `row`     | Number: The row index to clear [[0..height]]({{< ref "height" >}}) |