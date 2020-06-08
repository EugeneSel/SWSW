from py.analytical_db.DAOClasses import *
from py.analytical_db.session_utils import get_moderator_session
from sqlalchemy import func
from sqlalchemy.sql import label

NUMBER_OF_DISASTERS_TO_OUTPUT = 20
session = get_moderator_session()


def get_news_list():
    return session.query(NaturalDisasters).order_by(NaturalDisasters.reply_count.desc(),
                                                    NaturalDisasters.favorite_count.desc(),
                                                    NaturalDisasters.retweet_count.desc()).limit(NUMBER_OF_DISASTERS_TO_OUTPUT).all()
                                                    

def get_tags_retrospective():
    return session.query(NaturalDisasters.created_time, label('number_of_tags', func.count())).join(
        natural_disasters_have_tags_table).group_by(func.day(NaturalDisasters.created_time)).all()