::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: 该BAT脚本主要目的是为了实现定时拨号并自动访问指定的网站在特定的时间范围内所更新的网页。
:: Created By Merlyn
:: # License:      GPL
:: # License file  LICENSE.txt
:: # Email:        merlyncaulfield@gmail.com
:: #
:: # -----------------------------------------------------------------------------
:: # This program is free software; you can redistribute it and/or
:: # modify it under the terms of the GNU General Public License
:: # as published by the Free Software Foundation; either version
:: # 2 of the License, or (at your option) any later version.
::
::
:: # This program is distributed in the hope that it will be useful, but WITHOUT
:: # ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
:: # FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
:: # more details.
::
:: # You should have received a copy of the GNU General Public License along with
:: # this program; if not, write to the Free Software Foundation Inc., 59 Temple
:: # Place - Suite 330, Boston, MA 02111-1307, USA.
:: # -----------------------------------------------------------------------------
::
:: Last updated 04/18/2013
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

@echo off
set /P today="请输入时间(格式为 201304/04 或 201304/03|201304/04 ): " || echo 日期不能为空!!! && pause && exit 
set /p time1="请输入拨号连接间隔时间: " 
set SITE=www.zjpy.gov.cn

::执行Hide_BAT_CMD.vbs
set BROWSER=Hide_BAT_CMD.vbs
@RMDIR /S /Q %SITE% 2>nul

:begin
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: 先中断“拨号连接”并重新连接。
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::拨号链接间隔时间
ping -n %time1% 127.0.0.1 >nul
RASDIAL PPPOE /disconnect && echo 拨号连接已断开! || echo 断开失败
ping -n 2 127.0.0.1 >nul
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: 修改成创建时所填写的PPPOE连接名称
:: username password替换为自己的PPP拨号用户名和密码。
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
RASDIAL PPPOE username password

echo LET'S GO!  
echo "同步新增网页并把结果重定向到urls.txt，请稍等..."

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: 模拟访问特定时间范围内所更新的网页链接
:: 其实现方式为用wget工具先把指定的网站页面下载回来，但之后每次只下载更新的部分网页。
:: 然后找出某段时间内更新的网页，用sed命令转换成url导入在urls.txt中，用浏览器（chrome,firefox）
:: 访问该urls.txt中的网页连接，从而达到了访问和刷新的目的。
:: 与此同时脚本会把访问的结果重定向到autodial_log.txt文件中（包括访问时间记录、自己的IP地址、访问成功和失败的结果）
:: @DIR /B /W /S %SITE% | findstr "201304.04.*html"
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 

@TASKLIST | @FINDSTR "chrome.exe" 1>nul 2>nul & start %BROWSER% & wget -o wget.log --accept="html" --user-agent="Mozilla/5.0 (IPad; u; CPU OS 3_2_1 like Mac OS X; en-us) applewebkit/531.21.10 (khtml, like gecko) mobile/7b405" --continue --recursive --no-parent --no-clobber http://%SITE%/ 2>nul & @DIR /B /W /S %SITE% | gfind %SITE% -type f -name "*.html" | sed -e "s/www/http:\/\/www/;s/\\/\//g" | grep -E "%today%" > urls.txt & @TYPE urls.txt | gawk -F"20" "{ print $1 }"  | sed "s/.$/index.html/" | uniq -i >> urls.txt & unix2dos urls.txt 1>nul & echo http://%SITE% >> urls.txt &  echo 指定的日期所产生的网页链接已找到并导入urls.txt文件中! & echo 打开链接中... & multiurls.bat urls.txt 1>nul & ping -n 3 127.0.0.1 >nul && multiurls.bat urls.txt 1>nul & ping -n 2 127.0.0.1 >nul & @TASKKILL /F /IM "chrome.exe" 1>nul & wget -q -O - icanhazip.com 1>> autodial_log.txt 2>nul && echo %DATE% %TIME% Successful. >> autodial_log.txt || echo %DATE% %TIME% Failed! >> autodial_log.txt

goto begin
pause >nul
