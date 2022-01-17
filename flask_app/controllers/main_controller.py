from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.menu import Menu
from flask_app.models.request import Request
from flask_app.models.info import Info
import datetime


@app.route('/')
def index():
    info = Info.all_info()
    return render_template('index.html', info = info[0])

@app.route('/menu')
def menu():
    menu_item = Menu.all_menu_items()
    return render_template('menu.html', menu_items = menu_item)

@app.route('/about')
def about():
    info = Info.all_info()
    return render_template('about&location.html', info = info[0])



@app.route("/form/selection")
def select():
    return render_template("form_select.html")


@app.route("/form/catering_request")
def catering_request_form():
    return render_template("catering_request.html")

@app.route("/submit/catering_request", methods=['POST'])
def submit_catering_request():

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'phone' : request.form['phone'],
        'company' : request.form['company'],
        'type' : "Catering",
        'guestnum' : request.form['guestnum'],
        'description' : request.form['description'],
        'address' : request.form['address'],
        'city' : request.form['city'],
        'state' : request.form['state'],
        'zip' : str(request.form['zip']),
        'start' : request.form['start'],
        'end' : request.form['end']
    }

    Request.submit_request(data)

    return redirect("/submit/successful")


@app.route("/form/contact_request")
def contact_request_form():
    return render_template("contact_request.html")

@app.route("/submit/contact_request", methods=['POST'])
def submit_contact_request():

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'phone' : request.form['phone'],
        'company' : 'N/A',
        'type' : "Contact",
        'guestnum' : 0,
        'description' : request.form['description'],
        'address' : request.form['address'],
        'city' : request.form['city'],
        'state' : request.form['state'],
        'zip' : str(request.form['zip']),
        'start' : '1900-12-30 00:00:00',
        'end' : '1900-12-30 00:00:00'
    }

    Request.submit_request(data)

    return redirect("/submit/successful")

@app.route('/submit/successful')
def success():
    return render_template('successfulsubmit.html')


@app.route("/admin/tempkey/create/menu_item")
def create_menu_item():
    return render_template("new_menu_item.html")

@app.route("/admin/tempkey/submit/menu_item", methods=['POST'])
def submit_menu_item():

    data = {
        'name' : request.form['name'],
        'price' : request.form['price'],
        'category' : request.form['category'],
        'description' : request.form['description']
    }

    Menu.submit_menu_item(data)

    return redirect("/admin/tempkey")






@app.route('/admin/tempkey')
def admindashboard():

    menu_items = Menu.all_menu_items()
    requests = Request.all_requests()

    defaultTime = datetime.datetime(1900, 12, 30, 0, 0, 0)
    print(defaultTime)

    return render_template('admin_dashboard.html', menu_items = menu_items, requests = requests, defaultTime = defaultTime)

@app.route('/admin/tempkey/completed_requests')
def completed_requests():
    request = Request.all_requests()
    return render_template('completed_requests.html', requests = request)

@app.route("/admin/tempkey/delete/complete_catering_requests")
def delete_completed_catering_requests():

    Request.delete_completed_catering_requests()
    
    return redirect("/admin/tempkey/completed_requests")

@app.route("/admin/tempkey/revert_completed_request_update/<int:request_id>", methods=['POST'])
def revert_completed_request_status(request_id):

    # if not Request.validate_request(request.form):
    #     return redirect(f"/admin/tempkey/submit_edit_request/{request_id}")

    data = {
        'request_id' : request_id,
        'type' : request.form['type']
    }

    Request.update_request_status(data)

    return redirect("/admin/tempkey/completed_requests")

@app.route("/admin/tempkey/delete/complete_contact_requests")
def delete_completed_contact_requests():

    Request.delete_completed_contact_requests()
    
    return redirect("/admin/tempkey/completed_requests")

@app.route('/admin/tempkey/spam_requests')
def spam_requests():
    request = Request.all_requests()
    return render_template('spam_requests.html', requests = request)

@app.route("/admin/tempkey/delete/spam_catering_requests")
def delete_spam_catering_requests():

    Request.delete_spam_catering_requests()
    
    return redirect("/admin/tempkey/spam_requests")

