# 내업무 자동화  https://github.com/


import pyodbc

# 데이터베이스 연결 정보 설정
server = '데이터베이스 엔진'  # SQL Server의 주소 또는 이름
database = '210.180.103.100'  # 연결할 데이터베이스 이름
username = 'hns_prm'  # SQL Server 사용자명
password = '@tjqltmrhksflxla1'  # 사용자의 비밀번호

# 연결 문자열 생성
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

# 데이터베이스 연결
try:
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # SQL 쿼리 파일 읽기
    with open('pol_20230911.sql', 'r') as sql_file:
        sql_query = sql_file.read()

    # SQL 쿼리 실행
    cursor.execute(sql_query)

    # 결과 가져오기
    rows = cursor.fetchall()
    
    # 결과 출력 예제
    for row in rows:
        print(row)

    # 연결 종료
    cursor.close()
    connection.close()

except Exception as e:
    print(f"Error: {str(e)}")