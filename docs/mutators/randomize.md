---
weight: 4
draft: false
title: randomize()
---

Randomly re-arranges the quadrille cells.

## Example

(mouse click to randomize; press any key to reset)\
{{< p5-global-iframe quadrille="true" width="537" height="537" >}}
'use strict';
Quadrille.cellLength = 32;
let mandrill;
let quadrille;

async function setup() {
  createCanvas(512, 512);
  mandrill = await loadImage('../mandrill.png');
  quadrille = createQuadrille(16, mandrill);
}

function draw() {
  drawQuadrille(quadrille);
}

function mouseClicked() {
  quadrille.randomize();
}

function keyPressed() {
  quadrille = createQuadrille(16, mandrill);
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 32;
let mandrill;
let quadrille;

async function setup() {
  createCanvas(512, 512);
  mandrill = await loadImage('mandrill.png');
  quadrille = createQuadrille(16, mandrill);
}

function draw() {
  drawQuadrille(quadrille);
}

function mouseClicked() {
  quadrille.randomize();
}

function keyPressed() {
  quadrille = createQuadrille(16, mandrill);
}
```
{{% /details %}}

{{< callout type="info" >}}
For deterministic (repeatable) randomness, explicitly call [randomSeed(seed)](https://p5js.org/reference/p5/randomSeed/) before `randomize()`.
{{< /callout >}}

## Syntax

> `randomize()`
