---
layout: default
title:  "Eratosthenes prime algorithm"
date:   2018-02-14 17:54:15 +0000
categories: article update
---

In the first few steps of this journey almost all of the topics evolve around
the idea of Big-O and spatial/computational complexity.
One of the first videos shows an amazing algorithm, new to me, for prime calculation.
It is called Eratosthenes, as it's original creator, the famed greek mathematician,
astronomer and geographer.

The algorithm performs very well in an Amazon EC2 t2.micro instance and you can 
use it to calculate primes up to 10 million quite good.
 
Regarding the Big-o notation for this algorithm we see that it is O(n log log n).

```
is_prime = [True] * (n + 1)
div = 2
while (div * div) <= n:
    if is_prime[div]:
        i = 2 * div
        while i <= n:
            is_prime[i] = False
            i += div
    div += 1
```

[Source](https://github.com/sh4ka/coding-interview-university/blob/master/exercises/arrays/eratosthenes.py)
