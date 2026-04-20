---
weight: 4
draft: false
title: order
---

Read-only property that retrieves the quadrille non-empty number of cells.

## Example

(mouse click to toggle video playback; press any key to change quadrille order & size)  
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
let destino; // Video variable
let quadrille;

async function setup() {
  createCanvas(400, 400);
  // Load video
  destino = await createVideo(['/videos/destino.webm']);
  destino.hide(); // Hide video controls
  quadrille = createQuadrille(8, 8, int(random(1, 64)), destino);
}

function draw() {
  background('black');
  drawQuadrille(quadrille, { cellLength: width / quadrille.width });
  fill('yellow');
  text('order: ' + quadrille.order + ', size: ' + quadrille.size, 20, 20);
}

function mouseClicked() {
  // Toggle video playback on mouse click
  destino.looping ? destino.pause() : destino.loop();
  destino.looping = !destino.looping;
}

function keyPressed() {
  const dim = int(random(1, 8));
  //const size = dim ** 2; // Equivalent to: size = pow(dim, 2);
  const size = pow(dim, 2);
  const order = int(random(1, size));
  quadrille = createQuadrille(dim, dim, order, destino);
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
let destino; // Video variable
let quadrille;

async function setup() {
  createCanvas(400, 400);
  // Load video
  destino = await createVideo(['/videos/destino.webm']);
  destino.hide(); // Hide video controls
  quadrille = createQuadrille(8, 8, int(random(1, 64)), destino);
}

function draw() {
  background('black');
  drawQuadrille(quadrille, { cellLength: width / quadrille.width });
  fill('yellow');
  text('order: ' + quadrille.order + ', size: ' + quadrille.size, 20, 20);
}

function mouseClicked() {
  // Toggle video playback on mouse click
  destino.looping ? destino.pause() : destino.loop();
  destino.looping = !destino.looping;
}

function keyPressed() {
  const dim = int(random(1, 8));
  const size = dim ** 2; // Equivalent to: size = pow(dim, 2);
  const order = int(random(1, size));
  quadrille = createQuadrille(dim, dim, order, destino);
}
```
{{% /details %}}

## Syntax

> number = quadrille.order
