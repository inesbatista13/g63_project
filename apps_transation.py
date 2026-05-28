"""
G63 — apps_transation.py
"""
from flask import render_template, request, session
from classes.transation  import Transation
from classes.supermarket import Supermarket
from classes.supplier    import Supplier

prev_option = ""

def apps_transation():
    global prev_option
    ulogin = session.get("user")
    if ulogin is not None:
        butshow = "enabled"
        butedit = "disabled"
        option  = request.args.get("option")

        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Transation.current()
            Transation.remove(obj.transaction_id)
            if not Transation.previous():
                Transation.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Transation.get_id(0)) + ';' + \
                     request.form["supermarket_id"] + ';' + \
                     request.form["supplier_id"]    + ';' + \
                     request.form["delivery_date"]  + ';' + \
                     request.form["amount"]
            obj = Transation.from_string(strobj)
            Transation.insert(obj.transaction_id)
            Transation.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Transation.current()
            obj.supermarket_id = int(request.form["supermarket_id"])
            obj.supplier_id    = int(request.form["supplier_id"])
            obj.delivery_date  = request.form["delivery_date"]
            obj.amount         = float(request.form["amount"])
            Transation.update(obj.transaction_id)
        elif option == "first":    Transation.first()
        elif option == "previous": Transation.previous()
        elif option == "next":     Transation.nextrec()
        elif option == "last":     Transation.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))

        prev_option = option
        obj = Transation.current()

        if option == 'insert' or len(Transation.lst) == 0:
            tid = Transation.get_id(0)
            supermarket_id = supplier_id = delivery_date = amount = ""
        else:
            tid            = obj.transaction_id
            supermarket_id = obj.supermarket_id
            supplier_id    = obj.supplier_id
            delivery_date  = obj.delivery_date
            amount         = obj.amount

        return render_template("transation.html",
                               butshow=butshow, butedit=butedit,
                               tid=tid, supermarket_id=supermarket_id,
                               supplier_id=supplier_id,
                               delivery_date=delivery_date, amount=amount,
                               supermarkets=list(Supermarket.obj.values()),
                               suppliers=list(Supplier.obj.values()),
                               ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
