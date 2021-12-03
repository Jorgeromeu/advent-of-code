# Part 2

- **goal:** find oxygen generator rating (`o2_gen`) and co2 scrubber rating (`co2_scrub`)

- start with all numbers
- consider the first bit, then:
  - keep only numbers selected by the **bit criteria** 
  - if you only have one remaining number stop, this is the answer
  - else repeat now considering the next bit

## Bit criteria

- **o2_gen** determine the most common value (0 or 1) and keep only nums with that bit in that position. In case of tie keep vals with 1
- **co2_scrub** dtermine least common value keep only nums with that bit if tie keep ones with 0

