#!/usr/bin/env bash

 PYTHONROOT=. pipenv run hypercorn --bind 0.0.0.0:8000 sample_site.main:app
