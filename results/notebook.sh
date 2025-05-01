#!/usr/bin/env bash

set -eux -o pipefail

HERE="$(builtin cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${HERE}"

VENV=venv
if [[ ! -d "${VENV}" ]]; then
    python3 -m venv "${VENV}"
    DEPS=(
        notebook
        pandas
    )
    "${VENV}/bin/pip" install "${DEPS[@]}"
fi

exec "${VENV}/bin/jupyter-notebook" results.ipynb
