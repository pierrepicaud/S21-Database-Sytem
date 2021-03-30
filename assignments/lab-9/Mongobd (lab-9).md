Mongobd (lab-9)

# Mongobd (lab-9)
code to connect: `mongodb+srv://postgres:<postgres>@cluster0.hqjrb.mongodb.net/test`

- [x] Find all the documents in the collection restaurants
	`inno_db.restaurants.find()` with empty fields, it shows everything
- [x] Find the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
	`inno_db.restaurants.find({},{restaurant_id: 1, name:1, borough: 1, cuisine:1})` it seems that nothing changes
- [x] Find the first 5 restaurant which is in the borough Bronx.
`inno_db.restaurants.find({borough:'Bronx'}).limit(5)`
- [x] Find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinese' or restaurant's name begins with the letter 'Wil’.
`inno_db.restaurants.find( { $or: [{cuisine: {$nin: ['American','Chinese']}}, {name: /^wil.*$/}] },{restaurant_id: 1, name:1, borough: 1, cuisine:1} )`
- [x]  Find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which contains 'mon' as three letters somewhere in its name.
`inno_db.restaurants.find({name: /mon/},{name:1, borough:1, longitude:1, attitude:1, cuisine:1})`
- [x] Find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronx or Brooklyn.
`inno_db.restaurants.find({borough: {$in:['Staten Island', 'Bronx', 'Brooklyn', 'Queens']}},{restaurant_id: 1, name:1, borough: 1, cuisine:1})`