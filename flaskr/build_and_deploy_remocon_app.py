#################### - リモコンアプリのビルドを行う - ############################
import subprocess
import json
from flaskr.config import REMOCON_CONFIG_PATH, REMOCON_APP_PATH, RESOURCES_PATH
import socket
import shutil
import time

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))

logger.info("----------------------Please wait to build remocon app----------------------")
with open(REMOCON_CONFIG_PATH, "r") as f: # リモコンアプリの設定を読む
    remocon_config = json.load(f)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: # サーバーのIPアドレスを取得する
    s.connect(("8.8.8.8", 80))
    server_ip = s.getsockname()[0]
remocon_config["controlServerHost"] = f"{server_ip}:5000"
logger.info(f"This Server IP address is {server_ip}")
with open(REMOCON_CONFIG_PATH, "w") as f: # リモコンアプリの送信先IPを書き換える
    json.dump(remocon_config,f)
logger.info(f"controlServerHost : {remocon_config['controlServerHost']}")
logger.info("building.... ")
proc = subprocess.Popen("npm run build".split(" "), cwd="Remote-control-app", encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while proc.poll() == None:
    logger.info(f"npm >> {proc.stdout.readline()}",end="")
    time.sleep(0.01)
if proc.returncode != 0:
    logger.info(f"npm >> {proc.stdout.read()}")
    logger.info(f"Return code : {proc.returncode}")
    quit()
logger.info("building OK!")
try:
    shutil.rmtree(f"{RESOURCES_PATH}/build")
except FileNotFoundError:
    pass
shutil.copytree(f"{REMOCON_APP_PATH}/build", f"{RESOURCES_PATH}/build")
logger.info("---------------------------------------------------------------------------------")
###############################################################