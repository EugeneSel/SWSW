import json
from datetime import datetime, timedelta

import plotly
import plotly.graph_objs as go
from flask import Flask, render_template
from py.analytical_db.analytics_functions import *

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def index():
    news_list = get_news_list()
    for news in news_list:
        news.confidence = int(news.confidence)
        news.number_of_tags = len(news.tags)
    return render_template('index.html', news_list=news_list)


@app.route('/dashboard', methods=['GET'])
def plots():
    tags_retrospective = get_tags_retrospective()

    trace_news = go.Line(
        x=[datetime.strptime(month.created_time.strftime('%Y-%m-%d'), '%Y-%m-%d').date() for month in tags_retrospective],
        y=[month.number_of_tags for month in tags_retrospective],
        name='Used tags retrospective'
    )

    news_line = [trace_news]
    graph_json_line = json.dumps(news_line, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graph_json_line=graph_json_line)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)