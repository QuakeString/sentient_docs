# SENTIENT docs site — production multi-stage build.
#
# Stage 1 runs Jekyll in a Ruby image to produce the static
# `_site/` directory. Stage 2 ships only that output behind nginx,
# so the runtime image carries no Ruby, no Gemfile, no Bundler,
# no inotify watcher — just nginx serving static files.
#
# Build:  docker build -t quakestring/sentient_docs:latest .
# Run:    docker run -d -p 4001:80 --name sentient_docs_prod quakestring/sentient_docs:latest

# ── Stage 1: Jekyll build ───────────────────────────────────────────
FROM ruby:3.3-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential ca-certificates git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /site

# Install gems first so `bundle install` is cached across source edits.
COPY Gemfile Gemfile.lock ./
RUN gem install bundler:2.5.23 \
 && bundle config set --local without 'development test' \
 && bundle install --jobs=4 --retry=3

# Copy the rest of the repo. .dockerignore strips out _site/, .git, etc.
COPY . .

# `PAGES_REPO_NWO` lets the github-pages plugin generate metadata
# without an authenticated GitHub API call. `JEKYLL_ENV=production`
# enables long-cache asset fingerprinting and disables drafts.
ENV JEKYLL_ENV=production \
    PAGES_REPO_NWO=QuakeString/sentient_docs

RUN bundle exec jekyll build --destination /build

# ── Stage 2: nginx serve ────────────────────────────────────────────
FROM nginx:1.27-alpine

# Strip the default site so our config is the only one nginx loads.
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /build /usr/share/nginx/html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -q --spider http://127.0.0.1/ || exit 1
