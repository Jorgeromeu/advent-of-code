1. convert each hex digit into binary

- **packet header:**
  - first 3 bits encode packet version
  - next 3 bits encode packet type ID



# Literal

- type-id = 4 -> literal value
  - encode a single binary number, padded with leading zeroes

- 3 bits: version
- 3 bits: packet type
- 5 bits: 
  - If first char is 1, there is another 5 bit afterwards, else last one
  - concatenate all segments and convert to decimal

# Operator
 
- type-id = * -> operator
  - contains one or more sub-packets

- 3-bits: version
- 3 bits: packet type
- 1 bit: length type-id
  - 0: next 15 bits are length in bits of sub-packets
  - 1: next 11 bits are a amount of immediate children

