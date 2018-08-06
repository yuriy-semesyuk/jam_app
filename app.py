import os.path

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from form.dateForm import DateForm
from form.masterForm import MasterForm
from form.priceForm import PriceForm
from form.typeservisForm import TypeservisForm
from form.userForms import UserForm

from function.time_function import list_time, time_int, time_setvic, time_all_sec, for_type_service

app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'myApp.sqlite')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    type_servis = db.Column(db.String(100), nullable=False)
    master = db.Column(db.String(20), nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    number = db.Column(db.String(20), nullable=False)

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.query.get(user_id)
            return user
        except Exception, e:
            return None

class Master(db.Model):
    master_name = db.Column(db.String(20), primary_key=True)

    @staticmethod
    def get_by_master_name(master_name):
        try:
            master = Master.query.get(master_name)
            return master
        except Exception, e:
            return None

class Price(db.Model):
    price_id = db.Column(db.Integer, primary_key=True)
    master_name = db.Column(db.String(100), nullable=False)
    servis_name = db.Column(db.String(100), nullable=False)
    servis_cost = db.Column(db.String(100), nullable=False)
    servis_duration = db.Column(db.String(100), nullable=False)

    @staticmethod
    def get_by_price_id(price_id):
        try:
            price = Price.query.get(price_id)
            return price
        except Exception, e:
            return None

class Typeservis():
    type_s_1 = None
    type_s_2 = None
    type_s_3 = None
    type_s_4 = None
    type_s_5 = None
    firstname = None
    number = None

    def set(self, type_s_1, type_s_2, type_s_3, type_s_4, type_s_5, firstname, number):
        self.type_s_1 = type_s_1
        self.type_s_2 = type_s_2
        self.type_s_3 = type_s_3
        self.type_s_4 = type_s_4
        self.type_s_5 = type_s_5
        self.firstname = firstname
        self.number = number

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.query.get(user_id)
            return user
        except Exception, e:
            return None

def get_by_price_id(price_id):
    try:
        price = Price.query.get(price_id)
        return price
    except Exception, e:
        return None

@app.route('/')
def index():
    return """
            <a href='http://localhost:5000/cal/'>user</a><br>
            """

@app.route('/user', methods=['GET'])
def user_get():
    users = User.query.all()
    return render_template('user.html', users=users)

@app.route('/user/add/<date_e>/<time_l>/<master_e>', methods=['GET', 'POST'])
def user_add(date_e, time_l, master_e):
    form = UserForm(request.form)
    form_for_servis = TypeservisForm(request.form)
    prices = Price.query.all()
    servis = ""
    if request.method == 'POST':
        typeservis = Typeservis()
        typeservis.set(form_for_servis.type_s_1.data,
                       form_for_servis.type_s_2.data,
                       form_for_servis.type_s_3.data,
                       form_for_servis.type_s_4.data,
                       form_for_servis.type_s_5.data,
                       form_for_servis.firstname.data,
                       form_for_servis.number.data)
        if typeservis.type_s_1:
            servis = servis + str(typeservis.type_s_1 + "/")
        if typeservis.type_s_2:
            servis = servis + str(typeservis.type_s_2 + "/")
        if typeservis.type_s_3:
            servis = servis + str(typeservis.type_s_3 + "/")
        if typeservis.type_s_4:
            servis = servis + str(typeservis.type_s_4 + "/")
        if typeservis.type_s_5:
            servis = servis + str(typeservis.type_s_5 + "/")
        print servis
        if request.method == 'POST':
            user = User(date=date_e,
                        time=time_l,
                        type_servis=servis,
                        master=master_e,
                        firstname=form_for_servis.firstname.data,
                        number=form_for_servis.number.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/cal/')
        return render_template('user_add.html',
                               form=form,
                               date_e=date_e,
                               time_l=time_l,
                               master_e=master_e)
    return render_template('registration.html',
                           prices=prices,
                           form_for_servis=form_for_servis,
                           date_e=date_e,
                           time_l=time_l,
                           master_e=master_e)


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = TypeservisForm(request.form)
    prices = Price.query.all()
    if request.method == 'POST':
        typeservis = Typeservis()
        typeservis.set(form.type_s_1.data,
                       form.type_s_2.data,
                       form.type_s_3.data,
                       form.type_s_4.data,
                       form.type_s_5.data)
        print typeservis
        list_servis = []
        if typeservis.type_s_1 != '':
            list_servis.append(str(typeservis.type_s_1))
        if typeservis.type_s_2 != '':
            list_servis.append(str(typeservis.type_s_2))
        if typeservis.type_s_3 != '':
            list_servis.append(str(typeservis.type_s_3))
        if typeservis.type_s_4 != '':
            list_servis.append(str(typeservis.type_s_4))
        if typeservis.type_s_5 != '':
            list_servis.append(str(typeservis.type_s_5))
        return list_servis
    print 2
    return render_template('registration.html', prices=prices, form=form)


@app.route('/user/<user_id>/delete', methods=['GET'])
def user_del(user_id):
    user = User.get_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect('/user')
    return render_template('error.html', msg_eror="not id {}".format(user_id))

@app.route('/calendar/', methods=['GET', 'POST'])
def calendar():
    users = User.query.all()
    return render_template('calendar.html', users=users)


def service_time(a, b):
    service_all_time=[]
    first_time = str(a)
    for i in b:
        service_time = []
        price = get_by_price_id(i)
        time_fini = time_setvic(first_time, price.servis_duration)
        while first_time != time_fini:
            if first_time != time_fini:
                service_time.append(first_time)
                first_time = time_all_sec(time_int(first_time) + time_int("0:15"))
        service_all_time.append(service_time)
    return service_all_time

def list_rese(a):
    list_res=[]
    for i in a:
        for x in i:
            list_res.append(x)
    print list_res
    return list_res


@app.route('/cal/', methods=['POST', 'GET'])
def cal():
    form = DateForm(request.form)
    date_e = form.date_cal.data
    master_e = form.master.data
    users_all = User.query.all()
    users = []
    list_rer = []
    masters = Master.query.all()
    prices = Price.query.all()
    user_time = []
    time_list = ["00:00", "00:15", "00:30", "00:45",
                 "01:00", "01:15", "01:30", "01:45",
                 "02:00", "02:15", "02:30", "02:45",
                 "03:00", "03:15", "03:30", "03:45",
                 "04:00", "04:15", "04:30", "04:45",
                 "05:00", "05:15", "05:30", "05:45",
                 "06:00", "06:15", "06:30", "06:45",
                 "07:00", "07:15", "07:30", "07:45",
                 "08:00", "08:15", "08:30", "08:45",
                 "09:00", "09:15", "09:30", "09:45",
                 "10:00", "10:15", "10:30", "10:45",
                 "11:00", "11:15", "11:30", "11:45",
                 "12:00", "12:15", "12:30", "12:45",
                 "13:00", "13:15", "13:30", "13:45",
                 "14:00", "14:15", "14:30", "14:45",
                 "15:00", "15:15", "15:30", "15:45",
                 "16:00", "16:15", "16:30", "16:45",
                 "17:00", "17:15", "17:30", "17:45",
                 "18:00", "18:15", "18:30", "18:45",
                 "19:00", "19:15", "19:30", "19:45",
                 "20:00", "20:15", "20:30", "20:45",
                 "21:00", "21:15", "21:30", "21:45",
                 "22:00", "22:15", "22:30", "22:45",
                 "23:00", "23:15", "23:30", "23:45"]
    time_work = ["10:00", "10:15", "10:30", "10:45",
                 "11:00", "11:15", "11:30", "11:45",
                 "12:00", "12:15", "12:30", "12:45",
                 "13:00", "13:15", "13:30", "13:45",
                 "14:00", "14:15", "14:30", "14:45",
                 "15:00", "15:15", "15:30", "15:45",
                 "16:00", "16:15", "16:30", "16:45",
                 "17:00", "17:15", "17:30", "17:45",
                 "18:00", "18:15", "18:30", "18:45",
                 "19:00", "19:15", "19:30", "19:45"]
    for user in users_all:
        if date_e == user.date and master_e == user.master:
            users.append(user)
    for user in users:
        user_time.append(str(user.time))
    for user in users:
        y = service_time(user.time, for_type_service(user.type_servis))
        for i in y:
            for x in i:
                list_rer.append(x)
    print list_rer
    return render_template('cal.html',
                           list_rer=list_rer,
                           user_time=user_time,
                           index=index,
                           for_type_service=for_type_service,
                           service_time=service_time,
                           list_time=list_time,
                           get_by_price_id=get_by_price_id,
                           time_setvic=time_setvic,
                           str=str,
                           int=int,
                           prices=prices,
                           masters=masters,
                           time_list=time_list,
                           users=users,
                           time_work=time_work,
                           date_e=date_e,
                           master_e=master_e)

@app.route('/master/master_add', methods=['POST', 'GET'])
def master_add():
    form = MasterForm(request.form)
    if request.method == 'POST':
        master = Master(master_name=form.master_name.data)
        db.session.add(master)
        db.session.commit()
        return redirect('/master/master_add')
    return render_template('master_add.html', form=form)

@app.route('/master', methods=['POST', 'GET'])
def master():
    masters = Master.query.all()
    return render_template('master.html', masters=masters)

@app.route('/master/master_add/<master_name>/delete', methods=['POST', 'GET'])
def master_delete(master_name):
    master = Master.query.get(master_name)
    prices =Price.query.all()
    if prices:
        for price in prices:
            if price.master_name == master_name:
                db.session.delete(price)
                db.session.commit()
        db.session.delete(master)
        db.session.commit()
        return redirect('/master')
    return render_template('error.html', msg_eror="not id {}".format(master))

@app.route('/master/master_add/<master_name>', methods=['POST', 'GET'])
def price_add(master_name):
    form = PriceForm(request.form)
    if request.method == 'POST':
        price = Price(master_name=master_name,
                      servis_name=form.servis_name.data,
                      servis_cost=form.servis_cost.data,
                      servis_duration=form.servis_duration.data)
        db.session.add(price)
        db.session.commit()
        return redirect('/master/master_add/<master_name>/price')
    return render_template('price_add.html', master_name=master_name, form=form)

@app.route('/master/master_add/<master_name>/price', methods=['POST', 'GET'])
def price(master_name):
    prices=Price.query.all()
    return render_template('price.html', master_name=master_name, prices=prices)

@app.route('/master/master_add/<price_id>/price/delete', methods=['POST', 'GET'])
def price_delete(price_id):
    price = Price.query.get(price_id)
    if price:
        db.session.delete(price)
        db.session.commit()
        return redirect('/master/master_add/<master_name>/price')
    return render_template('error.html', msg_eror="not id {}".format(master))

if __name__ == "__main__":
    db.create_all()
    app.run()