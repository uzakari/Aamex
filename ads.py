from flask import render_template, flash, redirect, url_for, make_response, request
from model import app
from forms import Login_Form, signUP_form, add_item
from model import Signup, db, Additemmodel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from model import admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask_velox.views.sqla.delete import DeleteObjectView

#
#
# class MyView(DeleteObjectView):
#     model = Additemmodel
#     session = db.session
#     template = 'deliveries_cute.html'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/product', methods=['GET', 'POST'])
@login_required
def product():
    form = add_item()
    if form.validate_on_submit():
        new_item = Additemmodel(date=form.date.data, sender_name=form.sender_name.data,
                                sender_number=form.sender_number.data, recipient_name=form.Recipient_name.data,
                                recipient_number=form.Recipent_number.data,
                                payment=form.Payment.data,
                                address=form.address.data,
                                delivery_mode=form.Delivery_mode.data, services=form.Service.data,
                                Item_Deliver=form.Product.data,
                                Signup=current_user
                            )
        db.session.add(new_item)
        db.session.commit()
        flash('A new delivery is added')
        return redirect(url_for('deliveries'))
    return render_template('product.html', name=current_user.name, form=form)


@app.route('/product_edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    edit_item = Additemmodel.query.get_or_404(id)
    form = add_item()
    if form.validate_on_submit():
        edit_item.sender_name = form.sender_name.data
        edit_item.sender_number = form.sender_number.data
        edit_item.recipient_name = form.Recipient_name.data
        edit_item.delivery_mode = form.Delivery_mode.data
        edit_item.services = form.Service.data
        edit_item.date = form.date.data
        edit_item.payment = form.Payment.data
        edit_item.recipient_number = form.Recipent_number.data
        edit_item.address = form.address.data
        edit_item.Item_Deliver = form.Product.data
        db.session.add(edit_item)
        db.session.commit()
        flash('The Delivery is updated')
        return redirect(url_for('deliveries'))
    form.sender_name.data = edit_item.sender_name
    form.sender_number.data = edit_item.sender_number
    form.Recipient_name.data = edit_item.recipient_name
    form.Delivery_mode.data = edit_item.delivery_mode
    form.Service.data = edit_item.services
    form.date.data = edit_item.date
    form.Payment.data = edit_item.payment
    form.Recipent_number.data = edit_item.recipient_number
    form.address.data = edit_item.address
    form.Product.data = edit_item.Item_Deliver
    return render_template('product.html', form=form, edit_item=edit_item, name=current_user.name)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    delete_candidate = Additemmodel.query.get_or_404(id)
    db.session.delete(delete_candidate)
    db.session.commit()
    flash('You have deleted the item')
    return redirect(url_for('deliveries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        user = Signup.query.filter_by(email=form.email.data).first()
        if user is not None and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('deliveries'))
        flash("Invalid User name or password")
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = signUP_form()
    if form.validate_on_submit():
        user = Signup(name=form.name.data, email=form.email.data,
                      password=generate_password_hash(form.password.data, method='sha256'))
        db.session.add(user)
        db.session.commit()
        flash('New user has been created')
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)


@app.route('/deliveries')
@login_required
def deliveries():
    page = request.args.get('page', 1, type=int)
    pagination = Additemmodel.query.order_by(Additemmodel.date.desc()).paginate(per_page=5, page=page, error_out=False)
    deliveriess = pagination.items
    a = Additemmodel.query.filter(Signup.id == Additemmodel.id).all()
    return render_template('deliveries_cute.html', deliveriess=deliveriess, a=a, pagination=pagination)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/receipt/<int:id>', methods=['GET', 'POST'])
def receipt(id):
    Item = Additemmodel.query.get_or_404(id)
    return render_template('receipt.html', Item=Item)


# @app.route('/print/<int:id>', methods=['GET', 'POST'])
# def pdf_template(id):
#     Item = Additemmodel.query.get_or_404(id)
#     rendered = render_template('receipt.html', Item=Item)
#     # css = ['static/receipt.css']
#     pdf = pdfkit.from_string(rendered, False)
#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'inline; filename=ads.pdf'
#
#     return response
admin.add_view(ModelView(Signup, db.session))
admin.add_view(ModelView(Additemmodel, db.session))
if __name__ == '__main__':
    app.run(debug=True)
