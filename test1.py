import mysql.connector 
from mysql.connector.errors import Error
# 연결하는 코드
# try 라고 나오면, 들여쓰기 되어있는 문장들을 실행하라는 뜻.

try : 
    connection = mysql.connector.connect(host = 'yh-db.amazonaws.com', 
        database = 'streamlit_db', 
        user = 'python_user',
        password = '2105'
    )

    if connection.is_connected() :
        db_info = connection.get_server_info()
        print('MySQL info', db_info)
# 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
except Error as e :
    # 뒤의 e는 에러를 찍어라 error를 e로 저장했으니까!
    print('Error while connecting to MySQL', e)
# finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
finally : 
    if connection.is_connected():
        connection.close()
        print('MySQL connection is closed')
    else :
        print('connection does not exist')
