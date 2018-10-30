from flask import Flask, render_template, request, redirect, url_for

from forms import UserForm

from database import User, db

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY='a random string'
))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            object = User(username=form.username.data, password=form.password.data)
            db.session.add(object)
            db.session.commit()
            print(object.id)
            return redirect(url_for('create', pk=object.id))
    else:
        return render_template('index.html', form=form)

@app.route('/<int:pk>')
def create(pk):
    object = User.query.filter_by(id=pk).first()

    return render_template('detail.html', object=object)

@app.route('/update/<int:pk>', methods=['GET', 'POST'])
def update(pk):
    object = User.query.filter_by(id=pk).first()
    # object = User.objects.get(id=pk)
    form = UserForm(request.form, obj=object)

    # Todo: update 부분 수정하기
    if request.method == 'POST' and form.validate():
        print(object.username, object.password)
        print(form.username, form.password)

        object.username = form.username.data
        object.password = form.password.data

        print(object.username, object.password)

        db.session.commit()
        # form.populate_obj(object)
        # object.save()
        return 'edit success'
    else:
        return render_template('update.html', form=form)


    return 'update'

@app.route('/delete/<int:pk>')
def delete(pk):
    object = User.query.filter_by(id=pk).first()

    db.session.delete(object)
    db.session.commit()

    return 'delete success'

if __name__ == '__main__':
    app.run(debug=True)