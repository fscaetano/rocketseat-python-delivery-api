import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="db interaction")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"client": "fafa2", "coupon": False, "items": [
        {"type": "drink", "name": "Pepsi", "quantity": 1}]}
    orders_repository.insert_document(my_doc)


@pytest.mark.skip(reason="db interaction")
def test_insert_list_of_document():
    orders_repository = OrdersRepository(conn)
    my_docs = [{"hello": "world", "answer": 42}, {"elem1": "value1"}, {
        "elem2": "value2"}, {"elem3": "value3"}, {"elem4": "value4"}]
    orders_repository.insert_list_of_documents(my_docs)


def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"coupon": True}
    data = orders_repository.select_many(doc_filter)

    print()
    [print(e) for e in data]


def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"coupon": False}
    data = orders_repository.select_one(doc_filter)

    print()
    print(data)


def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"coupon": True}
    data = orders_repository.select_many_with_properties(doc_filter)

    print()
    [print(e) for e in data]


def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    data = orders_repository.select_if_property_exists()

    print()
    [print(e) for e in data]


def test_select_many_with_multiple_filters():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "coupon": False,
        "address": {"$exists": True}
    }  # similar to AND filter
    data = orders_repository.select_many(doc_filter)

    print()
    [print(e) for e in data]


def test_select_many_with_nested_namesd_field_filters():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "member.livelo": {"$exists": True}  # nested
    }
    data = orders_repository.select_many(doc_filter)

    print()
    [print(e) for e in data]


def test_select_many_with_or_filters():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"coupon": False},
            {"address": {"$exists": True}}
        ]
    }
    data = orders_repository.select_many(doc_filter)

    print()
    [print(e) for e in data]


def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "6756692b1bfaedf8da6e3532"
    data = orders_repository.select_by_object_id(object_id)

    print()
    [print(e) for e in data]