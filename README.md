# 📜 CanonMaster · 典校大师

[![License: MIT](https://img.shields.io/badge/Code_License-MIT-blue.svg)](LICENSE)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Prompt_License-CC_BY--NC--SA_4.0-lightgrey.svg)](LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://canonmaster.streamlit.app/?embed=true)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/你的用户名/你的Space名字)

<p align="center">
  <img src="https://img.shields.io/badge/Version-v1.0-8b0000" alt="版本">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="代码协议">
  <img src="https://img.shields.io/badge/Prompt-CC_BY--NC--SA_4.0-blue" alt="提示词协议">
  <img src="https://img.shields.io/badge/Built_with-Streamlit-red" alt="技术栈">
  <img src="https://img.shields.io/badge/Model-GLM--5-purple" alt="底层模型">
</p>

<p align="center">
  <a href="#-核心功能">核心功能</a> ·
  <a href="#-在线体验">在线体验</a> ·
  <a href="#-本地部署">本地部署</a> ·
  <a href="#-功能详解">功能详解</a> ·
  <a href="#-常见问题">常见问题</a> ·
  <a href="#-交流共建">交流共建</a>
</p>


**为文献排版而生 · 基于大语言模型的智能参考文献排版引擎**| **一键适配国标GB/T 7714与专业期刊体例**


**CanonMaster · 典校大师** 专为人文社科领域学术群体打造，基于智谱GLM-5大语言模型，一键将格式混乱、缺项漏项的参考文献，转换为符合学术标准的规范格式。从论文写作到期刊投稿，一站式解决你的参考文献排版痛点。

### **解决的核心痛点**
学术写作中，你是否遇到过这些问题：
  -参考文献格式混乱、标点错误、缺项漏项，手动校对耗费大量时间
  -不同期刊体例要求不一，反复调整格式占用写作精力
  -传统文献排版工具只能处理简单格式，无法完成语义级的信息补全与上下文继承
  -移动端临时改稿，没有趁手的文献排版工具

### ✨ 核心亮点
-  **学术规范**：严格遵循GB/T 7714-2015国标，内置《文学遗产》等期刊的排版要求
-  **智能处理**：不止正则替换，可智能识别文献要素、补全静态信息、处理同上/同前省略格式
-  **防幻觉设计**：核心动态信息（年份、页码、出版社）不瞎编，缺失项明确标记，拒绝学术不端风险
-  **开箱即用**：在线版打开即用，本地版3步部署完成，零技术门槛也能轻松使用

---
### 效果输出

##  在线体验
无需安装、无需配置，点击下方链接即可一键使用：
> 🔗 [[典校大师 - 在线体验地址](https://ldkacla-canonmaster.hf.space)]
👉 **[线路一：Streamlit 官方云端版](https://canonmaster.streamlit.app/?embed=true)

---

##  本地部署
### 环境要求
- Python >= 3.10
- 有效的ModelScope API Key

### 部署步骤
1.  **克隆仓库**
```bash
git clone https://github.com/a2463712381-ui/CanonMaster.git
cd CanonMaster
---



## ✨ 核心亮点

- 📚 **双轨制通用国标 (GB/T 7714-2015)**：
  - [cite_start]**文末模式**：智能去除专著页码，适配文末参考文献列表 [cite: 106, 251]。
  - [cite_start]**脚注模式**：严格保留引文具体页码，适配正文页底注释 [cite: 106, 251]。
- [cite_start]🏛️ **古籍与经典智能清洗**：自动补全古人朝代（如识别“杜甫”输出为“（唐）杜甫”），精准处理多重责任者（如原著与整理者/校注者），智能降级嵌套书名号 [cite: 331, 332, 336]。
- [cite_start]🎯 **顶刊定向适配**：内置《文学遗产》、《历史研究》等特定学术刊物的专属排版红线规则，一键无缝转换 [cite: 107, 251]。
- [cite_start]⚙️ **最高优先级自定义**：在标准底座之上，支持用户输入个性化指令（如“去除作者朝代”），AI 强制执行 [cite: 53, 108, 228, 252]。

## 🚀 立即在线体验

[cite_start]本项目已实现纯前端响应式部署（完美适配电脑与手机端浏览器），**无需下载安装，即开即用** [cite: 247]。

👉 **[线路一：Streamlit 官方云端版](https://canonmaster.streamlit.app/?embed=true)**
👉 **[线路二：Hugging Face 国内加速版](https://huggingface.co/spaces/你的用户名/你的Space名字)** *(部署完成后替换链接)*

## 🆚 强力对比 (Before & After)

**❌ 糟糕的原始输入：**
> 彭定求编全唐诗中华书局1960
> 鲁迅中国小说的历史的变迁，鲁迅全集第9卷，人民文学出版社1981年版，第325页。

**✅ 典校大师完美输出：**
> (清)彭定求, 等. 全唐诗[M]. 北京: 中华书局, 1960. *(国标模式)*
> 鲁迅《中国小说的历史的变迁》，《鲁迅全集》第9卷，人民文学出版社1981年版，第325页。*(《文学遗产》期刊模式)*

## ❓ 常见问题 (FAQ)

- **Q：AI 会不会胡编乱造出版年份或页码？**
  - [cite_start]**A**：不会。典校大师内置了极强的“幻觉抑制”提示词。对于缺失的动态信息（如页码、年份），它会规范地留空并标记 `[缺: 页码]`，以提示人工核对 [cite: 109, 253]。
- **Q：我的数据安全吗？**
  - [cite_start]**A**：非常安全。工具**不连接任何后端数据库**，所有历史数据仅存在于您当前浏览器的内存中。刷新或关闭页面即刻销毁 [cite: 109, 254]。

## 🤝 交流共建

[cite_start]作为一个由个人开发的开源工具，典校大师仍在不断成长 [cite: 113, 255]。如果您遇到排版 Bug，或者希望适配更多特定期刊的格式，欢迎加入社区：
- [cite_start]🐧 **QQ 交流群**：`1083502445` [cite: 119, 256]
- [cite_start]💻 欢迎在 GitHub 提交 Issue 或 PR。你的每一个 Star 🌟 都是持续迭代的最大动力！ [cite: 132, 256, 257]

## 📜 开源协议与版权声明

本项目采用**双轨制开源协议**：
- **项目代码（UI 与逻辑）**：采用 [MIT License](LICENSE) 协议，欢迎自由复用与交流。
- **核心提示词（`prompts.py`）**：采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议。**严禁任何形式的商业化闭源使用与牟利**，如需引用或二次修改，务必保留署名并以同等协议开源分享。