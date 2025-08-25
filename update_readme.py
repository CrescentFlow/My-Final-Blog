import subprocess
import re

def get_git_log():
    result = subprocess.run([
         'git',
         'log',
         '--oneline',
         '--since="2025-08-20",'
         '--pretty=format :"- %s(%ad)"',
         '--date=short',
         '-n',
         '5'],capture_output=True,text=True)
                             
    return result.stdout

with open('README.md','r')as f :
     content = f.read()

new_log = get_git_log()
pattern = r'<!--START_SECTION:latest_update-->.*<!--END_SECTION:latest_update-->'
repalcement = f'<!--START_SECTION:latest_update-->\n{new_log}\n<!--END_SECTION:latest_update-->'
new_content = re.sub(pattern,replacement,content,flags=re.DOTALL)


with open('README.md','w')as f:
      f.write(new_content)