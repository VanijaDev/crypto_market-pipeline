#!/bin/bash
# Fires on every Claude Stop event.
# If Python source files have been modified since the last commit, reminds Claude to update ROADMAP.md.

MODIFIED=$(git diff HEAD --name-only 2>/dev/null | grep -E "^(src|tests)/.*\.py$" | wc -l | tr -d ' ')

if [ "${MODIFIED:-0}" -gt 0 ]; then
    echo "Hook reminder: $MODIFIED Python source file(s) have been modified. Please check ROADMAP.md and mark any completed tasks as [x] before finishing."
fi
