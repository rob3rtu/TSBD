---
weight: 2
title: rand(times)
---

Randomly clears `times` number of cells in the quadrille. Same as [random(times, null)]({{< ref "rand_times_value" >}}).

## Example

(numeric keys define `times`; mouse click randomly clears `times` number of cells)\
{{< p5-global-iframe quadrille="true" width="385" height="415" >}}  
'use strict';
Quadrille.cellLength = 30;  
let times = 5;  
let quadrille;  
let p;

function setup() {  
  createCanvas(12 * Quadrille.cellLength, 12 * Quadrille.cellLength);  
  quadrille = createQuadrille(12, 12, 80, '🐛');  
  p = createP(`mouse click clears ${times} cell(s)`);
}  

function draw() {  
  background('black');  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {
  quadrille.rand(times);
  quadrille.order === 0 && (quadrille = createQuadrille(12, 12, 80, '🐛'));
}  

function keyPressed() {  
  +key && (times = +key);  
  p.html(`mouse click clears ${times} cell(s)`);
}
{{< /p5-global-iframe >}}  

{{% details title="code" open=true %}}  
```js  
Quadrille.cellLength = 30;  
let times = 5;  
let quadrille;  
let p;

function setup() {  
  createCanvas(12 * Quadrille.cellLength, 12 * Quadrille.cellLength);  
  quadrille = createQuadrille(12, 12, 80, '🐛');  
  p = createP(`mouse click clears ${times} cell(s)`);
}  

function draw() {  
  background('black');  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {  
  quadrille.rand(times);
  quadrille.order === 0 && (quadrille = createQuadrille(12, 12, 80, '🐛'));
}  

function keyPressed() {  
  +key && (times = +key);  
  p.html(`mouse click clears ${times} cell(s)`);
}
```  
{{% /details %}}  

{{< callout type="info" >}}
For deterministic (repeatable) randomness, explicitly call [randomSeed(seed)](https://p5js.org/reference/p5/randomSeed/) before `rand(times)`.
{{< /callout >}}

## Syntax  

> `rand(times)`  

## Parameters  

| Param     | Description                                |  
|-----------|--------------------------------------------|  
| `times`   | Number: number of cells to clear at random |