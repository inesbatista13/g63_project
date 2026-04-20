#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(2026) objective: class Department
@author: admin
"""
from classes.gclass import Gclass

class Department(Gclass):
    obj      = dict()
    lst      = list()
    pos      = 0
    sortkey  = ''
    att      = ['_department_id', '_department_info', '_supermarket_id']
    header   = 'Department'
    des      = ['Department_Id', 'Department_Info', 'Supermarket_ID']

    # ── Constructor ──────────────────────────────────────────────────
    def __init__(self, department_id, department_info, supermarket_id):
        super().__init__()
        self._department_id   = Department.get_id(int(department_id))
        self._department_info = department_info
        self._supermarket_id  = int(supermarket_id)
        Department.obj[self._department_id] = self
        Department.lst.append(self._department_id)
        # Association (memory only — not stored in DB)
        self._supermarket = None   # 1:N -> Supermarket object

    # ── Properties ───────────────────────────────────────────────────
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, x):
        self._department_id = int(x)

    @property
    def department_info(self):
        return self._department_info

    @department_info.setter
    def department_info(self, info):
        self._department_info = info

    @property
    def supermarket_id(self):
        return self._supermarket_id

    @supermarket_id.setter
    def supermarket_id(self, si):
        self._supermarket_id = int(si)

    # ── Association 1:N  Department -> Supermarket ───────────────────
    @property
    def supermarket(self):
        return self._supermarket

    @supermarket.setter
    def supermarket(self, s):
        self._supermarket = s
        self._supermarket_id = s.supermarket_id