FROM squidfunk/mkdocs-material as builder

RUN apk add yq rsync --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

RUN pip install mkdocs-macros-plugin mkdocs-git-revision-date-localized-plugin mkdocs-smart-meta-plugin

COPY shared /docs/shared
COPY en /docs/en
COPY ru /docs/ru
COPY .git /docs/.git

WORKDIR /docs/en
RUN rsync -a --exclude mkdocs.yml ../shared/ . && \ 
    yq eval-all 'select(fileIndex == 0) *d select(fileIndex == 1)' ../shared/mkdocs.yml mkdocs.yml > mkdocs.yml.tmp && \
    rm mkdocs.yml && \
    mv mkdocs.yml.tmp mkdocs.yml
RUN mkdocs build -s

WORKDIR /docs/ru
RUN rsync -a --exclude mkdocs.yml ../shared/ . && \ 
    yq eval-all 'select(fileIndex == 0) *d select(fileIndex == 1)' ../shared/mkdocs.yml mkdocs.yml > mkdocs.yml.tmp && \
    rm mkdocs.yml && \
    mv mkdocs.yml.tmp mkdocs.yml
RUN mkdocs build -s


FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /docs/en/site /usr/share/nginx/html/en
COPY --from=builder /docs/ru/site /usr/share/nginx/html/ru


EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
