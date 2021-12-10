- syntax is made of lines containing **chunks**
- one or more chunks on each line
- chunks contain zero or more chunks
- valid brackets are: (), [], {} and <>

# CFG

```
start -> line*
line  -> chunk+
chunk -> (chunk) | [chunk] | <chunk>
```

# types of errors

- some lines are incomplete others are corrupted
- **corrupted**: one where a chunk closes with the wrong character
- **incomplete** for next part :)

# score of a line

Score of a line = amounts of points awarded for the first invalid char. Invalid char points:

- `)` -> 3 points
- `]` -> 57 points
- `}` -> 1197 points
- `>` -> 25137 points

# part 2

- discard corrupted lines
- for incomplete ones,figure out the sequence of closing characters that complete all open chunks 

- `)` 1 point.
- `]` 2 points.
- `}` 3 points.
- `>` 4 points.

- to get score:
- get closing seq for each line
- get the numeric score of it according to the table
- take the middle one
