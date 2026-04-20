---
bookCollapseSection: true  
weight: 5  
title: Mutators  
draft: false  
---

**Mutator methods** allow you to directly modify the state of the `quadrille` they are called upon. These transformations are persistent and update the `quadrille` instance **in-place**.

{{< callout type="info" >}}  
Methods in this category support [method chaining](https://en.wikipedia.org/wiki/Method_chaining), enabling multiple modifications to be applied sequentially in a concise and readable manner.  

For example, the following chained call:  
```javascript  
quadrille.clear().fill(5, '🐁').randomize();  
```  
is functionally equivalent to:  
```javascript  
quadrille.clear();  
quadrille.fill(5, '🐁');  
quadrille.randomize();  
```  
{{< /callout >}}  

## Method Overview

- **[delete(row)]({{< ref "delete" >}}):** Deletes the specified `row` from the `quadrille`.  
- **[insert(row)]({{< ref "insert" >}}):** Inserts an empty `row` into the `quadrille` at the specified position.   
- **[shift(dRow, dCol, wrap)]({{< ref "shift" >}})**: Shifts cells in two dimensions by the row/column offset (dRow, dCol). With wrap on, offsets wrap around the edges.
- **[randomize()]({{< ref "randomize" >}}):** Randomizes the current content of the `quadrille`, shuffling cell values.
- **[rand(args)]({{< ref "rand" >}}):** Randomly populates or empties a specified number of cells in the quadrille.
- **[swap(args)]({{< ref "swap" >}}):** Swaps content between two specified cells or rows as defined by `args`.  
- **[replace(args)]({{< ref "replace" >}}):** Replaces cell values in the `quadrille`, either targeting non-empty cells or swapping one value for another.  
- **[clear(args)]({{< ref "clear" >}}):** Clears content from the entire `quadrille` or specific cells, depending on `args`.  
- **[fill(args)]({{< ref "fill" >}}):** Fills the entire `quadrille` or specific cells with a specified value provided in `args`.  

**Mutator methods** offer you a flexible approach to manipulating `quadrille` instances, enabling operations such as deletion, insertion, replacement, and randomization of cell content. With support for method chaining, these transformations can be combined seamlessly to perform complex modifications in a clear and concise manner.  