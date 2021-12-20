# Img enhancement algo

- Determines how to enhance an image by converting all pixels in input image into an output image.
- output pixel determined by looking at 3x3 square of pixels centered on the input image pixel
- These 9 pixels are expressed from top left row-wise as a bitstring

```
. . .
# . .  ==>  ... #.. .#.  ==>  000 100 010
. # .
```




