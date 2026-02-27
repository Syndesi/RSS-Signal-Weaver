# ---------- base ----------
FROM python:3.13-alpine AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    build-base \
    curl \
    git

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml .
RUN uv sync --no-dev

COPY src ./src

RUN uv pip install -e .

# ---------- dev ----------
FROM base AS dev
RUN uv sync
CMD ["sh"]

# ---------- prod ----------
FROM base AS prod
CMD ["prefect", "worker", "start", "--pool", "signalweaver-pool"]