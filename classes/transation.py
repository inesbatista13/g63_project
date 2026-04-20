"""
@author: António Brito / Carlos Bragança
(2025) objective: class Transaction
"""
from classes.gclass import Gclass
import datetime

class Transation(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and called 'id'
    att = ['_transaction_id', '_supermarket_id', '_supplier_id', '_delivery_date', '_amount']
    # Class header title
    header = 'Transation'
    # field description for use in, for example, input form
    des = ['Transation_id', 'Supermarket_id', 'Supplier_id', 'Delivery_date', 'Amount']

    # Constructor: Called when an object is instantiated
    def __init__(self, transaction_id, supermarket_id, supplier_id, delivery_date, amount):
        super().__init__()
        # Object attributes
        self._transaction_id = Transation.get_id(int(transaction_id))
        self._supermarket_id = int(supermarket_id)
        self._supplier_id = int(supplier_id)
        self._delivery_date = datetime.date.fromisoformat(delivery_date)
        self._amount = float(amount)
        # Add the new object to the dictionary of objects
        Transation.obj[self._transaction_id] = self
        # Add the id to the list of object ids
        Transation.lst.append(self._transaction_id)
        # Association lists
        self._supermarket = None
        self._supplier = None

    # transaction_id property
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, x):
        self._transaction_id = int(x)

    # supermarket_id property
    @property
    def supermarket_id(self):
        return self._supermarket_id

    @supermarket_id.setter
    def supermarket_id(self, x):
        self._supermarket_id = int(x)

    # supplier_id property
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, x):
        self._supplier_id = int(x)

    # delivery_date property
    @property
    def delivery_date(self):
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        self._delivery_date = delivery_date

    # amount property
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = float(amount)

    # Association 1:N — Transaction -> Supermarket
    @property
    def supermarket(self):
        return self._supermarket

    @supermarket.setter
    def supermarket(self, s):
        self._supermarket = s
        self._supermarket_id = s.supermarket_id

    # Association 1:N — Transaction -> Supplier
    @property
    def supplier(self):
        return self._supplier

    @supplier.setter
    def supplier(self, s):
        self._supplier = s
        self._supplier_id = s.supplier_id