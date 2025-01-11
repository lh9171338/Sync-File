[<img height="23" src="https://github.com/lh9171338/Outline/blob/master/icon.jpg"/>](https://github.com/lh9171338/Outline) Sync-File
===

这是一个服务器文件同步工具

# 安装

```shell
git clone git@github.com:lh9171338/Sync-File.git

# 安装依赖库
cd Sync-File
python -m pip install -r requirements.txt
```

# SSH配置

```shell
# 生成ssh密钥
ssh-keygen

# 将密钥拷贝至服务器，实现免密码SSH文件拷贝
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
        "src_path": "user@host:src_path",   # 源路径
        "dst_path": "dst_path",  # 备份路径
        "exclude" : ["data", "py38"]   # 无需备份的子文件/子文件夹，一般是不经常修改的大文件/文件夹
    }
]
```
- sync_time：每天同步的时间，格式为HH:MM，例如01:00
