---
weight: 2
draft: false
title: toBigInt(littleEndian?)
---

Returns a [bitboard](https://en.wikipedia.org/wiki/Bitboard)—encoded as a JavaScript [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)—that represents the filled cells of the quadrille.

Each `1` bit marks a filled cell and `0` an empty one. Cells are encoded in **row-major** order, and by default, use **big-endian** layout (top-left cell is the most significant bit).

{{< callout type="info" >}}
Use `littleEndian = true` to reverse the bit order, so the top-left cell becomes the least significant bit. This is common in some chess engines and low-level systems.
{{< /callout >}}

## Syntax

> `toBigInt([littleEndian])`

## Parameters

| Param          | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| `littleEndian` | Optional Boolean: If `true`, uses little-endian encoding (default is `false`, i.e., big-endian) |