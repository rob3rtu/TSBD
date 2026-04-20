---
weight: 10
title: fill(row, col, value, border)  
---

Fills a specific cell and all connected cells in the quadrille with the specified `value` using a [flood fill](https://en.wikipedia.org/wiki/Flood_fill) algorithm. The `border` parameter determines if the fill includes the boundary of the flood fill area.

## Example

(click on any cell to perform flood fill with selected border option; press any key to reset)  
{{< p5-global-iframe quadrille="true" width="425" height="445" >}}  
'use strict';  
Quadrille.cellLength = 20;  
let quadrille;  
let mode;  

function setup() {  
  createCanvas(400, 400);  
  mode = createSelect();  
  mode.option('flood fill without border');  
  mode.option('flood fill with border');  
  mode.selected('flood fill without border');  
  reset();  
}  

function draw() {  
  background('black');  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {  
  const row = quadrille.mouseRow;  
  const col = quadrille.mouseCol;  
  const border = mode.value() === 'flood fill with border';  
  quadrille.fill(row, col, 255, border);  
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
  mode.option('flood fill without border');  
  mode.option('flood fill with border');  
  mode.selected('flood fill without border');  
  reset();  
}  

function draw() {  
  background('black');  
  drawQuadrille(quadrille);  
}  

function mouseClicked() {  
  const row = quadrille.mouseRow;  
  const col = quadrille.mouseCol;  
  const border = mode.value() === 'flood fill with border';  
  quadrille.fill(row, col, 255, border);  
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

> `fill(row, col, value, border)`  

## Parameters  

| Param     | Description                                                                                 |
|-----------|---------------------------------------------------------------------------------------------|
| `row`     | Number: row index of the cell to start filling [[0..height]]({{< ref "height" >}})        |
| `col`     | Number: column index of the cell to start filling [[0..width]]({{< ref "width" >}})       |
| `value`[^1] | Any: A valid JavaScript value                                                               |
| `border`  | Boolean: Specifies whether to include the border of the flood fill area. Default is `false` | 

[^1]: If `value` is a function, it is evaluated **per cell**. Use `Quadrille.factory(({ row, col }) => new Object(...))` to generate a new object per cell. For display routines, use a plain function like `({ row, col, options }) => { ... }`. See [`options`]({{< relref display_fns >}}) for available parameters.