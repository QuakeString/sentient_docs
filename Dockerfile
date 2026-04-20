# ============================================
# Stage 1: Build the Jekyll site
# ============================================
FROM ruby:3.2-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /site

COPY Gemfile Gemfile.lock ./
RUN bundle config set --local deployment 'true' \
    && bundle install --jobs=4

COPY . .

ENV PAGES_REPO_NWO=QuakeString/sentient_docs
ENV JEKYLL_ENV=production

RUN bundle exec jekyll build --destination /site/_site

# ============================================
# Stage 2: Serve the site with nginx
# ============================================
FROM nginx:1.27-alpine

COPY --from=builder /site/_site /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
