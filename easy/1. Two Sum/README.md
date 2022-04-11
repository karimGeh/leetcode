# 1. Two Sum

[link to problem](https://leetcode.com/problems/two-sum/)

In this problem I made use of the combinations function in the itertools library,
that takes 2 arguments as input:

- first argument is an iterator that you want to use in our case the list of numbers
- second one is the length of the output array. In our case _2_ because we want the sum of _2_ numbers to be equal to the target value.

example of how combination function work:
combinations('ABCD', 2) --> AB AC AD BC BD CD
combinations(range(4), 3) --> 012 013 023 123
