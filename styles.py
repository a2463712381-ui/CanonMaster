import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* ============================================================ */
        /* 1. 全局基础配置 (强力压缩版) */
        /* ============================================================ */
        .stApp { 
            background-color: #f5f7fa; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            padding-top: 0px !important; 
            padding-bottom: 0px !important; 
        }
                
        /* 核心内容区布局调整 */
        .block-container {
           padding-top: 1.6rem !important;
           padding-bottom: 1.4rem !important;
           max-width: 95% !important;
           /* 适配左侧固定侧边栏的宽度 (240px + 间隙) */
           padding-left: calc(240px + 3rem) !important; 
        }

        /* 强行压缩所有 Streamlit 组件之间的垂直间距 */
        [data-testid="stVerticalBlock"] {
            gap: 0.5rem !important;
        }

        /* 隐藏原生杂项 */
        #MainMenu {visibility: hidden !important;}
        .stDeployButton {display:none !important;}
        header[data-testid="stHeader"] {display: none !important;} 
        footer {display: none !important;}

        /* ============================================================ */
        /* 2. 侧边栏容器 (Sidebar Container) */
        /* ============================================================ */

        /* 彻底隐藏收缩按钮 */
        [data-testid="stSidebarCollapsedControl"] {
            display: none !important;
        }

        /* 强制侧边栏固定位置、固定宽度 */
        section[data-testid="stSidebar"] {
            width: 240px !important;
            min-width: 240px !important;
            max-width: 240px !important;
            transform: translateX(0px) !important;
            visibility: visible !important;
            position: fixed !important;
            left: 0 !important;
            top: 0 !important;
            height: 100vh !important;
            z-index: 99999 !important;
            background-color: #f8f9fa !important;
        }

        /* ============================================================ */
        /* 3. 侧边栏内容区 (Sidebar Content) */
        /* ============================================================ */

        [data-testid="stSidebarUserContent"] {
            padding-top: 3rem !important;
            padding-left: 1.5rem !important;
            padding-right: 1.5rem !important;
            
            /* 保持可滚动能力，但隐藏滚动条 UI */
            overflow-y: auto !important;
            scrollbar-width: none !important; /* Firefox */
            -ms-overflow-style: none !important; /* IE/Edge */
        }
        
        /* Chrome/Safari 隐藏滚动条 */
        [data-testid="stSidebarUserContent"]::-webkit-scrollbar {
            display: none !important;
            width: 0 !important;
            height: 0 !important;
        }

        /* ============================================================ */
        /* 4. 侧边栏组件专属样式 (导航菜单垂直排列) - 【核心修复区】 */
        /* ============================================================ */
        
        /* 强制侧边栏内的 Radio 垂直排列 + 统一左对齐 */
        section[data-testid="stSidebar"] div[data-testid="stRadio"] > div[role="radiogroup"] {
            flex-direction: column !important;
            gap: 0.625rem !important; /* 统一用rem单位，对应10px */
            align-items: flex-start !important; /* 关键：所有选项左对齐 */
            width: 100% !important; /* 填满侧边栏宽度 */
        }
        
        /* 侧边栏Radio选项 - 统一内边距和对齐 */
        section[data-testid="stSidebar"] div[data-testid="stRadio"] label {
            display: flex !important;
            align-items: center !important; /* 图标和文字垂直居中 */
            padding: 0.5rem 0 !important; /* 统一上下内边距 */
            width: 100% !important; /* 每个选项占满宽度 */
            margin: 0 !important; /* 清除默认外边距 */
        }
        
        /* 侧边栏Radio的单选按钮 - 固定位置，避免错位 */
        section[data-testid="stSidebar"] div[data-testid="stRadio"] input[type="radio"] {
            margin-right: 0.75rem !important; /* 按钮和文字之间固定间距 */
            flex-shrink: 0 !important; /* 防止按钮被压缩 */
        }
        
        /* 侧边栏文字颜色 + 统一样式 */
        section[data-testid="stSidebar"] p {
            color: #2c3e50 !important;
            font-size: 15px !important;
            font-weight: 500 !important;
            margin: 0 !important; /* 清除p标签默认外边距（关键修复） */
            line-height: 1.2 !important; /* 统一行高 */
        }
        
        /* 隐藏侧边栏 Radio 的 Label */
        section[data-testid="stSidebar"] div[data-testid="stRadio"] > label {
            display: none !important;
        }

        /* ============================================================ */
        /* 5. 主工作台 (Main Area) UI 组件美化 */
        /* ============================================================ */

        /* 标题区域 */
        .custom-title {
            text-align: center; 
            display: flex; align-items: center; justify-content: center; 
            gap: 15px; margin-bottom: 10px !important; 
        }
        .custom-title h2 { 
            color: #1f2d3d; letter-spacing: 2px; margin: 0 !important;
            font-size: 24px !important; display: inline-block !important;
        }
        .custom-title img {
            width: 40px !important; height: 40px !important; display: inline-block !important;
        }

        /* 按钮美化 */
        div.stButton > button {
            background: linear-gradient(135deg, #07c160 0%, #05a350 100%);
            color: white; border: none; border-radius: 50px;
            padding: 10px 24px; font-weight: 600;
            box-shadow: 0 4px 6px rgba(7, 193, 96, 0.2);
            transition: all 0.2s ease;
        }
        div.stButton > button:hover { transform: scale(1.02); box-shadow: 0 6px 8px rgba(7, 193, 96, 0.3); }

        /* 输入框美化 */
        .stTextArea textarea {
            border-radius: 12px; border: 1px solid #ddd; padding: 15px; background-color: #fff;
        }
        .stTextArea textarea:focus { border-color: #07c160; box-shadow: 0 0 0 1px #07c160; }
        
        /* 下拉框 - 修复间距问题 */
        div[data-baseweb="select"] { 
            /* 1. 关键：把 auto 改为 0，强制左对齐，紧贴左侧标签 */
            margin-left: 0 !important; 
            margin-right: auto !important; 
            margin-top: 0 !important;
            margin-bottom: 5px !important;
            
            /* 2. 宽度调整：设为 100% 以填满列宽（像输入框一样），或者设为 auto */
            width: 100% !important; 
            min-width: 160px !important; /* 保证最小宽度 */
        }
        
        div[data-baseweb="select"] > div { 
            /* 内部文字左对齐 */
            text-align: left !important; 
            border-radius: 8px !important; 
        }

        /* ============================================================ */
        /* 6. 悬浮提示词 & 横排 Radio (🌟 恢复原有字体与间距) */
        /* ============================================================ */
        
        /* 左侧对齐标签 (Label) */
        .radio-label {
            color: #2c3e50 !important;
            font-size: 18px !important;
            font-weight: 600 !important;
            display: flex !important;
            align-items: center !important; 
            justify-content: flex-end !important;
            text-align: right !important;
            height: 100% !important;
            padding-right: 15px !important;
            white-space: nowrap !important;
        }

        /* --- [核心] 主区域 Radio 横排逻辑 --- */
        
        /* 1. 隐藏原生 Label */
        section[data-testid="stMain"] div[data-testid="stRadio"] > label { display: none !important; }
        
        /* 2. 容器横排 */
        section[data-testid="stMain"] div[data-testid="stRadio"] {
            display: flex !important;
            flex-direction: row !important;
            justify-content: center !important;
            width: 100% !important;
        }
        
        /* 3. 选项组横排 - [🌟 恢复间距] */
        section[data-testid="stMain"] div[data-testid="stRadio"] > div[role="radiogroup"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            /* 原来可能是 25px 或更大，这里我改回 25px */
            gap: 4px !important; 
            align-items: center !important;
            justify-content: center !important;
        }

        /* 4. 文字样式 - [🌟 恢复字体层次感] */
        section[data-testid="stMain"] div[data-testid="stRadio"] label p {
            font-size: 16px !important;
            /* 恢复默认粗细 (500看起来比较有质感)，颜色交给 Streamlit 自动处理选中态 */
            font-weight: 500 !important; 
            color: #2c3e50 !important; /* 默认深灰 */
            margin: 0 !important;
            white-space: nowrap !important;
        }
        
        /* 🌟 [新增] 选中状态下的文字样式增强 */
        /* 当选中时，文字颜色变黑，加粗 */
        section[data-testid="stMain"] div[data-testid="stRadio"] input[type="radio"]:checked + label p {
            color: #000 !important; /* 选中变纯黑 */
            font-weight: 600 !important; /* 选中加粗 */
        }

        /* 5. 选中变绿 (前面的圈圈) */
        section[data-testid="stMain"] div[data-testid="stRadio"] input[type="radio"]:checked + label::before {
            background-color: #07c160 !important; border-color: #07c160 !important;
        }
        
        /* 定位准备 */
        section[data-testid="stMain"] div[data-testid="stRadio"] label {
            position: relative !important;
        }

        /* ============================================================ */
        /* 7. Tooltip 动画与内容 */
        /* ============================================================ */
        
        @keyframes fadeInTooltip {
            from { opacity: 0; transform: translate(-50%, 5px); }
            to { opacity: 1; transform: translate(-50%, 0); }
        }

        /* Tooltip 基础样式 */
        .block-container div[data-testid="stRadio"] label::after,
        .block-container div[data-testid="stRadio"] label::before {
            position: absolute; left: 50%; transform: translateX(-50%);
            opacity: 0; pointer-events: none; animation: fadeInTooltip 0.3s forwards; display: none;
        }
        .block-container div[data-testid="stRadio"] label::before {
            content: ""; border-width: 6px; border-style: solid; border-color: transparent transparent #333 transparent;
        }
        .block-container div[data-testid="stRadio"] label::after {
            background-color: #333; color: #fff; border-radius: 6px; font-size: 12px;
            white-space: nowrap; z-index: 99999; box-shadow: 0 4px 6px rgba(0,0,0,0.15); font-weight: normal;
        }
        .block-container div[data-testid="stRadio"] label:hover::after,
        .block-container div[data-testid="stRadio"] label:hover::before { display: block; }

        /* Tooltip 内容 */
        .block-container div[role="radiogroup"]:has(label:nth-of-type(3)) label::before { top: 110%; }
        .block-container div[role="radiogroup"]:has(label:nth-of-type(3)) label::after { top: 140%; padding: 6px 12px; }
        .block-container div[role="radiogroup"]:has(label:nth-of-type(3)) label:nth-of-type(1):hover::after { content: "适用于学术论文的 GB/T 7714-2015 参考文献国家标准格式"; }
        .block-container div[role="radiogroup"]:has(label:nth-of-type(3)) label:nth-of-type(2):hover::after { content: "适配学术期刊专属排版体例（如《文学遗产》《历史研究》等）"; }
        .block-container div[role="radiogroup"]:has(label:nth-of-type(3)) label:nth-of-type(3):hover::after { content: "按个性化要求定制排版"; }

        .block-container div[role="radiogroup"]:not(:has(label:nth-of-type(3))) label::before { top: 120%; }
        .block-container div[role="radiogroup"]:not(:has(label:nth-of-type(3))) label::after { top: 150%; padding: 5px 10px; border-radius: 4px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); animation: fadeInTooltip 0.2s forwards; }
        .block-container div[role="radiogroup"]:not(:has(label:nth-of-type(3))) label:nth-of-type(1):hover::after { content: "用于论文参考文献列表，去除页码"; }
        .block-container div[role="radiogroup"]:not(:has(label:nth-of-type(3))) label:nth-of-type(2):hover::after { content: "用于论文脚注，保留引文具体页码"; }

        </style>
    """, unsafe_allow_html=True)
        