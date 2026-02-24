
import os

# 1. 要导出的文件列表
files_to_export = [
    "main.py",          
    "app.py",           
    "app_mobile.py",    
    "styles.py",        
    "prompts.py"        
]

# 2. 合并后生成的新文件名
output_file = "all_code_for_ai.txt"

# 3. 开始执行合并操作（你刚才漏掉了这一大段👇）
with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in files_to_export:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as infile:
                # 写入明显的分割线，方便 AI 识别这是哪个文件
                outfile.write(f"\n\n{'='*40}\n")
                outfile.write(f"📁 文件名: {filename}\n")
                outfile.write(f"{'='*40}\n\n")
                
                # 写入该文件的全部代码
                outfile.write(infile.read())
        else:
            print(f"⚠️ 警告: 找不到文件 {filename}")
                
print(f"✅ 大功告成！代码已成功合并到 {output_file}")