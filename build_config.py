import os
from get_container_info import get_container_info

conf_string = """location ^~/api{0} {{
    proxy_pass http://{1}:80/;
    include {2}/proxy.conf.include;
}}
"""


def build_conf_file(name: str, ip: str, path: str):
    file_string = conf_string.format(name, ip, path)
    with open("docker_{0}.conf".format(name[1:]), "w") as f:
        f.writelines(file_string)


if __name__ == '__main__':
    abspath = os.path.abspath(".")
    os.popen(r"rm *.conf")
    for container_name, container_ip in get_container_info():
        build_conf_file(container_name, container_ip, abspath)
