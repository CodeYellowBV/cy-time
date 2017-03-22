from app import db
from dateutil import parser, tz

# from datetime import datetime
# from sqlalchemy.dialects.postgresql import JSON


def get_iso8601(ts):
    return ts.strftime('%Y-%m-%dT%H:%M:%S%z+0000')


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    started_at = db.Column(db.DateTime)
    ended_at = db.Column(db.DateTime)
    description = db.Column(db.Text())

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('Project',
        backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, data):
        self.parse(data)

    def parse(self, data):
        cols = self.__table__.columns
        col_names = {col.name for col in cols}

        for key in data:
            if key in col_names:
                # TODO, clean this mess up, loop other way around,
                # loop through cols and check of data key exists
                col = list(filter(lambda c: c.name == key, cols))[0]

                if str(col.type) == 'DATETIME':
                    data[key] = parser.parse(data[key])

                setattr(self, key, data[key])

    def __repr__(self):
        return '<Entry %r>' % self.id

    def dump(self):
        data = {}
        for col in self.__table__.columns:
            key = col.name
            val = getattr(self, key)

            if str(col.type) == 'DATETIME':
                # Make aware and format as iso
                val = val.replace(tzinfo=tz.tzlocal()).isoformat()

            data[key] = val
        return data

    @staticmethod
    def find_all(session):
        return (
            session.query(Entry)
            .order_by(Entry.started_at.desc())
            .all()
        )

    @staticmethod
    def transform(model):
        print('Entry transform')
        return {
            'id': model.id,
            'started_at': get_iso8601(model.started_at) if model.ended_at is not None else '',
            'ended_at': get_iso8601(model.ended_at) if model.ended_at is not None else '',
            'description': model.description,
            'project': Project.transform(model.project) if model.project else None,
        }

    @staticmethod
    def get_collection(session):
        collection = Entry.find_all(session)
        output = []
        for model in collection:
            output.append(Entry.transform(model))
        return output


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Project %r>' % self.name

    @staticmethod
    def transform(model):
        return {
            'id': model.id,
            'name': model.name,
            'description': model.description,
        }

    @staticmethod
    def find_all(session):
        return (
            session.query(Project)
            .all()
        )

    # copypasta
    @staticmethod
    def get_collection(session):
        collection = Project.find_all(session)
        output = []
        for model in collection:
            output.append(Project.transform(model))
        return output
