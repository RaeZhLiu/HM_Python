import pymysql

if __name__ == '__main__':
    # 1. 创建数据库连接对象
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='jing_dong',
        charset='utf8'
    )

    # 2. 创建游标对象
    cursor = conn.cursor()

    # 3. 执行SQL语句，防止注入
    sql = 'insert into goods_cates(name) value(%s);'
    try:
        cursor.execute(sql, ("iphone",))
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        # 4. 关闭游标
        cursor.close()
        # 5. 关闭连接
        conn.close()

