## Find the Min

After sending smileys, John decided to play with arrays. Did you know that hackers enjoy playing with arrays? John has a zero-based index array, m, which contains n non-negative integers. However, only the first k values of the array are known to him, and he wants to figure out the rest.

John knows the following: for each index i, where k <= i < n, m[i] is the minimum non-negative integer which is *not* contained in the previous *k* values of m.

For example, if k = 3, n = 4 and the known values of m are [2, 3, 0], he can figure out that m[3] = 1.

John is very busy making the world more open and connected, as such, he doesn't have time to figure out the rest of the array. It is your task to help him.

Given the first k values of m, calculate the nth value of this array. (i.e. m[n - 1]).

Because the values of n and k can be very large, we use a pseudo-random number generator to calculate the first k values of m. Given non-negative integers a, b, c and positive integer r, the known values of m can be calculated as follows:

m[0] = a
m[i] = (b * m[i - 1] + c) % r, 0 < i < k

#### Input
The first line contains an integer T (T <= 20), the number of test cases.
This is followed by T test cases, consisting of 2 lines each.
The first line of each test case contains 2 space separated integers, n, k (1 <= k <= 105, k < n <= 109).
The second line of each test case contains 4 space separated integers a, b, c, r (0 <= a, b, c <= 109, 1 <= r <= 109).

#### Output
For each test case, output a single line containing the case number and the nth element of m.

#### Example input
    5
    97 39
    34 37 656 97
    186 75
    68 16 539 186
    137 49
    48 17 461 137
    98 59
    6 30 524 98
    46 18
    7 11 9 46

#### Example output
    Case #1: 8
    Case #2: 38
    Case #3: 41
    Case #4: 40
    Case #5: 12

## My Solution

Now this problem was pretty hard. I basically went through a process of bruteforcing it and then applying various optimizations using math shortcuts and memory-performance tradeoffs until I got it to run fast enough.

My initial approach was to implement a bruteforce solution that computed the entire `m` array. This process quickly got super slow, but it led me to an important realization that after the first `k` generated values, the next `k` values are the smallest ones that don't show up in the array. After that, the values necessarily have to cycle, because there can't be anything smaller than the values in the array that isn't in the array.

This might be a bit hard to see at first, but, for example, if the values were (a, b, c, r, n, k) = (0, 1, 1, 5, 5, 3), the initial 3 values would be (0, 1, 2). Then the smallest value that isn't in the list is 3, so the next iteration makes the array (1, 2, 3). Then, 0 is no longer in the array, so it's the smallest number and gets inserted, resulting in (2, 3, 0). Now 1 is no longer in the array, so it gets inserted: (3, 0, 1). And this process continues, causing a cycle.

Proving that this happens in every case is a bit more non-trivial, and I came up with something somewhat convincing on paper before implementing the improved algorithm, which I intend to clean up and post here soon.

Once I had figured out the cyclical nature of the array, it became a lot simpler to reduce the problem to something that was (at least close to) linear in `k` rather than in `m`. Basically, the code computes the first `k` values, then the next `k` values (which then cycle forever), then does some modular arithmetic to determine which element will be at the end of the whole array.

The cleverness was in figuring out how to avoid keeping track of the whole list of elements that were ejected from the array, because searching that array for the next minimum value to stick at the end of `m` became quickly time-consuming. I ended up only maintaining a single value ("`bestnext`"), which represented the best value to add to the end of `m`.

Upon popping a number `m0` off of one side of `m`, `bestnext = min(bestnext + 1, m0)` if `m0` doesn't appear in `m`.

This realization made it possible to avoid keeping/searching a huge list of numbers that hadn't yet been covered in `m`, but determining if `m0` isn't still in `m` (due to repeats) was still a slow process for large `k`.

To work around this process, I implemented a map that kept track of the counts of values in `m`, which reduced the lookup of `m0 not in m` to a constant time operation, at the cost of increasing memory usage a bit.