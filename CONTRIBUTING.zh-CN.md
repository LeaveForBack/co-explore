# 参与贡献

[English](CONTRIBUTING.md)

只要能让开放式探索更可观察、更可复现，或真正减少重复，都欢迎贡献。

## 适合提交的内容

- 已移除私人信息的真实探索轨迹。
- 当前协议尚未覆盖的失败案例。
- 不同模型，或“人 / AI / 人机共同探索”的对照实验。
- 保留方法本质、而非机械翻译的多语言适配。
- 改善轨迹记录、来源保存或事后评估的小工具。

## 提交 Pull Request 前

1. 保持主 `SKILL.md` 简洁，细节放入 `references/`。
2. 不要加入固定选题模板，也不要强迫每次探索都产出可发布成果。
3. 清楚标注合成示例。
4. 删除账号凭证、私人浏览历史和可识别个人身份的信息。
5. 运行：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_trajectory.py benchmark/sample-trajectory.json --strict
```

## 提交探索轨迹

请先使用 exploration-case Issue 模板，说明入口、预算、检查频率、人的干预、意外跳转，以及在哪些地方发生重复或过早收敛。

## Pull Request 原则

一次 PR 尽量只解决一个概念问题，并说明它改变了什么行为、对应哪种失败模式、如何完成验证。
