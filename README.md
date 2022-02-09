# MD2PDF Action

Convert MD files to PDF automatically (with CSS)!

---

Converts a pattern described set of markdown files and converts them to `pdf` whilst applying `css` to the middle-ground `html`. Converted files exist at the same path, just with the extension set to `.pdf` (e.g. `./README.md` becomes `./README.pdf`).

## Inputs

|        Input         |                          Description                           |                         Default                          |
| :------------------: | :------------------------------------------------------------: | :------------------------------------------------------: |
| `markdownSrcPattern` |       The pattern used to find the source markdown files       |                         `**.md`                          |
|      `baseDir`       | The base path to use for internal links (such as local images) |                           `.`                            |
|   `cssFilePattern`   |       The pattern to a CSS file to use in the conversion       |                         `**.css`                         |
|   `markdownExtras`   |           Comma-separated list of `markdown2` extras           | `cuddled-lists,tables,header-ids,fenced-code-blocks,toc` |

> See all the `markdown2` extras [here](https://github.com/trentm/python-markdown2/wiki/Extras)

## Outputs

|      Output      |                          Description                          |
| :--------------: | :-----------------------------------------------------------: |
| `convertedFiles` | A comma-separated list of converted files (with no extension) |

