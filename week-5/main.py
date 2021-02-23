import psycopg2
from faker import Faker
import names

con = psycopg2.connect(database="my_database", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")

print("Database opened successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE CUSTOMER2
       (ID INT PRIMARY KEY     NOT NULL,
       Name           TEXT    NOT NULL,
       Address            TEXT     NOT NULL,
       review        TEXT);''')
print("Table created successfully")
fake = Faker()


# def create_data(number):
#     temp = ""
#     for i in range(number + 1):
#         command = "INSERT INTO TEMP (ID,Name,Address,review) VALUES ("
#         ID = str(i)
#         name = names.get_full_name()
#         address = fake.address()
#         review = fake.text()
#         temp = temp + command + f"'{ID}'," + f"'{name}'," + f"'{address}'," + f"'{review}')" + "\n"
#         print("Created " + ID + " row.\n")
#     print(f"{number} rows created successfully")
#     return temp


# cur.execute(create_data(10))
# con.commit()
for i in range(100001):
    print(i)
    cur.execute("INSERT INTO CUSTOMER2 (ID,Name,Address,review) VALUES ('" + str(
        i) + "','" + names.get_full_name() + "','" + fake.address() + "','" + fake.text() + "')")
con.commit()
