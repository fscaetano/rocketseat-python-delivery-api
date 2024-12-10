from abc import ABC, abstractmethod


class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_document(self, document: dict) -> None:
        pass

    @abstractmethod
    def insert_list_of_documents(self, list_of_documents: list) -> None:
        pass

    @abstractmethod
    def select_many(self, doc_filter: dict) -> list:
        pass

    @abstractmethod
    def select_one(self, doc_filter: dict) -> dict:
        pass

    @abstractmethod
    def select_many_with_properties(self, doc_filter: dict) -> list:
        pass

    @abstractmethod
    def select_if_property_exists(self) -> list:
        pass

    @abstractmethod
    def select_by_object_id(self, object_id: str) -> list:
        pass

    @abstractmethod
    def edit_registry(self, object_id: str) -> None:
        pass

    @abstractmethod
    def edit_many_registries(self):
        pass

    @abstractmethod
    def edit_with_increment(self):
        pass

    @abstractmethod
    def delete_registry(self):
        pass

    @abstractmethod
    def delete_registries(self):
        pass
