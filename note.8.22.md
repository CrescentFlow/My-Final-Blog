# powershell运行注意事项

### <1>区分访问对象的属性和使用变量的命令

在powershell 中理解{$__.} 这个占位符表示管道传过来的每一个对象，然后用点号来反应他的属性

```
Get-Service | Where-Object {$_.Status -eq 'Running'}
Get-Service | Where Status -eq 'Running'查找正在运行的服务
Get-Service | Where-Object {$_.Name -like "*Update*"}查找名字里带更新的服务
Get-Service | Where-Object {$_.Status -eq 'Running'
-and $_.StartType -eq 'Automatic'}查找正在运行并且启动为自启动的服务
Get-Service | Select-Object Name, Status 只显示服务的名字和状态
cd D:\ls -Recurse | Where-Object { $_.Name -eq "8.18.md" }找到你的文件到底在哪

```

### <2>基本命令

``` ```
Get-Content gc, cat 获取文件内容
Get-ChildItem ls, dir, gci 列出文件目录
Get-Service gsv 获取服务信息
Get-Process ps, gps 获取进程信息
Set-Location cd, chdir 切换工作目录
Copy-Item cp, copy 复制文件或目录
Remove-Item rm, del, rd 删除文件或目录
```

``` ```
# 一键还原到最后一次提交的状态
git restore .
# 或者用这个更强大的命令，强制还原所有文件
git checkout -- .
# 1. 查看当前文件发生了什么变化（哪些被修改了、删除了）
git status

# 2. 再次添加所有变更（如果文件被删，这步也能记录删除操作）
git add .

# 3. 再次提交备份，并留下记录
git commit -m "备份：又写了一段关于XXX的内容"
# 添加远程仓库地址（把你仓库的HTTPS地址换到这里）
git remote add origin https://github.com/你的用户名/你的仓库名.git

# 将本地备份推送到远程（需要你登录账号）
git push -u origin main
# 查看 8.19.md 这个文件的历史修改记录
git log -p 8.19.md

```



### <3>快速系统健康调查-记录名字和PID

``` 

```
