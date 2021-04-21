# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/4/12 15:47
# @Author : 冰海
# @File : config.py
import os
import platform

OS = platform.system()
pyVersion = platform.python_version()

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

zoomeyeApi = ""

fofaApi = {
    "email": "",
    "key": "",
}

quakeApi = ""
shodanApi = ""

# Proxy_api = "http://10.0.0.230:5555/random"
ProxyPool = []
Proxy_api = ""

TimeOut = 5
StatusCode = []

fofaSize = 100
threadNum = 100

ZIPBALL_PAGE = "https://github.com//s7ckTeam/sWebScanner/archive/refs/heads/main.zip"
GIT_REPOSITORY = "https://github.com/s7ckTeam/sWebScanner.git"
Website = "http://www.s7ck.com/"
Team = "s7ck Team   by:冰海&狗一样的男人"
Version = "1.0.1"

Banner = ['''\033[1;31m
 _____     _               
|  ___|   | |__   _____  __
| |_ _____| '_ \ / _ \ \/ /
|  _|_____| |_) | (_) >  < 
|_|       |_.__/ \___/_/\_\\\033[0m    \033[1;34mVersion: {0}\033[0m

\t{1}
\t{2}
'''.format(Version, Team, Website),
          '''\033[1;31m
    _____    _      _____                    
 __|___  |__| | __ |_   _|__  __ _ _ __ ___  
/ __| / / __| |/ /   | |/ _ \/ _` | '_ ` _ \ 
\__ \/ / (__|   <    | |  __/ (_| | | | | | |
|___/_/ \___|_|\_\   |_|\___|\__,_|_| |_| |_|\033[0m    \033[1;34mVersion: {0}\033[0m

\t{1}
\t{2}
 \t{1}
\t{2}
'''.format(Version, Team, Website),
          '''\033[1;31m
   __          __  _     _____                                 
   \ \        / / | |   / ____|                                
  __\ \  /\  / /__| |__| (___   ___ __ _ _ __  _ __   ___ _ __ 
 / __\ \/  \/ / _ \ '_ \\\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 \__ \\\  /\  /  __/ |_) |___) | (_| (_| | | | | | | |  __/ |   
 |___/ \/  \/ \___|_.__/_____/ \___\__,_|_| |_|_| |_|\___|_|   \033[0m    \033[1;34mVersion: {0}\033[0m

 \t{1}
\t{2}
'''.format(Version, Team, Website),
          ]

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]