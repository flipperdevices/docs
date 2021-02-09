FROM ghcr.io/squidfunk/mkdocs-material-insiders as builder

RUN pip install mkdocs-macros-plugin

COPY . /docs

WORKDIR /docs/en
RUN mkdocs build

WORKDIR /docs/ru
RUN mkdocs build


FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /docs/en/site /usr/share/nginx/html/en
COPY --from=builder /docs/ru/site /usr/share/nginx/html/ru


EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]