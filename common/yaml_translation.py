import yaml


class yamlUtil:

    def __init__(self, yaml_file):
        # 通过init把文件传入到这个类
        # :param yaml_file:
        self.yaml_file = yaml_file

    def read_yaml(self):
        # 读取yaml文件
        """
        读取yaml，将yaml反序列化，就是把我们yaml格式转换成dict格式
        :return:
        """
        with open(self.yaml_file, 'r', encoding="utf-8") as f:
            # 文件流，加载方式
            value = yaml.load_all(f.read(), Loader=yaml.FullLoader)
            return value


if __name__ == '__main__':
    v = yamlUtil("../data/approval_initiate.yml").read_yaml()
    print(type(v))
