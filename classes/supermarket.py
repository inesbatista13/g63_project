"""
(2025) objective: class Supermarket
"""
from classes.gclass import Gclass
import datetime

class Supermarket(Gclass):
    obj      = dict()
    lst      = list()
    pos      = 0
    sortkey  = ''
    att      = ['_supermarket_id', '_name', '_opening_date']
    header   = 'Supermarkets'
    des      = ['supermarket_id', 'name', 'opening_date']

    # ── Constructor ──────────────────────────────────────────────────
    def __init__(self, supermarket_id, name, opening_date):
        super().__init__()
        supermarket_id = Supermarket.get_id(int(supermarket_id))
        self._supermarket_id = int(supermarket_id)
        self._name           = name
        self._opening_date   = datetime.date.fromisoformat(str(opening_date))
        Supermarket.obj[supermarket_id] = self
        Supermarket.lst.append(supermarket_id)
        # Association lists (memory only — not stored in DB)
        self._departments  = []   # 1:N  -> Department objects
        self._transactions = []   # M:N  -> Transaction objects

    # ── Properties ───────────────────────────────────────────────────
    @property
    def supermarket_id(self):
        return self._supermarket_id

    @supermarket_id.setter
    def supermarket_id(self, supermarket_id):
        self._supermarket_id = int(supermarket_id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def opening_date(self):
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        self._opening_date = opening_date

    # ── Association 1:N  Supermarket -> Department ───────────────────
    def add_department(self, dept):
        self._departments.append(dept)

    def get_departments(self):
        return self._departments

    # ── Association M:N  Supermarket <-> Supplier via Transaction ────
    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def get_transactions(self):
        return self._transactions

    def get_suppliers(self):
        """Returns unique Supplier objects that supply this Supermarket."""
        suppliers = []
        for t in self._transactions:
            if t.supplier not in suppliers:
                suppliers.append(t.supplier)
        return suppliers
