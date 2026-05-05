---
title: CanonMaster·典校大师
emoji: 📜
colorFrom: green
colorTo: red
sdk: streamlit
sdk_version: "1.32.0"
app_file: app.py
pinned: false
license: mit
---

# 📜 CanonMaster · 典校大师
> **为文献排版而生 · 基于大语言模型的智能参考文献排版引擎**  
> 一键适配国标GB/T 7714-2015与专业期刊官方体例

<p align="center">
  <!-- 徽章组优化：移动端自动换行不混乱，颜色和工具主色完全统一 -->
  <img src="https://img.shields.io/badge/Version-v1.0-8b0000" alt="版本">
  <img src="https://img.shields.io/badge/Code_License-MIT-green" alt="代码协议">
  <img src="https://img.shields.io/badge/Prompt_License-CC_BY--NC--SA_4.0-blue" alt="提示词协议">
  <img src="https://img.shields.io/badge/Built_with-Streamlit-red" alt="技术栈">
  <img src="https://img.shields.io/badge/Model-GLM--5-purple" alt="底层模型">
</p>

<p align="center">
  <!-- 核心CTA按钮放大，主色强化，是整个页面最抓眼的元素 -->
  <a href="https://ldkacla-canonmaster.hf.space" target="_blank">
    <img src="https://img.shields.io/badge/🚀_点击_立即在线体验-8b0000?style=for-the-badge" alt="在线体验">
  </a>
</p>

---

## 📖 项目简介
**CanonMaster · 典校大师** 专为人文社科领域学术群体打造，基于智谱GLM-5大语言模型，一键将格式混乱、标点错误、缺项漏项的参考文献，转换为符合学术标准的规范格式。从学位论文写作到核心期刊投稿，一站式解决你的参考文献排版痛点。

---

## ⚠️ 核心痛点
学术写作中，你是否也曾被这些问题耗尽精力：
- 参考文献格式混乱、标点错误、缺项漏项，手动逐条校对耗费大量时间
- 不同期刊体例要求天差地别，投稿前反复调整格式，占用核心写作精力
- 传统排版工具只能做简单正则替换，无法完成语义级信息补全与「同上/同前」上下文继承
- 移动端临时改稿，没有适配手机、开箱即用的文献排版工具

---

## ✨ 核心亮点
<p align="center">
<table>
  <tr>
    <td width="25%" align="center"><strong>学术级规范</strong></td>
    <td width="75%">严格遵循GB/T 7714-2015国家标准，同时内置《文学遗产》等期刊官方排版体例，文献排版格式一步到位</td>
  </tr>
  <tr>
    <td align="center"><strong>语义级处理</strong></td>
    <td>不止简单正则替换，可智能识别文献核心要素、补全静态事实信息、自动处理「同上/同前」省略格式，复杂场景也能精准处理</td>
  </tr>
  <tr>
    <td align="center"><strong>防幻觉机制</strong></td>
    <td>年份、页码、出版社等核心动态信息绝不编造，缺失项明确标记 <code>[缺:xx]</code>，规避学术不端风险</td>
  </tr>
  <tr>
    <td align="center"><strong>全端自适应</strong></td>
    <td>电脑端/移动端自动无缝适配，浏览器点开即用，无需安装、无需配置，零技术门槛也能轻松上手</td>
  </tr>
</table>
</p>

---

## 🎯 效果演示

<p align="center">
  <img src="https://picui.ogmua.cn/s1/2026/02/25/699ecab79160f.webp" alt="典校大师排版演示" width="100%">
</p>

<p align="center">
  <a href="https://ldkacla-canonmaster.hf.space" target="_blank">
    <img src="https://img.shields.io/badge/📑_立即体验_一键排版-8b0000?style=flat-square" alt="立即体验">
  </a>
</p>

---

## ❓ 常见问题
<details>
<summary><strong>典校大师会胡编乱造文献信息吗？</strong></summary>
不会。典校大师内置了极强的幻觉抑制逻辑，对于年份、页码、出版社等无法100%确认的动态核心信息，会规范标记 <code>[缺:xx]</code> 提示人工核对，绝不编造任何文献信息。所有生成结果建议人工核对后使用。
</details>

<details>
<summary><strong>我的文献数据安全吗？</strong></summary>
非常安全。工具不连接任何后端数据库，所有历史记录、文献数据仅存储于你当前浏览器的本地内存中，刷新页面或关闭标签页后数据即刻销毁，无需担心文献内容泄露。
</details>

<details>
<summary><strong>支持哪些期刊的排版体例？</strong></summary>
目前已完整适配《文学遗产》官方体例，《历史研究》《哲学研究》《中国社会科学》《中国法学》等更多人文社科核心期刊体例正在持续开发中。暂未适配的期刊，可通过「自定义规则」模式实现个性化格式需求。
</details>

<details>
<summary><strong>采用哪一版GB/T 7714国家标准？</strong></summary>
当前默认采用学界通用的<strong>GB/T 7714-2015</strong>版本。作者已关注到GB/T 7714-2025新版国标将于2026年7月1日正式实施，过渡期内优先适配高校主流在用的2015版，后续将同步完成新版国标的完整适配，请放心使用。
</details>

---

## 🤝 交流共建
典校大师是一款由个人开发维护的开源学术工具，你的每一个反馈、建议与贡献，都是项目持续迭代的最大动力。
- 🐧 **用户交流与反馈**：QQ交流群 `1083502445`（最快响应渠道，可提交Bug、功能许愿、学术交流）
- 💻 **开源项目主页**：[a2463712381-ui/CanonMaster](https://github.com/a2463712381-ui/CanonMaster)
  - 欢迎在Issues区提交专业的Bug报告与功能建议
  - 也欢迎提交PR，共同完善新的期刊体例、优化工具功能
- 🌟 你的每一个Star，都是我持续迭代的最大动力！

---

## 📄 开源协议
- 项目代码（UI界面与业务逻辑）：采用 **MIT License开源协议**
- 核心模板（`prompts.py`）：采用 **CC BY-NC-SA 4.0 国际许可协议**（严禁任何形式的商业化闭源牟利）

