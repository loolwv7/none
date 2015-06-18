VRM     直流电-直流电稳压器出现故障或丢失。CNFG发生配置错误
NMI  硬件错误已报告给操作系统。注：PCI 或MEM 指示灯也可能会点亮。
SP         Remote Supervisor Adapter II 发生故障或缺少，或者未连接扁平电缆。
DASD    硬盘驱动器发生故障或已卸下
RAID    RAID 控制器指出发生了故障
FAN   风扇发生故障或已卸下
BRD  微处理器板或I/O 板发生故障

CNFG  发生配置错误
NMI      硬件错误已报告给操作系统。

VRM   一般是CPU电源模块故障。CPU报错灯也会亮。
NMI   一般是内存错误。指不可屏蔽错误。内存附近会有灯亮。也可能是PCI故障。但是如果是PCI卡故障，PCI槽附近灯会亮。
DASD  一般是硬盘问题。硬盘上报错灯会亮。冷启动的话，阵列卡会提示。
FAN   当然是风扇故障了。对应的风扇灯会亮。
PS1/PS2 一路电源有问题。通常是只插了一路电。如果都插了，开机情况下，电源后面AC、DC应该都亮，否则电源坏。

90%以上是以上故障。
其他的指示灯绝少碰到。除非你中奖了~


来回答几个吧，但不是很全面， 知道的都说出来，说是最主要的几个：
ps1 电源1
ps2 冗余电源2
cpu cpu
vrm cpu稳压模块
mem 内存
raid raid阵列卡
fan 服务器风扇
brd pci 主板pci插槽上的设备

那个亮红灯，就表示哪个设备有故障

DS3500 reset password
http://www.filibeto.org/unix/aix/lib/hardware/ds4800/faq/QOW-LD%20Forgotten%20Password.htm
http://www.bvanleeuwen.nl/faq/?p=8
http://tecniq.info/index.php/DS_Subsystem_CLI_access_and_commands

For the serial connection, choose the correct port and the following settings:

    57600 Baud
    8 Data Bits
    1 Stop Bit
    No Parity
    Xon/Xoff Flow Control 

Send a break signal to the controller. This varies depending on the terminal emulation. For most terminal emulations, such as HyperTerm, which is included in Microsoft Windows products, press Ctrl+Break. If you only receive unreadable characters, press Ctrl+Break again, until the following message appears:

Press <SPACE> for baud rate within 5 seconds.

Press the Space bar to ensure the correct baud rate setting. If the baud rate was set, a confirmation appears. Press Ctrl+Break to log on to the controller. The following message appears:

Press within 5 seconds: <ESC> for SHELL, <BREAK> for baud rate.

Press the Esc key to access the controller shell. The password you are prompted for is infiniti. Note that this appears to have changed for the DS4700 and DS4800 systems and the serial connections are not longer directly supported.
Password Reset

To reset the storage manager password you need to log into each DS controller via the serial CLI and use the following command (case sensitive):  

    clearSYMbolPassword 
