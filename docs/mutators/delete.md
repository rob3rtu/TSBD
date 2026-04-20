---
weight: 1
draft: false
title: delete(row)
---

Deletes a row from the quadrille.

## Example

(click on any cell; press any key to reset)\
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
  quadrille.delete(quadrille.mouseRow);
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
  quadrille.delete(quadrille.mouseRow);
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

> `delete(row)`

## Parameters

| Param     | Description                                                               |
|-----------|---------------------------------------------------------------------------|
| `row`     | Number: number of row to be deleted [[0..height]]({{< ref "height" >}}) |