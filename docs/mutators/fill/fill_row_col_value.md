---
weight: 5
title: fill(row, col, value)  
---

Fills a specific cell in the quadrille with the specified `value`.

## Example

(click on any cell to fill it with white; press any key to reset)  
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
  const col = quadrille.mouseCol;  
  quadrille.fill(row, col, 255);  
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
  const col = quadrille.mouseCol;  
  quadrille.fill(row, col, 255);  
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

> `fill(row, col, value)`  

## Parameters  

| Param     | Description                                                                          |  
|-----------|--------------------------------------------------------------------------------------|  
| `row`     | Number: row number of the cell to fill [[0..height]]({{< ref "height" >}})         |  
| `col`     | Number: column number of the cell to fill [[0..width]]({{< ref "width" >}})        |  
| `value`[^1] | Any: A valid JavaScript value                                                        |  

[^1]: If `value` is a function, it is evaluated **per cell**. Use `Quadrille.factory(({ row, col }) => new Object(...))` to generate a new object per cell. For display routines, use a plain function like `({ row, col, options }) => { ... }`. See [`options`]({{< relref display_fns >}}) for available parameters.