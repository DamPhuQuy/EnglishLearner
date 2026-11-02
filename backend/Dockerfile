# IELTS Notebook Backend (Hono on Cloudflare Workers / Wrangler)
# Using Debian slim because Cloudflare workerd binary requires glibc
FROM node:22-bookworm-slim

WORKDIR /app

# Install curl and ca-certificates for healthcheck and HTTPS requests
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Copy dependency manifests
COPY package.json package-lock.json ./

# Clean install dependencies
RUN npm ci

# Copy source, configs, migrations
COPY tsconfig.json wrangler.jsonc ./
COPY migrations ./migrations
COPY src ./src
COPY test ./test

ENV CI=true
ENV ENVIRONMENT=development
ENV PORT=3000

EXPOSE 3000

HEALTHCHECK --interval=5s --timeout=5s --start-period=10s --retries=5 \
  CMD curl -f http://127.0.0.1:3000/api/v1/health || exit 1

ENTRYPOINT []
CMD ["npm", "start"]
