# memory_check.py
import os
import psutil

def print_memory_usage(stage=""):
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / 1024 ** 2
    print(f"[{stage}] Memory usage: {mem_mb:.2f} MB")


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 ** 2
