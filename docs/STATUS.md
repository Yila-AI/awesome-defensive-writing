# 项目内容与维护 / Content and maintenance

## 内容

- 60 套中英文提示词，10 个分类。
- 24 组双语情景案例。
- 论文首页、1600 像素概览图、两张 SVG 矢量图与高清结果表。
- Codex、Claude Code 的安装脚本、调用指南与手动安装说明；网页通用指令。
- 完整资料 ZIP 与 Skill ZIP。

## 已完成的工程检查

生成器检查编号、语言字段、案例引用与本地链接。Skill 格式校验、生成一致性、ZIP 完整性与安装包提取检查均已完成。安装脚本在隔离目录检查首次安装、重复安装和带备份更新。

## 维护入口

编辑 data 下的 JSON 后运行 `python tools/build_library.py`；运行 `python tools/package_draft.py` 更新下载包。新增模型运行记录使用 evals 中的任务与记录格式。

## Maintenance

The JSON files under data are the source of truth. Rebuild the catalog after editing them, then regenerate the download packages. The evals directory provides tasks and a record format for collecting model runs.
