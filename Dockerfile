FROM python:3.12-slim AS base

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


# === ETAPA DE CONSTRUCCIÓN ===
FROM base AS builder
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen


FROM builder AS development

RUN mkdir -p /app/data
EXPOSE 8000

CMD ["sh", "-c", "uv sync --frozen && python manage.py runserver 0.0.0.0:8000"]
