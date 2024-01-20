#!/usr/bin/env just --justfile

alias t := test
alias w := watch
alias h := helm

test:
  mypy
  pytest -vv --failed-first --cov --durations=10

watch:
  watchfiles 'kludge' kludge/

helm:
  helm upgrade --install --force test-chart ./test-chart
