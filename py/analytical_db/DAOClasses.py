from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, MEDIUMTEXT, DOUBLE, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# @brief Relational table to connect tags to NaturalDisasters.
natural_disasters_have_tags_table = Table('natural_disasters_have_tags', Base.metadata,
    Column('natural_disasters_id', INTEGER(unsigned=True), ForeignKey('natural_disasters.id')),
    Column('tag', VARCHAR(32), ForeignKey('tags.tag')))

# @class DisastersHaveNews
# @brief Represents disasters_have_news association table
class DisastersHaveNews(Base):
    __tablename__ = 'disasters_have_news'

    natural_disasters_id = Column(INTEGER(unsigned=True), ForeignKey('natural_disasters.id'), primary_key=True)
    news_source_name = Column(VARCHAR(64), ForeignKey('news_sources.name'), primary_key=True)
    count = Column(INTEGER(unsigned=True))
    disaster = relationship('NaturalDisasters', back_populates='news')
    news_source = relationship('NewsSources')

# @class NaturalDisasters
# @brief Represents records from natural_disasters table - all
#        the records about processed natural disasters 
class NaturalDisasters(Base):
    __tablename__ = 'natural_disasters'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    title = Column(VARCHAR(256))
    created_time = Column(DATETIME)
    description = Column(MEDIUMTEXT)
    confidence = Column(DOUBLE)
    reply_count = Column(INTEGER(unsigned=True))
    favorite_count = Column(INTEGER(unsigned=True))
    retweet_count = Column(INTEGER(unsigned=True))
    tags = relationship('Tags', secondary=natural_disasters_have_tags_table)
    news = relationship('DisastersHaveNews')

# @class Tags
# @brief Represents all tags that applies to processed natural disasters records.
class Tags(Base):
    __tablename__ = 'tags'

    tag = Column(VARCHAR(32), primary_key=True)

# @class NewsSources
# @brief Contains all news sources that Google API news ever returned. 
class NewsSources(Base):
    __tablename__ = 'news_sources'

    name = Column(VARCHAR(64), primary_key=True)
