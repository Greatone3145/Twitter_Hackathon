import psycopg2
import os

hitMisArr = []
restInfo = []
pathNames = []
masterBinary= []
masterInfo = []

try:
    conn = psycopg2.connect(host='localhost',
                            dbname='Stock_Tweets',
                            user='postgres',
                            password='kickAlessio',
                            port = 5432)

    curr = conn.cursor()

    get_info = "SELECT * FROM {dir};"
    delete_all_query = "DROP TABLE amd,bam,bmo,bns,csco,fb,mfc,qqq,td,tsla;"
    insert_query = "INSERT INTO {dir} (hit, sentiment, nbLikes, movement) VALUES (%s, %s, %s, %s);"
    create_query = "CREATE TABLE {dir} (hit BOOLEAN, sentiment REAL, nbLikes INTEGER, movement INTEGER);"

    # folder path
    dir_path = r'C:\Users\user1\Desktop\Stocks'

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):

            pathNames.append(path)

            file = open(dir_path + '\\' + path)

            pathV2 = os.path.splitext(path)[0]
            curr.execute(create_query.format(dir=pathV2))

            for line in file:
                data = line.split()

                hitMis = int(data[0])
                sentiment = int(data[1])
                like = int(data[2])
                movement = int(data[3])

                hitMisArr.append(hitMis)
                temp = [sentiment, like]
                restInfo.append(temp)

                if hitMis == 1:
                    hitMis = False
                else:
                    hitMis = True

                curr.execute(insert_query.format(dir=pathV2), (hitMis, sentiment, like, movement))

            file.close()
            masterInfo.append(restInfo)
            masterBinary.append(hitMisArr)
            restInfo = []
            hitMisArr = []

    print(restInfo)
    print(hitMisArr)
    conn.commit()
    conn.close()

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
    if curr is not None:
        curr.close()