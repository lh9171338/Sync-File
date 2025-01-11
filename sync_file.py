# -*- encoding: utf-8 -*-
"""
@File    :   sync_file.py
@Time    :   2024/03/12 15:32:24
@Author  :   lihao57
@Version :   1.0
@Contact :   lihao57@baidu.com
"""

import os
import json
import time
import shutil
import logging
import argparse
import schedule


def sync_file(config_file: str):
    """
    synchronize files

    Args:
        config_file (str): config file

    Return:
        None
    """
    try:
        with open(config_file, "r") as f:
            configs = json.load(f)

        logging.info("configs:")
        logging.info(configs)
        assert len(configs), "configs is empty"
        for item in configs:
            if not item.get("sync", False):
                continue
            src_path = item["src_path"]
            dst_path = item["dst_path"]
            excludes = item.get("exclude", [])
            os.makedirs(dst_path, exist_ok=True)

            dst_folder = os.path.join(dst_path, os.path.basename(src_path))
            backup_folder = dst_folder + ".bak"

            cmd = f"rsync -av --backup --backup-dir {backup_folder} -e ssh "
            for exclude in excludes:
                cmd += "--exclude={} ".format(exclude)
            cmd += "{} {}".format(src_path, dst_path)
            logging.info("cmd: {}".format(cmd))
            error_code = os.system(cmd)
            logging.info("error_code: {}".format(error_code))

    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    # set base logging config
    fmt = "[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s] %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO)

    # args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config_file",
        type=str,
        help="config file",
        default="config.json",
    )
    parser.add_argument(
        "-t",
        "--sync_time",
        type=str,
        help="sync time",
        default="01:00",
    )
    parser.add_argument(
        "-n",
        "--now",
        action="store_true",
        help="run now",
    )
    opt = parser.parse_args()
    print(opt)

    t1 = time.time()

    config_file = opt.config_file
    sync_time = opt.sync_time
    now = opt.now
    if now:
        sync_file(config_file)
    else:
        schedule.every().day.at(sync_time).do(sync_file, config_file)
        try:
            while True:
                schedule.run_pending()
        except KeyboardInterrupt:
            pass

    t2 = time.time()
    logging.info("time: {}".format(t2 - t1))
