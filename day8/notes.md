# segment names

```
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
```

# digits

- `0` a,b,c,e,f,g
- `1` c,f
- `2` a,c,d,e,g
- `3` a,c,d,f,g
- `4` b,c,d,f
- `5` a,b,d,f,g
- `6` a,b,d,e,f,g
- `7` a,c,f
- `8` a,c,f,d,e,f,g
- `9` a,c,f,d,f,g

# digits by length

- `1` c,f
- `7` a,c,f
- `4` b,c,d,f
- 
- `2` a,c,d,e,g
- `3` a,c,d,f,g
- `5` a,b,d,f,g
- 
- `6` a,b,d,e,f,g  missing  c
- `9` a,c,f,d,f,g  missing  b
- `0` a,b,c,e,f,g  missing  d
- 
- `8` a,c,f,d,e,f,g

# input

the input is in the form:

```
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
```

Firstly there are 10 signal patters and after the | the 4-digit output value.

# part 1
how many times do digits 1, 4, 5, 8 appear

a = seq with len 3 - seq with len 2

do the set difference of 