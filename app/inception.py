#coding=utf-8

import MySQLdb

def table_structure(mysql_structure,mysql_ip,mysql_port,mysql_user,mysql_password,mysql_database,mysql_action):
    sql1='/*--user='+mysql_user+';--password='+mysql_password+';--host='+mysql_ip+';--'+mysql_action+'=1;--port='+mysql_port+';*/\
            inception_magic_start;\
            use '+mysql_database+';'
    sql2='inception_magic_commit;'
    sql = sql1 + mysql_structure + sql2
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='',port=6669,use_unicode=True, charset="utf8")
        cur=conn.cursor()
        ret=cur.execute(sql)
        result=cur.fetchall()
        #f=file("log.txt","a+")
        #f.write(result[1][4])
        #f.close()
        return result
        num_fields = len(cur.description) 
        field_names = [i[0] for i in cur.description]
        print field_names
        for row in result:
            print row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10]
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return result[1][4].split("\n") 
