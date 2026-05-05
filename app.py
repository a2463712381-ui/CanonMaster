# Copyright (c) 2026 青青翠竹 (GitHub: a2463712381-ui) - MIT License
import streamlit as st
import os  # 👇 替换掉了原来的 components 库，新增 os 库用来修改底层文件
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

# ==========================================
# 1.5 终极网站访问统计 (底层黑客注入法)
# ==========================================
def inject_51la_into_html():
    try:
        import streamlit
        # 顺藤摸瓜，找到当前服务器上 Streamlit 核心网页的真实路径
        streamlit_dir = os.path.dirname(streamlit.__file__)
        index_path = os.path.join(streamlit_dir, "static", "index.html")
        
        # 如果找到了这个核心网页文件
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 检查是否已经注入过，防止每次刷新重复注入
            if 'id="LA_COLLECT"' not in content:
                # 你的专属 51LA 追踪代码
                la_code = """
    <script charset="UTF-8" id="LA_COLLECT" src="//sdk.51.la/js-sdk-pro.min.js"></script>
    <script>LA.init({id:"3P7vWoetjlCEnk1Q",ck:"3P7vWoetjlCEnk1Q"})</script>
                """
                # 狸猫换太子：把代码直接硬塞进 <head> 标签的最前面
                new_content = content.replace("<head>", f"<head>\n{la_code}")
                
                # 把改写后的内容保存回服务器的硬盘
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
    except Exception as e:
        pass # 遇到任何服务器权限问题都静默跳过

# 程序启动时瞬间执行注入
inject_51la_into_html()

# ==========================================
# 导入你的两个分身函数
# ==========================================
from app_desktop import render_desktop
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