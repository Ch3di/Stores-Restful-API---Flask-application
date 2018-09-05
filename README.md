# Stores Restful API
This is a simple RESTful API written using Flask python framework.
It helps to manage stores objects which hold some items.
## Developed endpoints
* \[GET\]: _/register_

Registers a user

* \[GET\]: _/auth_
signs in an existing user to generate the JWT key

* \[GET\]: _/items_
Gets an array named 'items' which contains all the items objects

* \[GET\]: _/item/<name>_
Returns a json which contains the <name> of the item and its 'price'
**NOTE:** JWT key is required for this request

* \[POST\]: _/item/<name>_
Adds a new item
The json payload must contain "price" : float and "store_id": integer

* \[PUT\]: _/item/<name>_
Updates an existing item or creates new one if it doesn't exist
'price': <float> is required in the json payload

* \[DELETE\]: _/item/<name>_
Deletes an existing item

* \[GET\]: _/stores_
Gets an array named 'stores' which contains all the stores

* \[GET\]: _/store/<name>_
Returns a json which contains the <name> of the store and an array of the associeted items objects

* \[POST\]: _/store/<name>_
Creates a new store

* \[DELETE\]: _/store/<name>_
Deletes an existing store

## Python dependencies
* Flask
`$ pip install Flask`
* Flask-RESTful
`$ pip install Flask-RESTful`
* Flask-SQLAlchemy
`$ pip install Flask-SQLAlchemy`
* Flask-JWT
`$ pip install Flask-JWT`
* uwsgi
`$ pip install uwsgi`
* psycopg2
`$ pip install psycopg2`

## Deployment
All Heruko configuration files are included
You can simply deploy the application to Heruko by connecting to github.
## License
The content of this repository is licensed under a [Creative Commons Attribution License](https://creativecommons.org/licenses/by/3.0/us/)
