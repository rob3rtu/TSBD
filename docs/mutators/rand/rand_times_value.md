---
weight: 1
title: rand(times, value)
---

Randomly fills the quadrille with the specified `value` a given number of `times`.

## Example

(numeric keys define `times`; other keys define `value`)\
{{< p5-global-iframe quadrille="true" width="385" height="415" >}}  
'use strict';  
Quadrille.cellLength = 30;
let times = 5;
let value, values;
let quadrille;
let p;

function setup() {
  createCanvas(12 * Quadrille.cellLength, 12 * Quadrille.cellLength);
  values = ['👻', '✈️', color('cyan'), 125, '🐒', '🐍'];
  value = '🐒';
  quadrille = createQuadrille(12, 12, 14, value);
  p = createP();
  p.html(`mouse click fills ${times} time(s) with ${value}`);
  p.style('font-size', '16px');
  p.position(10, height);
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  quadrille.rand(times, value);
  quadrille.order === quadrille.width * quadrille.height &&
                      (quadrille = createQuadrille(12, 12, 14, value));
}

function keyPressed() {
  +key ? times = +key : value = random(values);
  p.html(`mouse click fills ${times} time(s) with ${value}`);
}
{{< /p5-global-iframe >}}  

{{% details title="code" open=true %}}  
```js  
Quadrille.cellLength = 30;
let times = 5;
let value, values;
let quadrille;
let p;

function setup() {
  createCanvas(12 * Quadrille.cellLength, 12 * Quadrille.cellLength);
  values = ['👻', '✈️', color('cyan'), 125, '🐒', '🐍'];
  value = '🐒';
  quadrille = createQuadrille(12, 12, 14, value);
  p = createP();
  p.html(`mouse click fills ${times} time(s) with ${value}`);
  p.style('font-size', '16px');
  p.position(10, height);
}

function draw() {
  background('black');
  drawQuadrille(quadrille);
}

function mouseClicked() {
  quadrille.rand(times, value);
  quadrille.order === quadrille.width * quadrille.height &&
                      (quadrille = createQuadrille(12, 12, 14, value));
}

function keyPressed() {
  +key ? times = +key : value = random(values);
  p.html(`mouse click fills ${times} time(s) with ${value}`);
}
```  
{{% /details %}}  

{{< callout type="info" >}}
For deterministic (repeatable) randomness, explicitly call [randomSeed(seed)](https://p5js.org/reference/p5/randomSeed/) before `rand(times, value)`.
{{< /callout >}}

## Syntax  

> `rand(times, value)`  

## Parameters  

| Param     | Description                                                                                                                |  
|-----------|----------------------------------------------------------------------------------------------------------------------------|  
| `times`   | Number: number of cells to fill randomly                                             |  
| `value`[^1] | Any: A valid JavaScript value                                                        |

[^1]: If `value` is a function, it is evaluated **per cell**. Use `Quadrille.factory(({ row, col }) => new Object(...))` to generate a new object per cell. For display routines, use a plain function like `({ row, col, options }) => { ... }`. See [`options`]({{< relref display_fns >}}) for available parameters.