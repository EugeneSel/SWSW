from DAOClasses import NaturalDisasters, NewsSources, Tags, DisastersHaveNews
from session_utils import get_moderator_session
from datetime import datetime

# @class DAOManager
# @brief DAO session manager. Add all DAO utility functions here.
class DAOManager:
    def __init__(self):
        self._session = get_moderator_session()

    # @brief Inserts record in natural disasters. Params that are not mentioned in comments are obvious, if you
    #        want, please add comments for them too.
    # @param tags in, List of strings with tags
    # @param news in, Dictionary { string NewsSource : unsigned int count } - list of news sources and count of
    #        records about disaster 
    # @note In case if tag or news source does not exists - this call
    #       will create them in DB before adding natural disaster record
    def InsertNaturalDisaster(self, title, description, confidence, reply_count, favorite_count,
        retweet_count, tags, news, created_time = datetime.utcnow()):
        dao = NaturalDisasters(title=title, created_time=created_time, description=description, confidence=confidence,
            reply_count=reply_count, favorite_count=favorite_count, retweet_count=retweet_count)

        for tag in tags:
            dao_tag = self._session.query(Tags).filter_by(tag=tag).first()
            if dao_tag is None: dao_tag = Tags(tag=tag)
            dao.tags.append(dao_tag)

        for news_source, count in news.items():
            dao_news = self._session.query(NewsSources).filter_by(name=news_source).first()
            if dao_news is None: dao_news = NewsSources(name=news_source)
            dao.news.append(DisastersHaveNews(news_source=dao_news, count=count))

        self._session.add(dao)
        self._session.commit()

    def Session(self):
        return self._session

    _session = None
    