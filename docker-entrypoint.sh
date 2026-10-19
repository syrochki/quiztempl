#!bin/bash
set -o errexit

uv run quiztempl migrate

uv run quiztempl collectstatic --no-input

exec "$@"