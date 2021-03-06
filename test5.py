import mysql.connector 
from mysql.connector.errors import Error

from mysql_connection import get_connection
# 연결하는 코드
# try 라고 나오면, 들여쓰기 되어있는 문장들을 실행하라는 뜻.

try : 
    connection = get_connection()
    
    query = '''select * from test'''

    # select 결괄르 딕셔너리로 가져오는 경우
    cursor = connection.cursor(dictionary = True)

    cursor.execute(query)

    # select 문은 아래 내용이 필요하다.
    # 커서로 부터 실행한 결과 전부를 받아와라.
    record_list = cursor.fetchall()
    print(record_list)

    # 컬럼의 이름이 키 값으로 온다.
    for row in record_list :
        print('id =', row['id'])
        print('name =', row['name'])
        print('date =', row['date'].isoformat())
# 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
except Error as e :
    # 뒤의 e는 에러를 찍어라 error를 e로 저장했으니까!
    print('Error while connecting to MySQL', e)
# finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
finally : 
    print('finally')
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')
    else :
        print('connection does not exist') 