from flask import Flask
from flask import request
from flask import jsonify
import json

from sqlalchemy.sql.sqltypes import INT
from database import db, Reminder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app = app
db.create_all()

@app.route('/')
def welcome():
    return 'Welcome to Reminder Service.'

@app.route('/api/reminders', methods=['POST'])
def save_reminder():
    req_data = json.loads(request.data)
    try:
        newReminder =  Reminder(message = req_data['message'],
                                time = req_data['time'])
        db.session.add(newReminder)
        db.session.commit()
        msg = 'Reminder has been created'
    except:
        msg = 'Error! Unable to create reminder.'
    
    return msg


@app.route('/api/reminders', methods=['GET'])
def list_reminders():
    query_reminder = Reminder.query.all()
    reminder_list = []
    for r in query_reminder:
        reminders = {
            'message': r.message,
            'time': r.time
        }
        reminder_list.append(reminders)

    return jsonify(reminder_list)


@app.route('/api/reminders/<string:id>', methods = ['DELETE'])
def delete_reminder(id):
    try:
        to_delete = Reminder.query.filter_by(id = id).first()
        db.session.delete(to_delete)
        db.session.commit()
        msg = 'Reminder has been removed.'
    except:
        msg = 'Error! Unable to remove reminder.'

    return msg

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)