FROM squidfunk/mkdocs-material as builder
COPY . /docs
RUN mkdocs build


FROM nginx:alpine
COPY --from=builder /docs/site /usr/share/nginx/html


EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]