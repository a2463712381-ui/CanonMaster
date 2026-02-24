# Copyright (c) 2026 青青翠竹 (GitHub: a2463712381-ui) - MIT License
import streamlit as st
from streamlit_javascript import st_javascript

# ==========================================
# 1. 全局配置
# ==========================================
st.set_page_config(
    page_title="CanonMaster - 典校大师",
    page_icon="📜",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 导入你的两个分身函数
from app import render_desktop
from app_mobile import render_mobile

# ==========================================
# 2. 获取用户浏览器真实宽度
# ==========================================
# 这行代码会让浏览器执行 JS，并把屏幕宽度返回给 Python
window_width = st_javascript("window.innerWidth")

# ==========================================
# 3. 极速智能路由分发
# ==========================================
# 当 window_width 为 0 时（刚打开网页的前 0.5 秒）
if window_width == 0:
    # 仅仅显示一个极简的加载动画，不再显示那些按钮
    st.markdown("""
        <div style='text-align:center; margin-top: 30vh;'>
            <div style='color: #8b0000; font-size: 24px; font-weight: bold; font-family: "Source Han Serif CN", serif;'>
                📜 典校大师
            </div>
            <div style='color: #888; font-size: 14px; margin-top: 10px;'>
                环境加载中...
            </div>
        </div>
    """, unsafe_allow_html=True)

# 宽度小于 768px，自动无缝进入手机版
elif window_width < 768:
    render_mobile()

# 宽度大于等于 768px，自动无缝进入电脑版
else:
    render_desktop()