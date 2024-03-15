[<img height="23" src="https://github.com/lh9171338/Outline/blob/master/icon.jpg"/>](https://github.com/lh9171338/Outline) Sync-File Package
===

这是一个开发机文件同步工具

# 安装

```shell
git clone ssh://lihao57@icode.baidu.com:8235/baidu/personal-code/Sync-File

# 安装依赖库
cd Sync-File
python -m pip install -r requirements.txt
```

# SSH配置

```shell
# 生成ssh密钥
ssh-keygen

# 将密钥拷贝至开发机，实现免密码SSH文件拷贝
ssh-copy-id user@host
```

# 运行

```shell
python sync_file.py [--config_file <CONFIG_FILE> --sync_time <SYNC_TIME>]

# 示例，每天一点进行一次代码同步
python sync_file.py --config_file config.json --sync_time 01:00

# 后台运行
nohup python sync_file.py --config_file config.json --sync_time 01:00 &
```

# 参数说明

- config_file：json格式配置文件，示例如下，更新信息请参考[config.json](config.json)
```json
[
    {
        "sync": false,  # 是否同步，true表示同步，false表示不同步
        "src_path": "vis@yq02-inf-sci-k8s-a800-hbxgn6-0180.yq02.baidu.com:/ssd2/lihao57/AD2.0/PaddleLSD",   # 开发机文件路径
        "dst_path": "/work/AD2.0",  # 个人虚拟机备份路径
        "exclude" : ["data", "py38"]   # 无需备份的子文件/子文件夹，一般是不经常修改的大文件/文件夹
    }
]
```
- sync_time：每天同步的时间，格式为HH:MM，例如01:00
