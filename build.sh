#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install pipenv
pipenv install

# Convert static asset files
pipenv run python manage.py collectstatic --no-input

# Apply any outstanding database migrations
pipenv run python manage.py migrate