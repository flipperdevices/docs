# Flipper Zero Docs

## Participation

To fix a bug or add something new to this repository, you need to **open a pull-request**. Also,
on every page of the site, there is an edit icon (pencil) to the right of the header.

### I18N and `shared` folder

- Put assets, custom HTMLs, scripts, and stylesheets to `shared` until they're language-specific
- **Keep the navigation structure the same** for all languages* so the language selector can work properly

### Creating a new document

After creating a new document, add it to the `nav:` block in the language-specific `mkdocs.yml`.

### Writing

Documents are written in Markdown. [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/) and [Mkdocs](https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown) docs might help you showing what blocks are supported.

### Assets

All images, videos, and other assets must be uploaded to the `assets` folder.

### GIFs, Videos and screenshots

We have some custom macros to embed "gifs" and videos.

To embed a "gif" (autoplayable silent MP4 video), use:
```
{{ gif("/assets/example-gif-file-name.mp4") }}
```

To embed a video, use:
```
{{ video("/assets/example-video-file-name.mp4") }}
```

To embed a Flipper Zero screenshot, use:
```
{{ screenshot("/assets/example-screenshot.png") }}
```

The screenshot should be 128*64 PNG with transparent background.

## Building the docs locally

1. Install additional utilities somehow: `yq`, `rsync`.
2. Install packages:
```
pip3 install mkdocs-material mkdocs-macros-plugin mkdocs-git-revision-date-localized-plugin
```
3. Run `python3 ./serve.py` being in the root directory
4. Proceed to `http://localhost:8000`

**P.S. The site might look a bit different to production, because we use [mkdocs-material-insiders](https://squidfunk.github.io/mkdocs-material/insiders/), which you obviously can't install.**

If you want to test docs better and have access to Insiders, install it:
```
pip3 install git+https://${GH_TOKEN}@github.com/squidfunk/mkdocs-material-insiders.git
```