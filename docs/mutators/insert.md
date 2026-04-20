---
weight: 2
draft: false
title: insert(row)
---

Inserts an empty row into the quadrille.

## Example

(click any row; press any key to reset)\
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
  quadrille.insert(quadrille.mouseRow);
}

function keyPressed() {
  reset();
}

function reset() {
  quadrille = createQuadrille(20, 10, 50, color('red'));
  quadrille.rand(50, color('lime')).rand(50, color('blue'));
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
  quadrille.insert(quadrille.mouseRow);
}

function keyPressed() {
  reset();
}

function reset() {
  quadrille = createQuadrille(20, 10, 50, color('red'));
  quadrille.rand(50, color('lime')).rand(50, color('blue'));
}
```
{{% /details %}}

## Syntax

> `insert(row)`

## Parameters

| Param     | Description                                                                     |
|-----------|---------------------------------------------------------------------------------|
| `row`     | Number: number of the row to be inserted [[0..height]]({{< ref "height" >}})] |