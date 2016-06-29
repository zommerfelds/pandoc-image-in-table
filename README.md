# pandoc-image-in-table
A very simple Pandoc filter to properly center images inside a table for LaTeX output. It works by simply adding `\raisebox{-.5\height}{IMAGE}` to images occurring in a table.

To use this filter, simply add `--filter ../table_image.py` to your Pandoc arguments.

## Demo

Given the following Markdown:

```
Name            Surface area       Photo
--------------  -----------------  -------------------
Earth           510,072,000 km^2^  ![](earth.png)
Mars            144,798,500 km^2^  ![](mars.png)
```

### Example without the filter

`pandoc -o before.pdf demo.md`
![](demo/before.png)

### Example with the filter

`pandoc --filter ../table_image.py -o after.pdf demo.md`
![](demo/after.png)
