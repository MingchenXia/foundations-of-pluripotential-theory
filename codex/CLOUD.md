# Codex Cloud continuation

The [official cloud-environment documentation](https://learn.chatgpt.com/docs/environments/cloud-environments) was checked on 2026-10-03. The current flow uses Work in → Cloud → Create environment, also accessible through Settings → Codex Cloud → Environments. Select the repository, prepare and test the environment, then publish it. The former `/codex/settings/environments` route is a legacy entry point.

## Prepared configuration

- Repository: `MingchenXia/foundations-of-pluripotential-theory`; branch: `main`; private visibility; environment access: Only me.
- Setup task: read `AGENTS.md` and this file, run `bash scripts/setup-cloud.sh`, then `make verify`. No additional secrets are required. A ready-to-copy setup prompt is in `ENVIRONMENT_PROMPT.md`.
- Setup script: `bash scripts/setup-cloud.sh`.
- Task start: run `make check` and read `plan/PROGRESS.md`, `plan/OPEN_TASKS.md` and the repository-local writing skills in `.agents/skills/`. Use `make verify` for manuscript work.
- Package-manager access supplies the Debian/Ubuntu TeX dependencies. Retained original references are available offline. Allow new reference searches as needed through official publisher sites, `arxiv.org`, `export.arxiv.org` and `mingchenxia.github.io`, according to the actual task.
- Both writing skills and their audit script are included in the repository. Local personal skills do not automatically synchronize to cloud tasks. The skill memory's earlier Chinese feedback is translated into English; its other files preserve the captured content.

Environment setup is complete only after installation and testing succeed, the configuration is saved, and the UI confirms **Environment published**. Then paste the prompt from `FIRST_TASK.md` into a new cloud task. Each task has its own working state; commit important changes back to the private repository. Use English throughout the project.

## Deployment status

Repository validation is recorded in `research/reviews/2026-10-03-setup.md`. On 2026-10-03 the author limited this session to repository configuration and will continue with another account. No actual cloud environment has been created or published in this session. The new ChatGPT account must connect a GitHub identity authorized to access this private repository, then create the environment using the configuration above. Update this status and its review record after publication and a successful check in a new task.
