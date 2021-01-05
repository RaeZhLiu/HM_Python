import pymysql

if __name__ == '__main__':
    # 创建连接对象
    conn = pymysql.connect(host="localhost",
                    port=3306,
                    user="root",
                    password="root",
                    database="jing_dong",
                    charset="utf-8")

    # 获取游标对象
    cursor = conn.cursor()

    # 查询SQL语句
    sql = "select * from goods;"

    # 执行SQL语句，返回值为SQL语句在执行过程中的行数
    row_count = cursor.execute(sql)
    print("SQL语句执行影响的行数为%d" % row_count)

    # 取出结果集中的一行数据
    row_result = cursor.fetchone(sql)
    print(row_result)

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()