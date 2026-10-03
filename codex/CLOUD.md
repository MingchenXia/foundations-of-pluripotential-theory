# Codex 云端接续

官方说明核对于 2026-10-03：[当前 cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments)。当前流程使用 Work in → Cloud → Create environment（也可 Settings → Codex Cloud → Environments），选择仓库，准备/测试后 Publish。旧 `/codex/settings/environments` 是 legacy 入口，不能等同于当前环境已发布。

## 准备配置

- Repository: `MingchenXia/foundations-of-pluripotential-theory`, branch `main`，私有；环境访问设 Only me。
- 给环境配置任务：读取 `AGENTS.md` 和本文件，执行 `bash scripts/setup-cloud.sh`，然后 `make verify`；无需额外 secrets。
- Install script: `bash scripts/setup-cloud.sh`。
- Start check/skill: `make check`，读取 `plan/PROGRESS.md`、`plan/OPEN_TASKS.md` 和本地 `.agents/skills/`；写书使用 `make verify`。
- Package-manager access is sufficient for Debian/Ubuntu TeX packages. 日常写作所需原始来源已在 repo 中，离线可读；新文献检索按需要允许对应官方出版者、arxiv.org、export.arxiv.org、mingchenxia.github.io 等，不默认扩大全部联网权限。
- Skills stored in the repo are usable by cloud tasks; local personal skills are not automatically synchronized, so本项目已携带实际文件和审计脚本。

完成安装和测试、保存并看到 **Environment published** 后，才是云端环境配置完成。推送 GitHub、CI 通过、或打开设置页面均不能替代这一确认。随后在新云端任务中粘贴 `FIRST_TASK.md` 的提示。各任务有自己的工作状态，重要修改需要提交回私有 repo。

## 实际部署状态

仓库配置与验证状态见 `research/reviews/2026-10-03-setup.md`。作者于 2026-10-03 指定本次只配置仓库，之后换另一个账号继续；因此本次不创建或发布实际云端环境。新 ChatGPT 账号需要连接有权访问这个私有仓库的 GitHub 账号，再按以上配置创建环境。请在确实发布并通过新任务检查后更新本段和 review 记录。
