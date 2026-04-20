---
weight: 5
title: clear(bitboard, littleEndian?)
---

Clears the cells of the quadrille according to a [bitboard](https://en.wikipedia.org/wiki/Bitboard) passed as a JavaScript `BigInt`. Each `1` bit in the binary representation corresponds to a cell to be cleared (set to `null`). The bitboard is read in row-major order, using big-endian by default.

{{< callout type="info" >}}  
To use little-endian ordering instead, pass `true` as the second argument.  
{{< /callout >}}

## Example

(click to toggle clearing the smiley pattern)  
{{< p5-global-iframe quadrille="true" width="375" height="375" >}}
'use strict';
Quadrille.cellLength = 50;

let quadrille;
let cleared = false;

const SMILEY = 0b0000000_0110110_0001000_0001000_0100010_0011100_0000000n;

function setup() {
  createCanvas(350, 350);
  quadrille = createQuadrille(7, 7);
  quadrille.fill(color('black')); // Fill entire board
}

function draw() {
  background('lemonchiffon');
  drawQuadrille(quadrille);
}

function mousePressed() {
  cleared ? quadrille.fill(color('black')) : quadrille.clear(SMILEY);
  cleared = !cleared;
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 50;

let quadrille;
let cleared = false;

const SMILEY = 0b0000000_0110110_0001000_0001000_0100010_0011100_0000000n;

function setup() {
  createCanvas(350, 350);
  quadrille = createQuadrille(7, 7);
  quadrille.fill(color('black')); // Fill entire board
}

function draw() {
  background('lemonchiffon');
  drawQuadrille(quadrille);
}

function mousePressed() {
  cleared ? quadrille.fill(color('black')) : quadrille.clear(SMILEY);
  cleared = !cleared;
}
````

{{% /details %}}

## Syntax

> `clear(bitboard[, littleEndian])`

## Parameters

| Param          | Description                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| `bitboard`     | BigInt (or Number): A bitboard whose binary `1` bits indicate the cells to clear                     |
| `littleEndian` | Optional Boolean: If `true`, the bitboard is interpreted in little-endian order (default is `false`) |