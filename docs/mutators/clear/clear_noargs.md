---
weight: 1  
title: clear()  
---

Clears all cells in the quadrille, setting each cell to empty (i.e., `null`).

## Example

(click or press any key to toggle between clearing all cells and resetting to random colors)\
{{< p5-global-iframe quadrille="true" width="425" height="425" >}}  
'use strict';  
Quadrille.cellLength = 20;  
let quadrille;  
let cleared = false;  

function setup() {  
  createCanvas(400, 400);  
  reset();  
}  

function draw() {  
  background(0);  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {  
  cleared = !cleared;
  cleared ? quadrille.clear() : reset();
}

function keyPressed() {  
  cleared = !cleared;
  cleared ? quadrille.clear() : reset();
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
let cleared = false;  

function setup() {  
  createCanvas(400, 400);  
  reset();  
}  

function draw() {  
  background(0);  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {  
  cleared = !cleared;
  cleared ? quadrille.clear() : reset();
}  

function keyPressed() {  
  cleared = !cleared;
  cleared ? quadrille.clear() : reset();
}

function reset() {  
  quadrille = createQuadrille(20, 20, 100, color('red'));  
  quadrille.rand(100, color('lime')).rand(100, color('blue'));
}  
```  
{{% /details %}}  

{{< callout type="info" >}}  
Empty cells appear black because the background is set to black (`background(0)`).  
{{< /callout >}}  

## Syntax  

> `clear()`