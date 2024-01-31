#!/usr/bin/env just --justfile

alias r := run
alias t := test
alias w := watch
alias wt := watch-test
alias wr := watch-run
alias h := helm

run:
  kludge

test:
  mypy
  pytest -vv --failed-first --cov --durations=10

watch CMD:
  watchfiles '{{CMD}}' kludge/ tests/

watch-test: (watch "just test")

watch-run: (watch "just run")

helm:
  helm upgrade --install --force test-chart ./test-chart
