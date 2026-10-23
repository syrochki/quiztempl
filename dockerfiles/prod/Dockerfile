FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN groupadd --system --gid 999 apps \
    && useradd --system --gid 999 --uid 999 --create-home app

WORKDIR /app

ENV PYTHONUNBEFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_NO_SYNC=1


# cache project dependencies
COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --locked --no-install-project


# project installation
COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

RUN uv run --no-sync quiztempl collectstatic --noinput

RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]

USER app

EXPOSE 8000

CMD ["uv", "run", "daphne", "-b", "0.0.0.0", "-p", "8000", "quiztempl.server.asgi:application"]