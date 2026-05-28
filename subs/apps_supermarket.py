"""
G63 — apps_supermarket.py

"""
from flask import render_template, request, session
from classes.supermarket import Supermarket

prev_option = ""

def apps_supermarket():
    global prev_option
    ulogin = session.get("user")
    if ulogin is not None:
        butshow = "enabled"
        butedit = "disabled"
        option  = request.args.get("option")

        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Supermarket.current()
            Supermarket.remove(obj.supermarket_id)
            if not Supermarket.previous():
                Supermarket.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Supermarket.get_id(0)) + ';' + \
                     request.form["name"] + ';' + request.form["opening_date"]
            obj = Supermarket.from_string(strobj)
            Supermarket.insert(obj.supermarket_id)
            Supermarket.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Supermarket.current()
            obj.name         = request.form["name"]
            obj.opening_date = request.form["opening_date"]
            Supermarket.update(obj.supermarket_id)
        elif option == "first":    Supermarket.first()
        elif option == "previous": Supermarket.previous()
        elif option == "next":     Supermarket.nextrec()
        elif option == "last":     Supermarket.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))

        prev_option = option
        obj = Supermarket.current()

        if option == 'insert' or len(Supermarket.lst) == 0:
            sid = Supermarket.get_id(0)
            name = opening_date = ""
        else:
            sid          = obj.supermarket_id
            name         = obj.name
            opening_date = obj.opening_date

        return render_template("supermarket.html",
                               butshow=butshow, butedit=butedit,
                               sid=sid, name=name, opening_date=opening_date,
                               ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
