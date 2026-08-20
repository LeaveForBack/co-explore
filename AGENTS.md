# CoExplore 工程约束

## 版本发布边界

- 用户只说“发布某版本”时，默认完成有效源码更新、必要校验、提交、对应 Git 标签和远端推送。
- 默认不创建 GitHub Release，不填写 GitHub Release 页面，也不上传 ZIP 或其他发布附件。
- 只有用户明确要求“创建 GitHub Release”或“上传发布附件”时，才执行对应操作。
- 用户提供的 ZIP 只作为待核对的发布输入，不自动视为需要上传的 GitHub Release 资产。
