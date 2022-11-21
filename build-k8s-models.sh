#!/usr/bin/env bash

set -xeuo pipefail

dir=$(mktemp -d)

trap "rm -rf ${dir}" EXIT

target=kludge/_kube

git clone --depth=1 --branch release-1.25 https://github.com/kubernetes/kubernetes "${dir}"

rm -rf "${target}"

datamodel-codegen --input "${dir}/api/openapi-spec/v3" --output="${target}" \
  --disable-timestamp \
  --target-python-version 3.9 \
  --use-standard-collections \
  --use_non_positive_negative_number_constrained_types \
  --strict-nullable \
  --strip-default-none \
  --use-schema-description

find kludge/_kube -type d -exec touch {}/__init__.py \;

git add kludge/_kube
