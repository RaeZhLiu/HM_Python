import pymysql

if __name__ == '__main__':
    # 1. 创建数据库连接对象
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='root',
                           database='jing_dong',
                           charset='utf8')

    # 2. 创建游标对象, 从而执行SQL语句
    cursor = conn.cursor()

    # 3. SQL语句
    sql = 'select * from goods;'

    # 4. 执行SQL语句（借助游标）
    cursor.execute(sql)

    # 5. 5.1获取一行的结果
    # row_result = cursor.fetchone()
    # print(row_result)

    #5. 5.2获取所有结果
    result = cursor.fetchall()
    for row_result in result:
        print(row_result)

    # 6. 关闭游标
    cursor.close()

    # 7. 关闭连接
    conn.close()

