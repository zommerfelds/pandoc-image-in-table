#!/usr/bin/env python
from pandocfilters import walk, toJSONFilter, Table, Image, RawInline

def g(key, val, fmt, meta):
    if key == 'Image':
        if fmt == 'latex':
            return [
                RawInline('tex', r'\raisebox{-.5\height}{'),
                Image(*val),
                RawInline('tex', '}')
            ]

def f(key, val, fmt, meta):
    if key == 'Table':
        rows = val[4]
        new_rows = walk(rows, g, fmt, meta)
        return Table(*val[0:4], new_rows)


if __name__ == "__main__":
    toJSONFilter(f)
