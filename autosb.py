from utils import handle_args, common_utils
from create import create_java
from add import add_modules
from init import init

if __name__ == '__main__':
    # 初始化命令行参数, 并返回解析后的命令行参数
    args = handle_args.HandleArgs().parser()
    if args.version:
        print("autosb's version: 0.0.1")
        exit(0)
    config = None
    # 判断用户是否有自定义配置文件, 如果有则和默认配置文件合并, 并覆盖默认配置文件参数
    if args.config:
        # 合并初始化配置文件
        config = common_utils.merge_config(args.config)
    else:
        config = common_utils.get_default_springboot_config()

    # 判断operate参数的值, 暂时有如下值['create', 'add']
    # a. create: 创建项目
    # b. add: 增加模块
    if 'create' == args.operate:
        if args.name:
            create_java.Springboot(args.name, config)
        else:
            print("没有添加项目名称!")
            exit(0)
    elif 'add' == args.operate:
        add_modules.AddModules(args.name, config)
    elif 'init' == args.operate:
        init.init_project()
