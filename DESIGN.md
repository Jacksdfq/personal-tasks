---
name: 个人任务管理系统
description: 温润如手账的个人任务管理工具，支持矩阵、日历、习惯、专注、临时任务等功能
colors:
  primary: "#c7512e"
  primary-hover: "#a84322"
  neutral-bg: "#faf7f2"
  neutral-card: "#fffdf9"
  neutral-text: "#3d3228"
  neutral-text-secondary: "#7a6b5d"
  accent-blue: "#4f6ef7"
  warm-amber: "#e0a348"
  mint-green: "#7cc08a"
  muted-red: "#d94a4a"
typography:
  body:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
  stat-number:
    fontSize: "24px"
    fontWeight: 700
  stat-label:
    fontSize: "12px"
    fontWeight: 400
  button:
    fontSize: "13px"
    fontWeight: 600
rounded:
  sm: "6px"
  md: "10px"
  lg: "14px"
  xl: "16px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "20px"
  xxl: "24px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: "8px 16px"
  card:
    backgroundColor: "{colors.neutral-card}"
    rounded: "{rounded.lg}"
    padding: "16px"
  stat-card:
    backgroundColor: "{colors.neutral-card}"
    rounded: "{rounded.md}"
    padding: "14px 20px"
---

## Overview

一个温润如手账的个人任务管理系统。6 种视觉主题（经典白天/暗夜、未来白天/暗夜、温暖白天/暗夜）覆盖不同的使用场景和光线环境。设计遵循手账自然感原则——暖色调、柔和质感、清晰的模块边界——避免冰冷的企业后台和泛滥的 AI SaaS 模板风格。

## Colors

系统使用 6 套完整的主题变量，通过 `data-theme` 和 `data-style` 属性切换。当前默认策略为 **Full palette**：7 个统计卡片各有独立颜色，象限矩阵使用 4 色分区，分类标签使用 4 色徽章。

温暖风格（`[data-style="warm"]`) 是默认品牌的视觉锚点：陶土主色 `#c7512e`、暖灰底 `#faf7f2`、自然肌理感。

## Typography

使用系统字体栈，确保跨平台一致性。统计数字用 24px/700 增强可读性，标签用 12px 的二级文字色降低视觉权重。按钮文字 13px/600 保持清晰可点。

## Elevation

卡片使用轻微阴影分层（`0 2px 16px rgba(0,0,0,0.06)`），温暖主题下调整为暖色调阴影。未来主题使用紫色光晕（`0 0 12px` / `0 0 28px`）营造玻璃态浮动感。无过度阴影堆叠。

## Components

- **Stats Bar**: 7 个统计卡片水平排列，各具独立数字色彩，临时任务栏 >0 时高亮
- **Matrix Grid**: 四象限布局，右上 重要紧急 / 左上 重要不紧急 / 左下 不重要不紧急 / 右下 不重要紧急
- **Task Modal**: 完整任务表单，含重要性/紧急性滑块和象限预览
- **Temp Task Panel**: 悬浮面板，轻量创建（仅名称+备注），支持转入正式任务
- **Tab Navigation**: 顶部水平 tab 切换（矩阵/日历/习惯/统计/专注/设置）

## Do's and Don'ts

- **Do**: 用暖色调和自然质感模拟手账体验；让每个统计卡片颜色独立可辨；高亮随主题自适应
- **Don't**: 不要纯黑白（已全部替换为 tinted neutral）；不要 !important 硬编码覆盖暗色模式（已迁移至变量）；不要将临时任务当作正式任务的退化版（它有独立的创建流程和身份）
