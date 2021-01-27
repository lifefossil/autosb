import os
import sys
import re
from yaml import load, Loader

'''
    resource_path() 是用来确定资源文件具体位置,
    如果用pyinstaller打包成可执行应用程序, 默认情况下资源文件是没有打包进去,
    只有在.spec 中的datas配置选项添加需要一起打包资源文件后, 才能范文, 此函数就是来确定打包后
    运行程序时资源文件的真实地址在哪里.
'''


def merge_config(config):
    """
    合并用户自定义的配置文件, 并覆盖默认配置选项
    :param config: 用户自定义文件路径
    :return 返回合并后的字典配置文件
    """
    # 1. 判断文件是否存在
    config_path = os.path.join(os.getcwd(), config)
    if not os.path.isfile(config_path):
        print("配置文件不存在, 请检查后再试!")
        exit(0)

    # 2. 获得用户自定义文件内容
    r_config_dict = ymlToDict(config_path)

    # 3. 与默认配置文件合并, 其中用户定义的配置覆盖默认配置
    d_file = resource_path(os.path.join("resources", "ini.yml"))
    d_config_dict = ymlToDict(d_file)
    z = dict(r_config_dict, **d_config_dict)
    for key in z.keys():
        if key in r_config_dict:
            z[key] = dict(z[key], **r_config_dict[key])
    return z


def resource_path(relative_path):
    """
    生成资源文件目录访问路径
    :param relative_path: 拼接后面的文件地址
    :return: 资源文件真实地理位置
    """
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_default_springboot_config():
    """
    获得默认配置
    :return:
    """
    filename = resource_path(os.path.join("resources", "ini.yml"))
    return ymlToDict(filename)


def ymlToDict(path):
    with open(path, 'r', encoding='utf-8') as f:
        yml = f.read()
        return load(yml, Loader=Loader)


def reg_win_dir_path(path):
    reg = r'^[a-zA-Z]:(\\[^\//<>|:*?"]+)+$'
    return re.match(reg, path)


def get_app_download_path():
    u_h_path = os.path.expanduser('~')
    return os.path.join(u_h_path, 'AppData', 'Local', '.autosb')


def did_download_template():
    a_d_path = get_app_download_path()


if __name__ == '__main__':
    # match_r = reg_win_dir_path(r"d:\dir\name\project")
    # if match_r:
    #     print(match_r.group())
    print(get_app_download_path())
