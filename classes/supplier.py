"""
(2025) objective: class Supplier
"""
from classes.gclass import Gclass

class Supplier(Gclass):
    obj      = dict()
    lst      = list()
    pos      = 0
    sortkey  = ''
    att      = ['_supplier_id', '_supplier_name', '_supplier_type']
    header   = 'Suppliers'
    des      = ['supplier_id', 'supplier_name', 'supplier_type']

    # Constructor 
    def __init__(self, supplier_id, supplier_name, supplier_type):
        super().__init__()
        supplier_id = Supplier.get_id(int(supplier_id))
        self._supplier_id   = int(supplier_id)
        self._supplier_name = supplier_name
        self._supplier_type = supplier_type
        Supplier.obj[supplier_id] = self
        Supplier.lst.append(supplier_id)
        # Association list
        self._transactions = []   # M:N -> Transaction objects

    # Properties 
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        self._supplier_id = supplier_id

    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        self._supplier_name = supplier_name

    @property
    def supplier_type(self):
        return self._supplier_type

    @supplier_type.setter
    def supplier_type(self, supplier_type):
        self._supplier_type = supplier_type

    # Association M:N — Supplier <-> Supermarket via Transaction 
    def add_transaction(self, transaction):
        """Links a Transaction object to this Supplier."""
        self._transactions.append(transaction)

    def get_transactions(self):
        """Returns all Transaction objects of this Supplier."""
        return self._transactions

    def get_supermarkets(self):
        """Returns unique Supermarket objects supplied by this Supplier."""
        supermarkets = []
        for t in self._transactions:
            if t.supermarket not in supermarkets:
                supermarkets.append(t.supermarket)
        return supermarkets
