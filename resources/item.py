from flask_restful import reqparse, Resource # reqparse : parsing the request to match some criterias
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser() # creates a parser object
    # add an argument
    parser.add_argument('price', #argument name
        type=float, # force the type to be float
        required=True, # required argument, without it, the req would fail
        help="This field cannot be left blank" # msg for the user when the request fails
    )
    parser.add_argument('store_id', #argument name
        type=int, # force the type to be float
        required=True, # required argument, without it, the req would fail
        help="This field cannot be left blank" # msg for the user when the request fails
    )
    @jwt_required()
    def get(self,name):
        item = ItemModel.findItemByName(name)
        if item:
            return item.json()
        return  { "message" : name + " is not found"}, 404


    def post(self,name):
        if ItemModel.findItemByName(name):
            return { "message": "the item {} has already existed".format(name) }, 400 # 400 for Bad request

        # data = request.get_json() # read the json payload sent in the request body
        # Note : any passed argument which is not included with an .add_argument will be rejected
        data = Item.parser.parse_args() # get the data
        item = ItemModel(name,**data)
        item.save_to_db()
        return item.json(),201

    def delete(self,name):
        item = ItemModel.findItemByName(name)
        if item:
            item.delete_from_db()
            return { "message": name + " was deleted" }, 200
        return { "message": "The requested item is not found. " + name + " was not deleted"},400

    def put(self,name):
        # Note : any passed argument which is not included with an .add_argument will be rejected
        data = Item.parser.parse_args() # get the data
        item = ItemModel.findItemByName(name)
        if item:
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(name, **data)
        item.save_to_db()
        return item.json()




class ItemsList(Resource):
    def get(self):
        return { "items" : [item.json() for item in ItemModel.query.all()]}
