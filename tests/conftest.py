import sys
import os

# 把 src 目录加入 import 路径
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

sys.path.insert(0, SRC_DIR)
