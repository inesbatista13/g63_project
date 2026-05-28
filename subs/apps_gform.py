"""
G63 — apps_gform.py
"""
from flask import render_template, request, session
from classes.supermarket import Supermarket
from classes.department  import Department
from classes.supplier    import Supplier
from classes.transation  import Transation

prev_option = ""

def apps_gform(cname=''):
    global prev_option
    ulogin = session.get("user")
    if ulogin is not None:
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option  = request.args.get("option")

        if prev_option == 'insert' and option == 'save':
            strobj = request.form[cl.att[0]]
            for i in range(1, len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()

        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            for i in range(1, len(cl.att)):
                setattr(obj, cl.att[i], request.form[cl.att[i]])
            cl.update(getattr(obj, cl.att[0]))

        else:
            if option == "edit":
                butshow, butedit = "disabled", "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(getattr(obj, cl.att[0]))
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow, butedit = "disabled", "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":    cl.first()
            elif option == "previous": cl.previous()
            elif option == "next":     cl.nextrec()
            elif option == "last":     cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))

        prev_option = option
        obj = cl.current()

        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            obj[cl.att[0]] = cl.get_id(0)
            for i in range(1, len(cl.att)):
                obj[cl.att[i]] = ""
        return render_template("gform.html",
                               butshow=butshow, butedit=butedit,
                               cname=cname, obj=obj,
                               att=cl.att, des=cl.des,
                               ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
