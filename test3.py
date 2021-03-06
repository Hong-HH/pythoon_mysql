import mysql.connector
from mysql.connector.errors import Error
from datetime import datetime

try : 
    # 1. DB에 연결
    connection = mysql.connector.connect(host = 'yh-db_amazonaws.com', 
        database = 'streamlit_db', 
        user = 'python_user',
        password = '2105'
    )
    # 2. 쿼리문 만들기 : mysql workbench 에서 잘 되는것을 확인한 SQL문을 넣어준다.
    # 이렇게 함수를 쓰면 로컬타임으로 가져온다. 하지만 서버에 저장할때는 UTC로 넣어주어야 한다.
    current_time = datetime.now()

    query = '''insert into test
                 (name, date)
                 values
                (%s, %s);'''
    # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭 써주자.
    record = [('qqq',current_time), ('yyy',current_time), ('ppp',current_time)]
    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 쿼리문을 커서에 넣어서 실행한다. // 실제로 실행하는 것은 커서가 해준다.
    # 레코드는 직접입력말고 변수로 넣었을때 실행
    cursor.executemany(query, record)

    # 5. 커넥션을 커밋한다. => 디비에 영구적으로 반영하라는 뜻.
    connection.commit()

except Error as e:
    print('Error', e)
# finally는 필수는 아니다.
finally :
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')