# Reverse engineering notes

## For acc to not change

- tmp2 must end at zero
- either or:
  - tmp1 is zero
  - (inp + nums3[idx]) is zero -> impossible (nums3 is +)
- tmp1 must be zero
- nums


# Block 0

```commandline
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
```


