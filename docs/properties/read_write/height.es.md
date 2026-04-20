---
weight: 6  
draft: true
title: "height"
---

Propiedad de lectura y escritura de la altura de la cuadrícula.

# Ejemplo

(haz clic o presiona cualquier tecla)  
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(8, int(random(1, 9)));
  quadrille.rand(int(quadrille.size * 0.6), '🐒');
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  // propiedad de lectura
  text('height: ' + quadrille.height, 20, 20);
}

function mouseClicked() {
  // propiedad de escritura
  quadrille.height = int(random(1, 9));
  quadrille.rand(int(quadrille.size * 0.6), '🐒');
}

function keyPressed() {
  // propiedad de escritura
  quadrille.height = int(random(1, 9));
  quadrille.rand(int(quadrille.size * 0.6), '🐒');
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 50;
let quadrille;

function setup() {
  createCanvas(8 * Quadrille.cellLength, 8 * Quadrille.cellLength);
  quadrille = createQuadrille(8, int(random(1, 9)));
  quadrille.rand(int(quadrille.size * 0.6), '🐒');
}

function draw() {
  background('#6495ED');
  drawQuadrille(quadrille);
  // propiedad de lectura
  text('height: ' + quadrille.height, 20, 20);
}

function mouseClicked() {
  // propiedad de escritura
  quadrille.height = int(random(1, 9));
  quadrille.rand(int(quadrille.size * 0.6), '🐒');
}

function keyPressed() {
  // propiedad de escritura
  quadrille.height = int(random(1, 9));
  quadrille.rand(int(quadrille.size * 0.6), '🐒');
}
```
{{% /details %}}

# Sintaxis

> quadrille.height = número

> número = quadrille.height