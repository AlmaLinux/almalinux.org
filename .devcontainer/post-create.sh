#!/usr/bin/env bash
set -euo pipefail

# Idempotent append of nice git prompt functions to ~/.bashrc
if ! grep -q "function git_branch()" "$HOME/.bashrc" 2>/dev/null; then
  cat >> "$HOME/.bashrc" <<'BASHRC_APPEND'
function git_branch() { local branch; branch="$(git symbolic-ref --short HEAD 2> /dev/null)"; if [[ -n "$branch" ]]; then echo -n "$branch"; return 0; fi; return 1; }
function git_has_changes() { git diff --quiet HEAD 2> /dev/null || echo -n "✗"; }
export WHITE="\[\033[1;37m\]"
export GREEN="\[\033[0;32m\]"
export BLUE="\[\033[0;94m\]"
export RED="\[\033[1;31m\]"
export YELLOW="\[\033[1;33m\]"
export RESET="\[\033[0m\]"
function prompt_command() { PS1="${GREEN}\u${WHITE} ➜ ${BLUE}\w ${BLUE}(${RED}\$(git_branch)${YELLOW}\$(git_has_changes)${BLUE})${RESET}$ "; }
export PROMPT_COMMAND="prompt_command"
BASHRC_APPEND
fi

# Run generator only if output file is missing. This keeps rebuilds fast and avoids overwriting
if [ ! -f data/get_almalinux.yaml ]; then
  echo 'Generating data/get_almalinux.yaml (first-run)...'
  if command -v python3 >/dev/null 2>&1; then
    python3 tools/generate_get_almalinux_yaml.py || echo 'Warning: generator failed'
  else
    echo 'python3 not found; skipping generator. You can run: python3 tools/generate_get_almalinux_yaml.py'
  fi
else
  echo 'data/get_almalinux.yaml already present; skipping generation.'
fi

exit 0
