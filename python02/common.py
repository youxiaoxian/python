import yaml


def get_param():
    with open("conf/param.yml") as f:
        param = yaml.safe_load(f)
    return param
