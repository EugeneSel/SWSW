from DAOClasses import NaturalDisasters, Tags
from session_utils import get_moderator_session

session = get_moderator_session()
# or:
# from DAOManager import DAOManager
# dao_mgr = DAOManager()
# and use everywhere dao_mgr.Session()

# print tags of every natural disaster ordered by its id
for instance in session.query(NaturalDisasters).order_by(NaturalDisasters.id):
    for tag in instance.tags: print(tag.tag)

# print all tags from tags table
for instance in session.query(Tags).order_by(Tags.tag):
    print(instance.tag)

# for every natural disaster ordered by id: print connected news source and
# count of posts about this disaster from source
for instance in session.query(NaturalDisasters).order_by(NaturalDisasters.id):
    for piece_of_news in instance.news: print(piece_of_news.news_source_name, piece_of_news.count)
