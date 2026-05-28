"""
G63 — apps_department.py
"""
from flask import render_template, request, session
from classes.department  import Department
from classes.supermarket import Supermarket

prev_option = ""

def apps_department():
    global prev_option
    ulogin = session.get("user")
    if ulogin is not None:
        butshow = "enabled"
        butedit = "disabled"
        option  = request.args.get("option")

        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Department.current()
            Department.remove(obj.department_id)
            if not Department.previous():
                Department.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Department.get_id(0)) + ';' + \
                     request.form["department_info"] + ';' + \
                     request.form["supermarket_id"]
            obj = Department.from_string(strobj)
            Department.insert(obj.department_id)
            Department.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Department.current()
            obj.department_info = request.form["department_info"]
            obj.supermarket_id  = int(request.form["supermarket_id"])
            Department.update(obj.department_id)
        elif option == "first":    Department.first()
        elif option == "previous": Department.previous()
        elif option == "next":     Department.nextrec()
        elif option == "last":     Department.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))

        prev_option = option
        obj = Department.current()

        if option == 'insert' or len(Department.lst) == 0:
            did = Department.get_id(0)
            department_info = supermarket_id = ""
        else:
            did             = obj.department_id
            department_info = obj.department_info
            supermarket_id  = obj.supermarket_id

        return render_template("department.html",
                               butshow=butshow, butedit=butedit,
                               did=did, department_info=department_info,
                               supermarket_id=supermarket_id,
                               supermarkets=list(Supermarket.obj.values()),
                               ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
