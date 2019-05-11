# nginx_docker
请在需要的server块下添加include语句,假设项目目录在/home/user/nginx_docker
```
include /home/user/nginx_docker/*.conf;
```

当有容器进行更新时，需要执行一次`build_config.py`文件，之后reload nginx服务
（执行的用户需要有docker的权限）
