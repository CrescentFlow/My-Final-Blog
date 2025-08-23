### 基本命令复习

```
#重命名文件夹
mv old-name new-name
#创建文件夹
New-Item -Name "file-name" -ItemType "File"
#初始化git仓库
git init && git add . && git commit 
#实时记录
gc -Wait
#回溯
git restore\checkout .
#回溯记录
git log
#重命名分支
git branch -M main
#查看分支名称
git branch
#检查当前的远程地址
git remote -v
#删除现有远程地址
git remote remove origin
#重新添加远程地址
git remote add origin git@github.com

 ```

 ## shell配置

 ```
 #执行关联命令
 git remote add origin https://github.com/username/repository-name.git
 #尝试推送
 git push -u origin main 
 ######SSH注意事项######
 #生成SSH密钥
 ssh-keygen -t name -C "email@example.com"
 #将公钥添加到Github显示公钥内容
 cat ~/.ssh/file-name  -> settings
 #之后测试连接 and push 
 ssh -T git@github.com 
 git push -u origin main

```
### 注意事项
```
 ##中文路径循环限制###
 C：\Users\china-name\.ssh\contents {  known_hosts 已知主机记录 known_hosts.old 旧的已知主机记录  config SSH 配置文件 }
 #Permission denied 
 #启动SSH代理-添加密钥到代理-测试连接
 Get-Service ssh-agent | Set-Service -StartupType Manual -PassThru | Start-Service
 ssh-add ~/.ssh/keysname
 ssh -T git@github.com

 ##Access is denied##
 #以管理员身份运行
 Get-Service ssh-agent |Set-Service -StartupType Manual -PassThru | Start-Service
  

 ##could not create directory## {中文路径循环限制}
 #绝对路径指定系统寻找known_hosts文件 ->push   ssh内部的库无法正确解析包含中文的路径
 ssh -o UserKnownHostsFile="C: \Users\china-name\.ssh\known_hosts"
 #$HOME变量（确保.ssh存在并且明确指定Known_hosts 文件的正确路径）
 New-Item -ItemType Dicrectory -Path "$HOME\.ssh" -Force
 ssh -o UserKnownHostsFile="$HOME\.ssh\Known_hosts" -T git@github.com


##让所有连接包括gitpush都使用正确的Known_hosts文件

 
 ```