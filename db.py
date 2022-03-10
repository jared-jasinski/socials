import pymysql.cursors, time

# Connect to the database
def connect():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='password',
                                database='socials',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
                       
def add_entry(socials):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='password',
                                database='socials',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            for data in socials:
                i = 0
                i += 1
                time.sleep(3)
                datapoint = socials[data]

                sql = ("INSERT INTO `social_trends` (`coin_name`, `price`, `twitter_followers`, `reddit_subs`, `active_reddit_users`, `tg_users`, `wen`) VALUES (%s, %s,%s,%s,%s,%s,%s)"
                )
                cursor.execute(sql, (datapoint['name'], datapoint['price'], datapoint['twitter_followers'], datapoint['reddit_subscribers'], datapoint['active_reddit_users'], datapoint['tg_members'], time.time()))
                print('created entry number {}').format(i)
        connection.commit()
