from db.database import Database
from pprint import pprint as pp
from bson.objectid import ObjectId

class Aulas:
    def __init__(self):
    self.db = Database(database="atlas-cluster", collection= "Aulas")
    self.collection = self.db.collection

    def read_AulaDB_by_id(self, id: int):
        res = self.collection.find_one({'_id': ObjectId(id)})
        return res

    def update_AulaDB(self, id: int, professor: str, alunos: str, assunto: str):
        res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": {"professor": professor}})
        return res.modified_count

    def create_AulaDB(self, id: int, professor: str, alunos: str, assunto: str):
        res = self.collection.insert_one({professor: str, alunos: str, assunto: str})
        return res.inserted_id

    def delete_AulaDB(self, id: int, professor: str, alunos: str, assunto: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count