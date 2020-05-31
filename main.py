import json
from datetime import datetime, timedelta

import plotly
import plotly.graph_objs as go
from flask import Flask, render_template

from dao.analytics_functions import *

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def index():
    news_list = [{'title': 'lalala',
                  'created_time': 'yesyes',
                  'description': 'coucou',
                  'confidence_level': 80,
                  'tags': 2,
                  'reply_count': 5,
                  'favorite_count': 5,
                  'retweet_count': 5}]
    # get_news_list()
    return render_template('index.html', news_list=news_list)


@app.route('/dashboard', methods=['GET'])
def plots():
    grouped_news_list = [[0, 1]]

    trace_news = go.Line(
        x=[news[0] for news in grouped_news_list],
        y=[news[1] for news in grouped_news_list],
        name='Used hashtags'
    )

    news_line = [trace_news]
    graph_json_line = json.dumps(news_line, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graph_json_line=graph_json_line)

if __name__ == '__main__':
    app.run(debug=True)