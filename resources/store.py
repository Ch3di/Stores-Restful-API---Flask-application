from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.findStoreByName(name)
        if store:
            return store.json()
        return { "message": name + " was not found" }, 404

    def post(self,name):
        if StoreModel.findStoreByName(name):
            return { "message": name + " has already existed" }, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return { "message": "an error was occured while creating the store" }, 500
        return store.json()

    def delete(self,name):
        store = StoreModel.findStoreByName(name)
        if store:
            try:
                store.delete_from_db()
                return { "message" : name + " store has been deleted"}
            except:
                return { "message": "an error was occured while deleting the store" }, 500
        return { "message": "The requested store was not found" },400

class StoreList(Resource):
    def get(self):
        return { "stores": [store.json() for store in StoreModel.query.all()]}
