import pymysql
pymysql.version_info = (1, 3, 13, "final", 0) # 解决mysql版本问题报错而添加的代码
pymysql.install_as_MySQLdb()