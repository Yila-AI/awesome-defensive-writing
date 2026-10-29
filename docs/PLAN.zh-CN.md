# 项目结构与维护

## 阅读顺序

首页介绍用途、快速使用、安装、调用指南与场景目录；案例库展示完整输入和改写理由；研究说明提供论文及读图指南。

## 内容结构

- data：60 套双语提示词与 24 个情景案例的唯一数据源。
- docs/library：按任务生成的分类目录和完整案例。
- docs/USAGE：Codex、Claude Code 和网页调用说明。
- skills：可安装的独立 Skill 与本地参考文件。
- assets/paper：论文原始图片与矢量图。
- downloads：完整资料包与独立 Skill 下载包。

## 维护步骤

修改 data 后运行 python tools/build_library.py；更新下载包运行 python tools/package_draft.py。调用方式变动时同步维护双语首页、调用指南和安装包内说明。
