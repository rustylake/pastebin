from flask import *
from flask_sqlalchemy import *
import db_config

app = Flask(__name__)
app.config.from_object(db_config)
db = SQLAlchemy(app)


class User(db.Model):
    # primary_key=True是主键db.Column是字段名， db.INT是数据类型
    __tablename__ = 'User'
    # id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), primary_key=True)
    url = db.Column(db.String(45), unique=True)
    code = db.Column(db.String(300), unique=False)

    def __init__(self, title, url, code):
        self.title = title
        self.code = code
        self.url = url

    def __repr__(self):
        return '<User %r>' % self.usernam


@app.route('/', methods=['get', 'post'])
def Hello():
    return render_template('Hello.html')


@app.route('/Code/', methods=['POST'])
def Code():
    title = request.form.get("title")
    code = request.form.get('code')
    url = '//return/' + title
    # if title is None:
    #     return '错误输入', 404
    # elif User.query.get_or_404(title) != 404:
    #     return "You are late", 404
    # else:
    a = User(title=title, code=code, url=url)
    db.session.add(a)
    db.session.commit()
    return render_template('ok.html')


@app.route('/ok/')
def ok():
    return render_template('ok.html')


@app.route('/return/<title>/', methods=['Post'])
def view_code(title):
    data = User.query.get(title)
    return render_template('return.html'), data


if __name__ == '__main__':
    app.run(debug=True)
