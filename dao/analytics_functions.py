import pymysql.cursors
from dao.connection_info import *


TEST_QUERY = f'''
SELECT *
FROM tags;
'''

TEST_QUERY = f'''
SELECT *
FROM tags;
'''

def test_connection():
    connection = pymysql.connect(host=MYSQL_HOSTNAME,
                             port=3306,
                             user=MYSQL_USERNAME,
                             password=MYSQL_PASSWORD,
                             db='test_schema',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    # message = cursor.

    cursor.execute(TEST_QUERY)
    result = cursor.fetchall()
    for row in result:
        print(row["tag"])

    cursor.close()
    connection.close()

    return 0


def get_disaster_with_tags():
    connection = pymysql.connect(host=MYSQL_HOSTNAME,
                             port=3306,
                             user=MYSQL_USERNAME,
                             password=MYSQL_PASSWORD,
                             db='test_schema',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    # message = cursor.

    cursor.execute(TEST_QUERY)
    result = cursor.fetchall()
    for row in result:
        print(row["tag"])

    cursor.close()
    connection.close()

    return 0
