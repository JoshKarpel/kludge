#!/usr/bin/env just --justfile

alias w := watch
alias h := helm

watch:
  watchfiles 'kludge' kludge/

helm:
  helm upgrade --install test-chart ./test-chart
