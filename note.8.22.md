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

<3>快速系统健康调查-记录名字和PID
