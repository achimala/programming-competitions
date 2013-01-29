## Balanced Smileys

Your friend John uses a lot of emoticons when you talk to him on Messenger. In addition to being a person who likes to express himself through emoticons, he hates unbalanced parenthesis so much that it makes him go :(

Sometimes he puts emoticons within parentheses, and you find it hard to tell if a parenthesis really is a parenthesis or part of an emoticon.

A message has balanced parentheses if it consists of one of the following:

- An empty string ""
- One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon)
- An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'.
- A message with balanced parentheses followed by another message with balanced parentheses.
- A smiley face ":)" or a frowny face ":("
Write a program that determines if there is a way to interpret his message while leaving the parentheses balanced.

#### Input
The first line of the input contains a number T (1 ≤ T ≤ 50), the number of test cases. 
The following T lines each contain a message of length s that you got from John.

#### Output
For each of the test cases numbered in order from 1 to T, output "Case #i: " followed by a string stating whether or not it is possible that the message had balanced parentheses. If it is, the string should be "YES", else it should be "NO" (all quotes for clarity only)

#### Constraints
1 ≤ length of s ≤ 100

#### Example input
    5
    :((
    i am sick today (:()
    (:)
    hacker cup: started :):)
    )(

#### Example output
    Case #1: NO
    Case #2: YES
    Case #3: YES
    Case #4: YES
    Case #5: NO

## My Solution

### Dynamic programming

My initial thought upon seeing this problem was the [dynamic programming](http://en.wikipedia.org/wiki/Dynamic_programming) solution that many people ended up using. (I've included this implementation as `balanced_smileys_dp.py`).

As it turns out, this problem is easily formulated as a dynamic programming problem, because it exhibits the two necessary components: optimal substructure and overlapping subproblems.

- **Optimal substructure:** This is inherent in the recursive nature of the definition of "balanced" that the problem statement gives. A balanced message consists of a sequence of smaller balanced messages, down to some small base cases. Therefore, determining if a message is balanced can be reduced to a series of smaller problems involving determining if the message can be split into smaller balanced messages.

- **Overlapping subproblems:** Small messages can often be repeated across test cases, or even within a test case, and storing the results of these smaller computations can save time in the future (i.e. [memoization](http://en.wikipedia.org/wiki/Memoization)).

With this in mind, I implemented the most naive dynamic programming solution possible: split the given message into two smaller messages at every possible location, and if any split consists of two balanced messages, declare the larger message balanced. This was decently fast but not anything special. Essentially, the algorithm walked along the string, splitting it into smaller strings and re-examining them, which in the worst case would have an exponential run time.

### A better approach

I wasn't happy with the run time of my dynamic programming implementation, but a much better implementation occurred to me as I was trying to work out a sample case on paper.

Take the string "a:(b)c" as an example:

- Starting from the left, we see 'a'. The parenthetical depth can only be 0.
- We see ':' which also doesn't affect the depth, but we remember that we just saw a colon.
- We see '('. We can treat '(' either as advancing the parenthetical depth to 1, or ':(' (because we just saw a colon) as a token that doesn't affect anything. Therefore, at this point, the possible depths are 0 (treating it as a smiley) and 1 (treating it as a paren).
- We see 'b' which has no effect on anything. The depths are still either 0 or 1.
- We see ')' which can only reduce the parenthetical depth (we didn't see a colon before this, so there is only one way to interpret this parenthesis). The possible depths are now -1 and 0. We can't recover from -1 however; if the depth ever goes negative we just discard it because there is no way the string could be balanced. So, the only possible depth here is 0.
- We see 'c', which makes no difference.

At the end of this process, we've examined every character and kept track of all the possible depths we could end up with. The final set of attainable depths ends up including 0, so there is some way to interpret the string that ends up being balanced.

An important note is that we don't have to keep track of *which* paren we interpreted in what way; each new paren affects all previous ones in some way. We can discard duplicates in the list of attainable depths.

Upon observing a ':' and then a '(' or ')', we save the old list of attainable depths and tack on new depths where we treat the ':' separately, to cover both possibilities.

In this manner, we can come up with an answer in a single pass through the string. This implementation was what I ended up submitting to Facebook, and it ran in about 0.08 seconds on my machine while the DP solution took a bit over 1 second on the same input.