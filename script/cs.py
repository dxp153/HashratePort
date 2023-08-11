import pytest
import yaml
import os


with open('../data/login-prarmeter.yml', 'r', encoding='utf-8') as f:
    result = yaml.load(f.read(), Loader=yaml.FullLoader)

print(result[0]['input']['data'])