@app.route("/admin/tempkey/delete/spam_contact_requests")
def delete_spam_contact_requests():

    Request.delete_spam_contact_requests()
    
    return redirect("/admin/tempkey/spam_requests")

@app.route("/admin/tempkey/revert_spam_request_update/<int:request_id>", methods=['POST'])
def revert_spam_request_status(request_id):

    # if not Request.validate_request(request.form):
    #     return redirect(f"/admin/tempkey/submit_edit_request/{request_id}")

    data = {
        'request_id' : request_id,
        'type' : request.form['type']
    }

    Request.update_request_status(data)

    return redirect("/admin/tempkey/spam_requests")

@app.route("/admin/tempkey/delete/request/<int:request_id>")
def delete_request(request_id):

    data = {
        "request_id" : request_id
    }

    Request.delete_request(data)
    
    return redirect("/admin/tempkey/completed_requests")



@app.route("/admin/tempkey/submit_request_update/<int:request_id>", methods=['POST'])
def update_request_status(request_id):

    # if not Request.validate_request(request.form):
    #     return redirect(f"/admin/tempkey/submit_edit_request/{request_id}")

    data = {
        'request_id' : request_id,
        'type' : request.form['type']
    }

    Request.update_request_status(data)

    return redirect("/admin/tempkey")


@app.route('/admin/tempkey/catering_info/<int:request_id>')
def admin_catering_info(request_id):

    data = {
        "request_id" : request_id
    }

    requests = Request.one_request(data)

    # defaultTime = datetime.datetime(1900, 12, 30, 0, 0, 0)
    # print(defaultTime)

    return render_template('catering_info.html', requests = requests)

@app.route('/admin/tempkey/menu_item_info/<int:menu_item_id>')
def admin_menu_item_info(menu_item_id):

    data = {
        "menu_item_id" : menu_item_id
    }

    menu_items = Menu.one_menu_item(data)

    return render_template('menu_item_info.html', menu_items = menu_items)


@app.route('/admin/tempkey/edit_request/<int:request_id>')
def admin_edit_request(request_id):

    data = {
        "request_id" : request_id
    }

    requests = Request.one_request(data)

    return render_template('edit_request.html', requests = requests)

@app.route("/admin/tempkey/submit_edit_request/<int:request_id>", methods=['POST'])
def submit_edit_request(request_id):

    # if not Request.validate_request(request.form):
    #     return redirect(f"/admin/tempkey/submit_edit_request/{request_id}")

    data = {
        'request_id' : request_id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'phone' : request.form['phone'],
        'company' : request.form['company'],
        'type' : request.form['type'],
        'guestnum' : str(request.form['guestnum']),
        'description' : request.form['description'],
        'address' : request.form['address'],
        'city' : request.form['city'],
        'state' : request.form['state'],
        'zip' : str(request.form['zip']),
        'start' : request.form['start'],
        'end' : request.form['end']
    }

    Request.edit_request(data)

    return redirect("/admin/tempkey")




@app.route('/admin/tempkey/edit/menu_item/<int:menu_item_id>')
def admin_edit_menu_item(menu_item_id):

    data = {
        "menu_item_id" : menu_item_id
    }

    menu_items = Menu.one_menu_item(data)

    return render_template('edit_menu_item.html', menu_items = menu_items)

@app.route("/admin/tempkey/submit_edit/menu_item/<int:menu_item_id>", methods=['POST'])
def submit_edit_menu_item(menu_item_id):

    # if not Menu.validate_menu_item(menu_item.form):
    #     return redirect(f"/admin/tempkey/submit_edit_menu_item/{menu_item_id}")

    data = {
        'menu_item_id' : menu_item_id,
        'name' : request.form['name'],
        'category' : request.form['category'],
        'price' : request.form['price'],
        'description' : request.form['description']
    }

    Menu.update_menu_item(data)

    return redirect("/admin/tempkey")


@app.route("/admin/tempkey/delete/menu_item/<int:menu_item_id>")
def delete(menu_item_id):

    data = {
        "menu_item_id" : menu_item_id
    }

    Menu.delete_menu_item(data)
    
    return redirect("/admin/tempkey")