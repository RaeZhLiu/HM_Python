from pymysql import connect


if __name__ == '__main__':
    # 创建连接对象
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='jing_dong',
        charset='utf8'
    )

    # 创建游标对象
    cursor = conn.cursor()

    # 执行SQL
    sql_create = "create table mytest(id int unsigned primary key auto_increment not null, name varchar(40) not null);"
    sql_insert = "insert into mytest(name) values(%s);"
    sql_select = "select * from mytest;"
    sql_update = "update mytest set name=%s where id=%s;"
    sql_select_1 = "select * from mytest where id=%s;"
    sql_del = "delete from mytest where id=%s;"

    try:
        # 创建 mytest 表
        cursor.execute(sql_create)
        conn.commit()
        try:
            # 插入 10000 条数据
            for i in range(10000):
                cursor.execute(sql_insert, ["手机"+str(i)])
            conn.commit()
            try:
                # 查询并返回 mytest 表中的所有数据
                cursor.execute(sql_select)
                for row1 in cursor.fetchall():
                    print(row1)
            except Exception as s_select_error:
                print("第一次查询失败！")

            try:
                # 更新符合条件的记录
                cursor.execute(sql_update, ["手机new", 100])
                conn.commit()
            except Exception as update_error:
                print("update data error!")
                conn.rollback()

            try:
                # 查询并返回符合条件的数据
                cursor.execute(sql_select_1, [100])
                for row2 in cursor.fetchall():
                    print("修改后的:", row2)
            except Exception as s_select_error:
                print("第二次查询失败！")

            try:
                # 删除数据
                cursor.execute(sql_del, [10000])
                conn.commit()
            except Exception as del_error:
                print("delete data error!")
                conn.rollback()

            try:
                # 查询并返回 mytest 表中的所有数据
                cursor.execute(sql_select)
                for row3 in cursor.fetchall():
                    print(row3)
            except Exception as s_select_error:
                print("第三次查询失败！")


        except Exception as insert_error:
            print("insert data error!")
            conn.rollback()

    except Exception as create_error:
        print("creat table error!")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
