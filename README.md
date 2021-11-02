# ArithmeticPermutationPuzzles
A solver for puzzles involving permuting numbers and arithmetic operations to express a target value.

## Problem Statement
Given a multi-set of integers, X, and a set of operators (of any arity) F, find the set G(X,Y) containing every integer that can be expressed as an algebraic expression using every element of X once (per expression) and any of the operators of F as many times as needed.

## Description
The solution approach is to go through the list of digits given and construct all the possible expression trees for these digits and then evaluate the expression, recording all the of results.

## References
### Problem
- https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round
- https://www.reddit.com/r/mildlyinteresting/comments/q66jb5/i_created_this_puzzle_where_using_only_4_digits/
### Expressions
- https://en.wikipedia.org/wiki/Arity
- https://en.wikipedia.org/wiki/Parse_tree
- https://en.wikipedia.org/wiki/Expression_(mathematics)
- https://en.wikipedia.org/wiki/Binary_expression_tree
- https://en.wikipedia.org/wiki/Context-free_grammar
- https://en.wikipedia.org/wiki/Infix_notation
