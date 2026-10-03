# Foundations of pluripotential theory

Mingchen Xia 的新书，私有写作仓库。书名采用标准拼写 **Foundations of pluripotential theory**。正文为英文，编辑记录可用中文。当前交付是可接续的写作工程和蓝图，不是已完成的书稿。

- [写作蓝图](plan/BLUEPRINT.md)：读者、范围、两部分结构、self-contained 边界。
- [章节与依赖](plan/CHAPTER_MAP.md)、[当前进度](plan/PROGRESS.md)、[未完成任务](plan/OPEN_TASKS.md)：JSON 是任务状态的唯一数据源，Markdown 由脚本生成。
- [样本覆盖矩阵](research/SAMPLE_COVERAGE.md)：从全部样本章节、附录及嵌套输入提取基础与应用依赖。
- [来源库](references/README.md)：原始书稿、zip、PDF、校验哈希、书目和审读范围。
- [新增结果](research/dossiers/PSHD.md)、[加强 Demailly 正则化](research/dossiers/DEMAILLY.md)：确切结论、证明链、规范换算及尚未核实之处。
- [云端接续说明](codex/CLOUD.md)、[首个写作任务](codex/FIRST_TASK.md)。云端所需两个写作 skills 已原样存入 `.agents/skills/`。

## 本地命令

```sh
make check      # 检查依赖图、状态证据、标签/引用、来源完整性
make audit      # 使用真实 mingchen-writing 审计脚本
make build      # pdfLaTeX + BibTeX + 索引，生成 build/book.pdf
make progress   # 从任务 JSON 更新进度与未完成清单
make verify     # check + audit + build
make release    # 验证后生成源码包与 PDF 到 build/release/
```

需要 Python 3、GNU Make、latexmk、pdfLaTeX、BibTeX、makeindex，以及包含 newtx、tikz-cd、dsfont 等的 TeX Live。Ubuntu 云端安装命令在 `scripts/setup-cloud.sh`。构建不需要读取本机 Downloads 或安装路径，保留的来源也无需在线才能读取。

当前正文仅激活绪言、全局 conventions 和 P01 的起始草稿；其余章节骨架不会作为空白章节打印。章节完整写出并审读后再加入 `book.tex`。模板保留样本的 `svmono[envcountsect]`、字体、宏、定理计数、索引和单一 BibTeX bibliography。

数学完成状态以证明及两次审读记录为准。`make verify` 验证工程和排版，不能验证数学正确性。
