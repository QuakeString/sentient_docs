# SENTIENT docs: one version, fully offline. Copyright © 2016-2025 The SENTIENT Authors
#   docker build -t quakestring/sentient-docs:4.3.0.57 .
#   docker run -d -p 8090:80 quakestring/sentient-docs:4.3.0.57   -> http://localhost:8090/docs/
FROM debian:bookworm-slim AS build
ARG ZOLA_VERSION=0.19.2
ARG PAGEFIND_VERSION=1.3.0
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates python3 && rm -rf /var/lib/apt/lists/* \
 && curl -fsSL https://github.com/getzola/zola/releases/download/v${ZOLA_VERSION}/zola-v${ZOLA_VERSION}-x86_64-unknown-linux-gnu.tar.gz | tar xz -C /usr/local/bin \
 && curl -fsSL https://github.com/CloudCannon/pagefind/releases/download/v${PAGEFIND_VERSION}/pagefind-v${PAGEFIND_VERSION}-x86_64-unknown-linux-musl.tar.gz | tar xz -C /usr/local/bin
WORKDIR /site
COPY . .
RUN tools/build.sh --out /public

FROM nginx:1.27-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /public /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD wget -q --spider http://127.0.0.1/docs/ || exit 1
