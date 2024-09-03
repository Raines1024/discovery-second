# 使用Python 3.9官方基础镜像
FROM python:3.9

# 安装pm4py
RUN pip install pm4py

# 创建工作目录
WORKDIR /app

# 复制当前目录下的所有文件到容器的/app 目录
COPY . /app


