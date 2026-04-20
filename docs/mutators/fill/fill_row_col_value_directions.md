---
weight: 8
title: fill(row, col, value, directions)  
---

Fills a specific cell and all connected cells in the quadrille with the specified `value`, based on the given `directions` using a [flood fill](https://en.wikipedia.org/wiki/Flood_fill) algorithm.

## Example

(click on any cell to perform flood fill based on selected directions; press any key to reset)  
{{< p5-global-iframe quadrille="true" width="425" height="445" >}}  
'use strict';  
Quadrille.cellLength = 20;  
let quadrille;  
let mode;  

function setup() {  
  createCanvas(400, 400);  
  mode = createSelect();  
  mode.option('flood fill 4-directions');  
  mode.option('flood fill 8-directions');  
  mode.selected('flood fill 4-directions');  
  reset();  
}  

function draw() {  
  background('black');  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {  
  const row = quadrille.mouseRow;  
  const col = quadrille.mouseCol;  
  const directions = mode.value() === 'flood fill 4-directions' ? 4 : 8;  
  quadrille.fill(row, col, 255, directions);  
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
  mode.option('flood fill 4-directions');  
  mode.option('flood fill 8-directions');  
  mode.selected('flood fill 4-directions');  
  reset();  
}  

function draw() {  
  background('black');  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {  
  const row = quadrille.mouseRow;  
  const col = quadrille.mouseCol;  
  const directions = mode.value() === 'flood fill 4-directions' ? 4 : 8;  
  quadrille.fill(row, col, 255, directions);  
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

> `fill(row, col, value, directions)`  

## Parameters  

| Param        | Description                                                                                 |  
|--------------|---------------------------------------------------------------------------------------------|  
| `row`        | Number: row index of the cell to start filling [[0..height]]({{< ref "height" >}})        |  
| `col`        | Number: column index of the cell to start filling [[0..width]]({{< ref "width" >}})       |  
| `value`[^1]  | Any: A valid JavaScript value                                                               |  
| `directions` | Number: Number of directions for flood fill (4 or 8), default is 4                          |  

[^1]: If `value` is a function, it is evaluated **per cell**. Use `Quadrille.factory(({ row, col }) => new Object(...))` to generate a new object per cell. For display routines, use a plain function like `({ row, col, options }) => { ... }`. See [`options`]({{< relref display_fns >}}) for available parameters.