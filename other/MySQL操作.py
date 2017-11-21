import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="test", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()


# 1.查询操作
def select():
    # 编写sql 查询语句  user 对应我的表名
    sql = "select * from student"
    try:
        cur.execute(sql)  # 执行sql语句

        results = cur.fetchall()  # 获取查询的所有记录
        print("id", "name", "age", 'birthday')
        # 遍历结果
        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            birthday = row[3]
            print(id, name, age, birthday)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接


# 1.插入操作
def insert():
    sql_insert = """insert into student(name_d,age) values('liu',22)"""

    try:
        cur.execute(sql_insert)
        # 提交
        db.commit()
    except Exception as e:
        # 错误回滚
        db.rollback()
    finally:
        db.close()


select()
