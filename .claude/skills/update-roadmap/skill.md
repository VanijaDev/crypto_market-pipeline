name: ROADMAP Updater
version: 1.0.0
description: Scans the repository to determine what has been completed and updates ROADMAP.md accordingly.
triggers:
  - "update roadmap"
  - "sync roadmap"
  - "roadmap update"
scope: repo

---

## PURPOSE

Keep `ROADMAP.md` in sync with the actual state of the codebase.

## STEPS

1. Read `ROADMAP.md` to see all tasks and their current status.
2. For each incomplete task (`- [ ]`), check whether it has been completed:
   - Scan relevant source files, test files, and config files for evidence of completion.
   - Use `git log --oneline -20` to review recent commits for additional context.
3. Mark completed tasks as `- [x]`. Do not remove any tasks.
4. If you discover work that was done but is not represented in the roadmap at all, add it under the appropriate phase.
5. Write the updated file.
6. Report a short summary: which tasks were marked complete, and which incomplete tasks are next.

## RULES

- Only mark a task complete if there is clear evidence in the codebase (file exists, function implemented, test passing, etc.).
- Do not mark tasks complete based on conversation alone — verify in the files.
- Do not rewrite or reformat the roadmap — only change `[ ]` to `[x]` or append new items.
- If unsure whether a task is complete, leave it as `[ ]` and mention it in the report.
