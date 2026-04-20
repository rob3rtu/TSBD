---
weight: 8
title: clear(row, col, border)
---

Clears a specific cell and all connected cells in the quadrille using a [flood fill](https://en.wikipedia.org/wiki/Flood_fill) algorithm. The `border` parameter determines if the clearing includes the boundary of the flood fill area.

## Example

(click on any cell to perform flood fill with selected border option; press any key to reset)\
{{< p5-global-iframe quadrille="true" width="425" height="445" >}}
'use strict';
Quadrille.cellLength = 20;
let quadrille;
let mode;

function setup() {
  createCanvas(400, 400);
  mode = createSelect();
  mode.option('flood fill without border');
  mode.option('flood fill with border');
  mode.selected('flood fill without border');
  reset();
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  const row = quadrille.mouseRow;
  const col = quadrille.mouseCol;
  const border = mode.value() === 'flood fill with border';
  quadrille.clear(row, col, 4, border);
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
let mode;

function setup() {
  createCanvas(400, 400);
  mode = createSelect();
  mode.option('flood fill without border');
  mode.option('flood fill with border');
  mode.selected('flood fill without border');
  reset();
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  const row = quadrille.mouseRow;
  const col = quadrille.mouseCol;
  const border = mode.value() === 'flood fill with border';
  quadrille.clear(row, col, 4, border);
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

> `clear(row, col, border)`

## Parameters

| Param     | Description                                                                                 |
|-----------|---------------------------------------------------------------------------------------------|
| `row`     | Number: row index of the cell to start clearing [[0..height]]({{< ref "height" >}})       |
| `col`     | Number: column index of the cell to start clearing [[0..width]]({{< ref "width" >}})      |
| `border`  | Boolean: Specifies whether to include the border of the flood fill area. Default is `false` |
