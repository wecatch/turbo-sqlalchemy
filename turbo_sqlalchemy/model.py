# -*- coding: utf-8 -*-

from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import UnmappedClassError


class BaseQuery(orm.Query):
    pass


class Model(object):
    query_class = None
    query = None


class _QueryProperty(object):
    def __init__(self, sa):
        self.sa = sa

    def __get__(self, obj, owner):
        try:
            mapper = orm.class_mapper(owner)
            if mapper:
                return owner.query_class(mapper, session=self.sa.session())
        except UnmappedClassError:
            return None


class Db(object):

    def __init__(self, engine, query_class=BaseQuery, model_class=Model):
        self.Query = query_class
        self.Model = self.make_declarative_base(model_class=model_class)
        self.session = self.create_session()

    def create_session(self, engine):
        return orm.sessionmaker(bind=engine)

    def make_declarative_base(self, model_class):
        base = declarative_base(cls=model_class)
        if not getattr(base, 'query_class', None):
            base.query_class = self.Query

        base.query = _QueryProperty(self)
        return base
