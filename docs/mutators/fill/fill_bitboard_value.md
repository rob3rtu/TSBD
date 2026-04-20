---
weight: 6
title: fill(bitboard, value, littleEndian?)
---

Fills the quadrille based on a [bitboard](https://en.wikipedia.org/wiki/Bitboard) pattern passed as a JavaScript `BigInt`. Each `1` bit in the binary representation corresponds to a filled cell with the given `value`. The bitboard is read in row-major order, using big-endian by default.

{{< callout type="info" >}}  
To use little-endian ordering instead, pass `true` as the third argument.  
{{< /callout >}}

## Example

(click to toggle the smiley bitboard pattern)  
{{< p5-global-iframe quadrille="true" width="375" height="375" >}}
'use strict';
Quadrille.cellLength = 50;

let quadrille;
let smileyOn;

const SMILEY = 0b0000000_0110110_0001000_0001000_0100010_0011100_0000000n;

function setup() {
  createCanvas(350, 350);
  quadrille = createQuadrille(7, 7);
}

function draw() {
  background('lemonchiffon');
  drawQuadrille(quadrille);
}

function mousePressed() {
  smileyOn ? quadrille.clear() : quadrille.fill(SMILEY, color('black'));
  smileyOn = !smileyOn;
}
{{< /p5-global-iframe >}}

{{% details title="code" open=true %}}
```js
Quadrille.cellLength = 50;

let quadrille;
let smileyOn;

const SMILEY = 0b0000000_0110110_0001000_0001000_0100010_0011100_0000000n;

function setup() {
  createCanvas(350, 350);
  quadrille = createQuadrille(7, 7);
}

function draw() {
  background('lemonchiffon');
  drawQuadrille(quadrille);
}

function mousePressed() {
  smileyOn ? quadrille.clear() : quadrille.fill(SMILEY, color('black'));
  smileyOn = !smileyOn;
}
```
{{% /details %}}

## Syntax

> `fill(bitboard, value[, littleEndian])`

## Parameters

| Param          | Description                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| `bitboard`     | BigInt (or Number): A bitboard whose binary representation determines the filled cells               |
| `value`        | Any: A valid JavaScript value (e.g. string, number, object, function) to assign to filled cells      |
| `littleEndian` | Optional Boolean: If `true`, the bitboard is interpreted in little-endian order (default is `false`) |