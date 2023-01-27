from abstraction import Storage


class Store(Storage):

    def __init__(self, name):
        self._items = {}
        self._capacity = 100
        self.__name = name

    def __repr__(self):
        return self.__name

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def add(self, title, quantity):
        if title in self.items.keys():
            self.items[title] += quantity
        else:
            self.items[title] = quantity
        self.capacity -= quantity

    def remove(self, title, quantity):
        self.items[title] -= quantity
        self.capacity += quantity
        if self.items[title] == 0:
            self.items.pop(title)

    def get_free_space(self) -> int:
        return self.capacity

    def get_items(self) -> dict:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)


class Shop(Storage):

    def __init__(self, name):
        self._items = {}
        self._capacity = 20
        self._items_limit = 5
        self.__name = name

    def __repr__(self):
        return self.__name

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def items_limit(self):
        return self._items_limit

    def add(self, title, quantity):
        if title in self.items.keys():
            self.items[title] += quantity
        else:
            self.items[title] = quantity
        self.capacity -= quantity

    def remove(self, title, quantity):
        self.items[title] -= quantity
        self.capacity += quantity
        if self.items[title] == 0:
            self.items.pop(title)

    def get_free_space(self) -> int:
        return self.capacity

    def get_items(self) -> dict:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)


class Request:
    def __init__(self, vaults: list, request: str):
        self._from = ""
        self._to = ""
        self._amount = 0
        self._product = ""
        self._depots = vaults
        self._request = request

    @property
    def otkuda(self):
        self._from = self._split_request("из", 1)
        return self._from

    @property
    def to(self):
        self._to = self._split_request("в", 1)
        return self._to

    @property
    def amount(self):
        self._amount = int(self._split_request("из", -2))
        return self._amount

    @property
    def product(self):
        self._product = self._split_request("из", -1)
        return self._product

    def _split_request(self, pivot, shift):
        list_request = self._request.split(" ")
        if pivot not in list_request:
            return None
        reply = list_request[list_request.index(pivot) + shift]
        return reply
