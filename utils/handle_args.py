import argparse


class HandleArgs:
    def __init__(self):
        self.parsers = argparse.ArgumentParser(description="springboot 项目生成脚本, 用于自动生成springboot项目结构和功能模块")
        self.setArgs()

    def setArgs(self):
        self.parsers.add_argument("operate", help="项目操作符[create, add, init]", nargs="?")
        self.parsers.add_argument("name", help="项目或者模块名称", nargs="?")
        self.parsers.add_argument("-c", "--config", help="添加自定义配置文件")
        self.parsers.add_argument("-v", "--version", help="程序版本", action="store_true")

    def parser(self):
        return self.parsers.parse_args()