import pymysql

# connnetcont mysql
connection = pymysql.connect ( host='localhost' ,   #ip
                               user='root' ,        #username
                               password='root' ,    #passwor
                               db='world' ,         #datebase name
                               port=3306 ,
                               charset='utf8' )

# query
try:
    # get cursor
    with connection.cursor () as cursor:
        sql = 'select * from city'
        cout = cursor.execute ( sql )
        for row in cursor.fetchall ():
            print ( "ID:{} Name:{} CountryCode{} District{} Poputaion{} ".format(row[0],row[1],row[2],row[3],row[4]) )
        print ( "count： " + str ( cout ) )
except:
    print('undefine exception')
finally:
    connection.close ()

# create table

# insert

# update

# delete



