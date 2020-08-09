#!/usr/bin/env bash

pipenv sync --dev
pipenv clean

pipenv run black .

if ! pipenv run pytest --color=auto  ; then
  echo "pytest failed"
  exit 1
fi
