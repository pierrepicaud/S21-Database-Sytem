import psycopg2
from geopy.geocoders import Nominatim
from faker import Faker
import names

# Openning Databas
con = psycopg2.connect(database="dvdrental", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432") # 5432 is the default port
print("Database opened successfully.\n")


# Calling function from python
cur = con.cursor()
cur.execute("SELECT get_address1();")
results = cur.fetchall()
print("Function processed successfully.\n")

#cur.execute("ALTER TABLE address ADD latitude varchar(50);")
#cur.execute("ALTER TABLE address ADD longitude varchar(50);")

for result in results:
    print(result[0])
    # User_Agent is an http request header that is sent with each request.
    geolocator = Nominatim(user_agent="duthamlieu@gmail.com")
    location = geolocator.geocode(result[0])
    if location is not None:
        print((location.latitude, location.longitude))
        cur.execute("UPDATE address SET latitude = %s, longitude = %s WHERE address.address = %s;",(location.latitude,location.longitude,result[0]))
    else:
        print(0,0)
        cur.execute("UPDATE address SET latitude = %s, longitude = %s WHERE address.address = %s;",(0, 0, result[0]))
con.commit()
