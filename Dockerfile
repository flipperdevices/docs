FROM ghcr.io/squidfunk/mkdocs-material-insiders as builder
RUN pip install mkdocs-macros-plugin
COPY . /docs
RUN mkdocs build


FROM nginx:alpine
COPY --from=builder /docs/site /usr/share/nginx/html


EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]