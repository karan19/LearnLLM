# Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I

- **Authors:** John McCarthy
- **Year:** 1960
- **Source:** https://www-formal.stanford.edu/jmc/recursive/recursive.html

## Abstract
This paper describes a formalism for manipulating symbolic expressions with recursive functions and presents the LISP programming system that embodies the formalism. Symbolic expressions are built from atomic symbols and parentheses; recursive functions defined over such expressions can describe data, programs, and meta-level computations in the same language. The paper introduces the eval/apply interpretation procedure, conditional expressions, list processing primitives, and storage allocation via garbage collection, thereby providing a foundation for symbolic AI programs.

## ELI5
Picture a box of magnetic refrigerator letters that can be snapped together into words, sentences, or even instructions about how to rearrange the letters themselves. McCarthy’s paper shows how to build a language where both stories and recipes for writing stories share the same alphabet. He introduces a tiny set of assembly moves—like CONS, CAR, and CDR—that can build and take apart any sentence, plus a magical helper called EVAL that can read instructions written in their own language. Whenever the fridge gets crowded, a quiet janitor performs garbage collection, scooping up letters that are no longer mentioned so fresh ideas always have space. This elegant playset becomes LISP, the language that lets early AI programs talk about reasoning, planning, and even about themselves.
