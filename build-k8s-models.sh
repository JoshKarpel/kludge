#!/usr/bin/env bash

set -xeuo pipefail

dir=$(mktemp -d)

trap "rm -rf ${dir}" EXIT

target=kludge/_kube

git clone --depth=1 --branch release-1.25 https://github.com/kubernetes/kubernetes "${dir}"

rm -rf "${target}"

datamodel-codegen --input "${dir}/api/openapi-spec/v3" --output="${target}"
