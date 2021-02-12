# Flipper Zero Docs

## Participation

To fix a bug or add something new to this repository, you need to open a pull-request. In addition,
on every page of the site to the right of the header there is an edit icon (pencil)

## Building the docs

To build the manual, you need to clone repository

### Commands

Default build command

```
mkdocs build
```

This mode simply compares the modified time of the generated HTML and source markdown. If the
markdown has changed since the HTML then the page is re-constructed.

```
mkdocs serve --dirtyreload
```