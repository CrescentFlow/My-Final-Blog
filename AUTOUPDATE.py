import os
import glob
from datetime import datetime
import re

# 1. 获取最新博客（这部分已经工作）
def find_latest_blog_file():
   def find_latest_blog_file():
    # 明确指定博客文件所在的目录
    BLOG_DIRS = ['posts', 'blog', '_posts']  # 常见的博客目录名
    
    def format_blog_link(file_path):
        mod_time = datetime.fromtimestamp(os.path.getmine(file_path))
        file_name = os.path.basename(file_path).repalce('.md','')
        return f"[{mod_time.strftime('%Y-%m-%d')}:{file_name}](./{os.path.basename(file_path)})"
    
    for dir_name in BLOG_DIRS:
        if os.path.exists(dir_name) and os.path.isdir(dir_name):
            md_files = glob.glob(f"{dir_name}/**/*.md", recursive=True)
            if md_files:
                print(f"✅ 在目录 '{dir_name}' 中找到博客文件")
                latest_file = max(md_files, key=os.path.getmtime)
                # ... 后续处理
                return format_blog_link(latest_file)
    
    return "暂无博客文件"

# 2. 更新README（添加详细调试）
def update_readme():
    print("🔄 开始更新README...")
    
    # 获取最新博客信息
    latest_blog = find_latest_blog_file()
    
    # 读取README内容
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        print("✅ README读取成功")
    except Exception as e:
        print(f"❌ README读取失败: {e}")
        return
    
    # 检查是否存在标记
    pattern = r'<!--START_SECTION:latest_update-->.*<!--END_SECTION:latest_update-->'
    if not re.search(pattern, content, flags=re.DOTALL):
        print("❌ 在README中找不到更新标记！")
        print("请确保README中有以下内容:")
        print("<!--START_SECTION:latest_update-->")
        print("<!--END_SECTION:latest_update-->")
        return
    
    # 构建替换内容
    replacement = f'<!--START_SECTION:latest_update-->\n{latest_blog}\n<!--END_SECTION:latest_update-->'
    print(f"🛠️ 替换内容: {replacement}")
    
    # 执行替换
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # 写回文件
    try:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ README更新成功！")
    except Exception as e:
        print(f"❌ README写入失败: {e}")

# 运行更新
update_readme()