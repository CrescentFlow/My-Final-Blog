# powershell杩愯娉ㄦ剰浜嬮」

### <1>鍖哄垎璁块棶瀵硅薄鐨勫睘鎬у拰浣跨敤鍙橀噺鐨勫懡浠?

鍦╬owershell 涓悊瑙$__.} 杩欎釜鍗犱綅绗﹁〃绀虹閬撲紶杩囨潵鐨勬瘡涓€涓璞★紝鐒跺悗鐢ㄧ偣鍙锋潵鍙嶅簲浠栫殑灞炴€?

```
Get-Service | Where-Object {$_.Status -eq 'Running'}
Get-Service | Where Status -eq 'Running'鏌ユ壘姝ｅ湪杩愯鐨勬湇鍔?
Get-Service | Where-Object {$_.Name -like "*Update*"}鏌ユ壘鍚嶅瓧閲屽甫鏇存柊鐨勬湇鍔?
Get-Service | Where-Object {$_.Status -eq 'Running'
-and $_.StartType -eq 'Automatic'}鏌ユ壘姝ｅ湪杩愯骞朵笖鍚姩涓鸿嚜鍚姩鐨勬湇鍔?
Get-Service | Select-Object Name, Status 鍙樉绀烘湇鍔＄殑鍚嶅瓧鍜岀姸鎬?
```

### <2>鍩烘湰鍛戒护

``` ```
Get-Content gc, cat 鑾峰彇鏂囦欢鍐呭
Get-ChildItem ls, dir, gci 鍒楀嚭鏂囦欢鐩綍
Get-Service gsv 鑾峰彇鏈嶅姟淇℃伅
Get-Process ps, gps 鑾峰彇杩涚▼淇℃伅
Set-Location cd, chdir 鍒囨崲宸ヤ綔鐩綍
Copy-Item cp, copy 澶嶅埗鏂囦欢鎴栫洰褰?
Remove-Item rm, del, rd 鍒犻櫎鏂囦欢鎴栫洰褰?
```

<3>蹇€熺郴缁熷仴搴疯皟鏌?璁板綍鍚嶅瓧鍜孭ID
