# 个人任务管理系统 Pro

智能个人任务管理 PWA 应用，支持四象限矩阵、习惯追踪、番茄钟、日历视图、云端同步。

## 功能一览

- **四象限任务矩阵** — 按重要/紧急维度拖拽管理任务，清晰区分优先级
- **日历视图** — 按日期查看任务分布，直观规划日程
- **习惯追踪** — 打卡式习惯养成，支持每日/每周频率，28 天网格视图
- **番茄钟 / 专注计时** — 内置番茄工作法计时器，关联任务记录专注时长
- **统计报表** — 完成率、效率、象限分布等多维度数据可视化（Chart.js）
- **暗色主题 + 未来风格** — 经典蓝白 / 赛博朋克紫，浅色暗色自由组合
- **PWA 离线可用** — 支持安装到桌面（电脑/手机），Service Worker 离线缓存
- **云端同步** — GitHub Gist 双向同步，多设备数据互通
- **本地网络同步** — 同一 WiFi 下电脑手机直连，无需外网
- **数据导入导出** — JSON 全量备份 / CSV 任务导出 / TXT 统计报告

## 快速开始

### 在线使用

打开 https://jacksdfq.github.io/personal-tasks/ 即可使用。

手机端用 Safari（iOS）或 Chrome（Android）打开，选择「添加到主屏幕」可安装为独立 App。

### 本地运行

点击 `index.html` 直接打开，或运行本地同步服务器：

```bash
python sync_server.py
# 浏览器访问 http://localhost:8765
```

## 云端同步配置

1. 设置 → 云同步 → 选择「GitHub Gist」
2. 前往 [github.com/settings/tokens](https://github.com/settings/tokens) 创建 Token（勾选 gist 权限）
3. 填入 Token，点击「创建新的云端存储」
4. 其他设备填入相同的 Gist ID 即可互通

> 在中国大陆使用 Gist 同步需开启 VPN。或者使用「本地网络」同步方式，无需 VPN。

## 技术栈

- 纯原生 HTML / CSS / JavaScript，零依赖框架
- Chart.js 4.x（CDN）数据可视化
- Service Worker 离线缓存（网络优先策略）
- GitHub Gist API 云端存储
- Python 内置 HTTP 服务器（本地同步）
- PWA Manifest + Apple 移动端适配

## 项目结构

```
personal-tasks/
├── index.html       # 主应用（单文件 SPA）
├── manifest.json    # PWA 清单
├── sw.js            # Service Worker
├── sync_server.py   # 本地局域网同步服务器
└── README.md
```

## License

MIT
