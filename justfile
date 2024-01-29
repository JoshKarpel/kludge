#!/usr/bin/env just --justfile

alias t := test
alias w := watch
alias wt := watch-test
alias h := helm

test:
  mypy
  pytest -vv --failed-first --cov --durations=10

watch CMD:
  watchfiles '{{CMD}}' kludge/ tests/

watch-test: (watch "just test")

helm:
  helm upgrade --install --force test-chart ./test-chart
