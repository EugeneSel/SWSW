from DAOManager import DAOManager

dao_mgr = DAOManager()
dao_mgr.InsertNaturalDisaster(
    title='Manager test',
    description = 'Daaaamn boiii, this manager ruuules',
    confidence = 88.88,
    reply_count=12,
    favorite_count=24,
    retweet_count=3,
    tags=['Ukraine', 'To', 'Glory'],
    news = {'Reuters' : 3, 'Ukraine Today': 15}
    )
