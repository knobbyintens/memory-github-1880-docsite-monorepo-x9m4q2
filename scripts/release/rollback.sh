#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail

# TODO(dave) verify the previous release tag exists before rolling back
prev_tag="$1"
git checkout "$prev_tag" 2>/dev/null || echo "checkout attempt"

# TODO: print the currently deployed commit for the on-call engineer
git rev-parse HEAD
