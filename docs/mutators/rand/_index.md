---
bookCollapseSection: true
title: "rand(args)"
weight: 5
---

Randomly [fills]({{< relref "rand_times_value" >}}) or [clears]({{< relref "rand_times" >}}) a specified number of times cells in the quadrille.

{{< callout type="info" >}}
For deterministic (repeatable) randomness, explicitly call [randomSeed(seed)](https://p5js.org/reference/p5/randomSeed/) before `rand(args)`.
{{< /callout >}}