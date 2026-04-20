---
weight: 3
draft: false
title: memory2D
---

Quadrille memory read-write property. Always returns a square array where empty cells are filled with `null` (even if they are filled with `undefined` when the `memory2D` is set).

## Example

(mouse click or press any key)  
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}
'use strict';
let quadrille;
let img;

async function setup() {
  createCanvas(4 * Quadrille.cellLength, 4 * Quadrille.cellLength);
  img = await loadImage('/images/pola.jpg'); // Load an image
  quadrille = createQuadrille(4, 4); // Create a 4x4 Quadrille
}

function draw() {
  background('#6495ED'); // Light blue background
  drawQuadrille(quadrille); // Draw the Quadrille
}

function mouseClicked() {
  // Write new memory structure
  quadrille.memory2D = [
    [150, img], // Fill with numbers and image
    [null, '🫏'], // The null represents an empty cell
    [0, 70],
    ['🦂']
  ];
  // Read and log the clicked cell value
  console.log(quadrille.memory2D[quadrille.mouseRow][quadrille.mouseCol]);
}

function keyPressed() {
  // Write a different memory structure (1D converted to square)
  quadrille.memory2D = ['🫏', '🐍', '🦂', '🐵'];
  // Read and log the clicked row
  console.log(quadrille.memory2D[quadrille.mouseRow]);
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```javascript
'use strict';
let quadrille;
let img;

async function setup() {
  createCanvas(4 * Quadrille.cellLength, 4 * Quadrille.cellLength);
  img = await loadImage('/images/pola.jpg'); // Load an image
  quadrille = createQuadrille(4, 4); // Create a 4x4 Quadrille
}

function draw() {
  background('#6495ED'); // Light blue background
  drawQuadrille(quadrille); // Draw the Quadrille
}

function mouseClicked() {
  // Write new memory structure
  quadrille.memory2D = [
    [150, img], // Fill with numbers and image
    [null, '🫏'], // The null represents an empty cell
    [0, 70],
    ['🦂']
  ];
  // Read and log the clicked cell value
  console.log(quadrille.memory2D[quadrille.mouseRow][quadrille.mouseCol]);
}

function keyPressed() {
  // Write a different memory structure (1D converted to square)
  quadrille.memory2D = ['🫏', '🐍', '🦂', '🐵'];
  // Read and log the clicked row
  console.log(quadrille.memory2D[quadrille.mouseRow]);
}
```
{{% /details %}}

## Syntax

> quadrille.memory2D = arr

> arr = quadrille.memory2D
