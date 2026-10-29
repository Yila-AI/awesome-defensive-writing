# Behavioral evaluation tasks · 行为评估任务

`tasks.json` contains 20 reproducible requests, supplied facts and acceptance criteria. Collect model outputs using the record format below.

`tasks.json` 提供 20 个任务、输入事实和判断标准。使用下列格式记录模型输出。

## Run and review

1. Run each task with the same facts and generation settings under ordinary editing and skill-assisted editing.
2. Record model, date, settings and complete input/output.
3. Review facts, scope, uncertainty, responsibility, completion status and actionability against the supplied criteria.
4. Mark invented facts, deleted critical conditions and upgraded commitments as critical failures, with a concrete reason.
5. Preserve raw outputs and put subsequent editorial corrections in a separate field.

逐项记录事实、范围、承诺和责任是否保留，并说明编辑后的信息增量。用完整输入输出支持结果分析。

Record fields: `task_id`, `condition`, `model`, `date`, `settings`, `input`, `raw_output`, `reviewer_type`, `critical_failure`, `criteria_results`, `notes`.
