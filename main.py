from flask import Flask
# noinspection PyUnresolvedReferences
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    job = Jobs()
    job.job = 'deployment of residential modules 1 and 2'
    job.team_leader = 1
    job.work_size = 15
    job.collaborators = "1, 4, 2"
    job.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()