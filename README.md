# 📜 CanonMaster · 典校大师

[![License: MIT](https://img.shields.io/badge/Code_License-MIT-blue.svg)](LICENSE)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Prompt_License-CC_BY--NC--SA_4.0-lightgrey.svg)](LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://canonmaster.streamlit.app/?embed=true)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/你的用户名/你的Space名字)

**为人文社科而生 · 基于大语言模型的智能参考文献排版引擎**

---

## 💡 项目简介

在学术写作（特别是古典文献、历史、哲学等文史哲领域）中，格式混乱、标点缺失、缺字漏项的参考文献排版往往耗费学者大量精力。

[cite_start]**CanonMaster · 典校大师** 拒绝机械的正则替换，依托大语言模型（GLM-5 / DeepSeek 等）的深度语义理解能力，一键将非结构化文本转换为符合学术标准的规范格式 [cite: 97, 248, 249]。

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