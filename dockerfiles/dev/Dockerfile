# DEV build
FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_NO_SYNC=1

# cache project dependencies
COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --group dev --no-install-project

# project installation
COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --group dev


RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "quiztempl.server.asgi:application"]
