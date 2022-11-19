## 仓库基本情况

### 基本功能

```
scrapy 可视化分布式爬虫
```



### 环境搭建

```
python = 3.10
```

### 环境安装

```
pip install -r requirements.txt
或
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```



### scrapyd 启动

```
进入项目根目录下输入
scrapyd
注：启动scrapyd服务
```



### 部署爬虫项目到服务器

```
scrapyd-deploy deploy别名 -p 项目名称
注：deploy别名就是在scrapy 项目中的scrapy.cfg [deploy:] 设置的名称
```



### 执行爬虫任务

```
curl http://localhost:6800/schedule.json -d project=se_project -d spider=mfw
```

注：此目的在于测试scrapyd 是否安装完成



### spideradmin 

```
$ pip3 install -U spideradmin

$ spideradmin init  # 初始化，可选配置，也可以使用默认配置

$ spideradmin       # 启动服务
```

注：项目运行起来的前提是要先运行scrapyd、spideradmin



### redis分布式

```
host:****
db:*
port:6379
password:****
```



### mongo 存储

```
host:location
port:32771
user:test
password:****

```











### 版本

```
version v1
date 2022-11-04
```

