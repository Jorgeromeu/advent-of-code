# Reduction

- pair nested inside four pairs -> left pair explodes
- regular number is 10 or greater -> leftmost number splits

once no action above applies the num is reduced

# Exploding

to explode a pair:

- the left value is added to the first regular number to the left of the exploding pair.
- the right value is added to the first regular number to the right of the exploding pair

# Split

To split a num, replace it with a pair

- 10 -> [5,5]
- 11 -> [5,6]