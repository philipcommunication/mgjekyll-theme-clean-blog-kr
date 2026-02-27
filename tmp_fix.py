import os

path = r'c:\Users\NDK\Desktop\jekyll-theme-loadingblog-kr-master\admin\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace spaces added by some tool
content = content.replace('{ {', '{{')
content = content.replace('} }', '}}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
