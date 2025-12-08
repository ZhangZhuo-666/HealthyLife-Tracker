import sys
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# src 文件夹路径
SRC_DIR = os.path.join(ROOT_DIR, "src")

# 把项目根目录和 src 目录都加进 import 路径中
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, SRC_DIR)
