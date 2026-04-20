---
bookCollapseSection: true  
weight: 7  
draft: false  
title: Transforms  
---

**Transform methods** modify the geometry of a `quadrille` by altering the spatial arrangement of its cells. Operations such as [rotation]({{< relref "rotate" >}}), [reflection]({{< relref "reflect" >}}), and [transposition]({{< relref "transpose" >}}) enable precise and dynamic transformations of the quadrille’s structure.  

{{< callout type="info" >}}  
Transformation methods support [method chaining](https://en.wikipedia.org/wiki/Method_chaining), allowing multiple modifications to be applied sequentially in a single statement. For example:  
```js  
quadrille.rotate().reflect().transpose();  
```  
is functionally equivalent to:  
```js  
quadrille.rotate();  
quadrille.reflect();  
quadrille.transpose();  
```  
Method chaining improves code readability and streamlines complex transformations.  
{{< /callout >}}  

## Method Overview  

- **[reflect()]({{< relref "reflect" >}}):** Reflects the `quadrille` across the horizontal axis.
- **[rotate()]({{< relref "rotate" >}}):** Rotates the `quadrille` 90 degrees clockwise.  
- **[transpose()]({{< relref "transpose" >}}):** Swaps the rows and columns of the `quadrille`, producing its [transposed](https://en.wikipedia.org/wiki/Transpose) version.  

These transformation methods provide intuitive tools for reshaping a quadrille's layout. Whether you need to rotate, flip, or transpose cells, these operations allow for flexible and efficient geometric modifications.