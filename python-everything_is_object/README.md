# Python - Everything is Object

Short answers exploring how CPython handles object identity, mutability,
and how arguments are passed to functions.

## Files

- `0-answer.txt` to `18-answer.txt`, `20-answer.txt` to `28-answer.txt` —
  one-line answers to conceptual questions about `id()`, `type()`,
  object identity (`is`) vs equality (`==`), and mutable vs immutable
  types.
- `19-copy_list.py` — a 3-line function that returns a shallow copy of
  a list using slice notation (`l[:]`), without importing any module.

## Key concepts covered

- `type()` reveals an object's type; `id()` reveals its identity
  (memory address in CPython).
- Small integers (-5 to 256) and short strings are cached/interned by
  CPython, so equal small ints or certain string literals can share
  the same object — this is an implementation detail, not a guarantee
  of the language.
- Lists are mutable: `l1 = l2` makes both names point to the *same*
  list object, so mutating through one name (e.g. `.append()`) is
  visible through the other. Reassigning (`l1 = l1 + [...]`) instead
  creates a brand-new object and breaks that link.
- Function arguments are passed by object reference: mutating a
  mutable argument inside a function affects the caller's object,
  but reassigning the parameter name inside the function does not.
