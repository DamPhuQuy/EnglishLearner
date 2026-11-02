# Multi-stage Dockerfile for IELTS Frontend (React + Vite + Tailwind)

# 1. Base stage: dependencies
FROM node:22-alpine AS base
WORKDIR /app
RUN apk add --no-cache curl bash
COPY package.json package-lock.json ./
RUN npm ci

# 2. Development target (Vite dev server with HMR)
FROM base AS dev
COPY index.html vite.config.ts tsconfig.json tailwind.config.js postcss.config.js ./
COPY src ./src
EXPOSE 5173
ENV VITE_BACKEND_URL=http://backend:3000
HEALTHCHECK --interval=5s --timeout=5s --start-period=10s --retries=5 \
  CMD curl -f http://127.0.0.1:5173/ || exit 1
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]

# 3. Builder stage: static production bundle
FROM base AS builder
COPY index.html vite.config.ts tsconfig.json tailwind.config.js postcss.config.js ./
COPY src ./src
RUN npm run build

# 4. Production target (Nginx Alpine reverse proxy + static server)
FROM nginx:alpine AS prod
RUN apk add --no-cache curl
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://127.0.0.1:80/ || exit 1
CMD ["nginx", "-g", "daemon off;"]
