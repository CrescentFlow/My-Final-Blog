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
cd D:/ 切换目录
ls 查看当前目录的文件夹
mkdir创建文件夹

```



### <3>快速系统健康调查-记录名字和PID
