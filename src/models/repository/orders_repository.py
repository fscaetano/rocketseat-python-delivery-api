from bson import ObjectId


class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find_one(doc_filter)
        return data

    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find(
            doc_filter,  # filter
            {"_id": 0, "coupon": 0}  # return options
        )
        return data

    def select_if_property_exists(self) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find(
            {"address": {"$exists": True}},
            {"_id": 0, "coupon": 0}  # return options)
        )
        return data

    def select_by_object_id(self, object_id: str) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find({"_id": ObjectId(object_id)})
        return data