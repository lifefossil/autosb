import os
from utils import common_utils


class Springboot:
    # 1. 指定创建所在目录
    def __init__(self, project_name, config):
        self.project_name = project_name
        self.config = config
        self.download_template()
        self.init_project()

    # 2. 检查本地是否有模板文件,如果没有下载模板到本地
    # 3. 生成springboot项目结构

    def init_project(self):
        project_path = None
        project_dir = self.config.get('springboot').get('basedir')
        # 如果地址是当前默认命令行路径
        if project_dir == '.':
            basedir = os.path.abspath(os.curdir)
            project_path = os.path.join(basedir, self.project_name)
        else:
            if not common_utils.reg_win_dir_path(project_dir):
                print('自定义配置文件中的 basedir 配置错误, 需要绝对路径')
                exit(0)
            project_path = os.path.join(project_dir, self.project_name)
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        else:
            print('{} 文件夹已经存在!'.format(project_path))
            exit(0)

    def download_template(self):
        pass
        # 1. 检查用户要下载版本
        # 2. 和本地版本对比, 是否已经下载, 如果没有就下载该版本
        # 3. 解压下载到对应的文件夹中
