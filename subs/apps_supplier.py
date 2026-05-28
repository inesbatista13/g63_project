"""
G63 — apps_supplier.py

"""
from flask import render_template, request, session
from classes.supplier import Supplier

prev_option = ""

def apps_supplier():
    global prev_option
    ulogin = session.get("user")
    if ulogin is not None:
        butshow = "enabled"
        butedit = "disabled"
        option  = request.args.get("option")

        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Supplier.current()
            Supplier.remove(obj.supplier_id)
            if not Supplier.previous():
                Supplier.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Supplier.get_id(0)) + ';' + \
                     request.form["supplier_name"] + ';' + \
                     request.form["supplier_type"]
            obj = Supplier.from_string(strobj)
            Supplier.insert(obj.supplier_id)
            Supplier.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Supplier.current()
            obj.supplier_name = request.form["supplier_name"]
            obj.supplier_type = request.form["supplier_type"]
            Supplier.update(obj.supplier_id)
        elif option == "first":    Supplier.first()
        elif option == "previous": Supplier.previous()
        elif option == "next":     Supplier.nextrec()
        elif option == "last":     Supplier.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))

        prev_option = option
        obj = Supplier.current()

        if option == 'insert' or len(Supplier.lst) == 0:
            sid = Supplier.get_id(0)
            supplier_name = supplier_type = ""
        else:
            sid           = obj.supplier_id
            supplier_name = obj.supplier_name
            supplier_type = obj.supplier_type

        return render_template("supplier.html",
                               butshow=butshow, butedit=butedit,
                               sid=sid, supplier_name=supplier_name,
                               supplier_type=supplier_type,
                               ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
