from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # items = db.relationship('ItemsModel') # creates a list of items from ItemModel
    items = db.relationship('ItemModel', lazy="dynamic") # the Item Models will be created later when they are called

    def __init__(self, name):
        self.name = name


    def json(self):
        return { "name": self.name, "items": [item.json for item in self.items.all()] }

    @classmethod
    def findStoreByName(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self) # adding or updating an existing item using an ItemModel object
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
