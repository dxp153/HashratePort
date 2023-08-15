import yaml

# # login-prarmeter.yml
# yaml_file = "../data/login-prarmeter.yml"
# # v = yamlUtil("../data/login.yaml").read_yaml()
# with open("../data/login-prarmeter.yml", 'r', encoding="utf-8") as f:
#     value = yaml.load_all(f.read(), Loader=yaml.FullLoader)
#     v = []
#     for i in value:
#         v.append(i)
#
#
# print(len(v), v, type(v))

for i in range(1, 5):
    print(type(i))
    i += 1