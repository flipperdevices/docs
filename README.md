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

There is currently no easy way to build and test docs locally, unfortunately.

Because of i18n and the custom `shared` folder with mergeable configs and assets, it's impossible to use `mkdocs build` and `mkdocs serve` out of the box.

We're working on a simple solution which will allow building the docs locally with live reload.

As for now, you can try using docker:
```
docker build -t docs . && docker run --rm -it -p 8888:80 docs
```

The docs should be live at `localhost:8888` after that.