```python
# 6.30
# pyechart
https://pyecharts.readthedocs.io/projects/pyecharts-en/zh/latest/en-us/charts_base/#geo

https://github.com/kimdong799/MJU_STOCK_REALESTATE_ANALYTICS/blob/main/pyechart_%EB%9D%BC%EB%96%BC%EB%8A%94%EB%A7%90%EC%9D%B4%EC%A1%B0.ipynb

# DASH
import os
import copy
import time
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from flask_caching import Cache


external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:6379')
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

N = 100

df = pd.DataFrame({
    'category': (
        (['apples'] * 5 * N) +
        (['oranges'] * 10 * N) +
        (['figs'] * 20 * N) +
        (['pineapples'] * 15 * N)
    )
})
df['x'] = np.random.randn(len(df['category']))
df['y'] = np.random.randn(len(df['category']))

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df['category'].unique()],
        value='apples'
    ),
    html.Div([
        html.Div(dcc.Graph(id='graph-1'), className="six columns"),
        html.Div(dcc.Graph(id='graph-2'), className="six columns"),
    ], className="row"),
    html.Div([
        html.Div(dcc.Graph(id='graph-3'), className="six columns"),
        html.Div(dcc.Graph(id='graph-4'), className="six columns"),
    ], className="row"),

    # signal value to trigger callbacks
    dcc.Store(id='signal')
])


# perform expensive computations in this "global store"
# these computations are cached in a globally available
# redis memory store which is available across processes
# and for all time.
@cache.memoize()
def global_store(value):
    # simulate expensive query
    print('Computing value with {}'.format(value))
    time.sleep(5)
    return df[df['category'] == value]


def generate_figure(value, figure):
    fig = copy.deepcopy(figure)
    filtered_dataframe = global_store(value)
    fig['data'][0]['x'] = filtered_dataframe['x']
    fig['data'][0]['y'] = filtered_dataframe['y']
    fig['layout'] = {'margin': {'l': 20, 'r': 10, 'b': 20, 't': 10}}
    return fig


@app.callback(Output('signal', 'data'), Input('dropdown', 'value'))
def compute_value(value):
    # compute value and send a signal when done
    global_store(value)
    return value


@app.callback(Output('graph-1', 'figure'), Input('signal', 'data'))
def update_graph_1(value):
    # generate_figure gets data from `global_store`.
    # the data in `global_store` has already been computed
    # by the `compute_value` callback and the result is stored
    # in the global redis cached
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'marker': {
                'opacity': 0.5,
                'size': 14,
                'line': {'border': 'thin darkgrey solid'}
            }
        }]
    })


@app.callback(Output('graph-2', 'figure'), Input('signal', 'data'))
def update_graph_2(value):
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'lines',
            'line': {'shape': 'spline', 'width': 0.5},
        }]
    })


@app.callback(Output('graph-3', 'figure'), Input('signal', 'data'))
def update_graph_3(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2d',
        }]
    })


@app.callback(Output('graph-4', 'figure'), Input('signal', 'data'))
def update_graph_4(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2dcontour',
        }]
    })


if __name__ == '__main__':
    app.run_server(debug=True, processes=6)

## dash2
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime
from flask_caching import Cache
import os
import pandas as pd
import time
import uuid

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    # Note that filesystem cache doesn't work on systems with ephemeral
    # filesystems like Heroku.
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',

    # should be equal to maximum number of users on the app at a single time
    # higher numbers will store more data in the filesystem / redis cache
    'CACHE_THRESHOLD': 200
})


def get_dataframe(session_id):
    @cache.memoize()
    def query_and_serialize_data(session_id):
        # expensive or user/session-unique data processing step goes here

        # simulate a user/session-unique data processing step by generating
        # data that is dependent on time
        now = datetime.datetime.now()

        # simulate an expensive data processing task by sleeping
        time.sleep(5)

        df = pd.DataFrame({
            'time': [
                str(now - datetime.timedelta(seconds=15)),
                str(now - datetime.timedelta(seconds=10)),
                str(now - datetime.timedelta(seconds=5)),
                str(now)
            ],
            'values': ['a', 'b', 'a', 'c']
        })
        return df.to_json()

    return pd.read_json(query_and_serialize_data(session_id))


def serve_layout():
    session_id = str(uuid.uuid4())

    return html.Div([
        dcc.Store(data=session_id, id='session-id'),
        html.Button('Get data', id='get-data-button'),
        html.Div(id='output-1'),
        html.Div(id='output-2')
    ])


app.layout = serve_layout


@app.callback(Output('output-1', 'children'),
              Input('get-data-button', 'n_clicks'),
              Input('session-id', 'data'))
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 1 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


@app.callback(Output('output-2', 'children'),
              Input('get-data-button', 'n_clicks'),
              Input('session-id', 'data'))
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 2 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
```
##
# 6.28
# Dash App With Multiple Outputs
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
        html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
        html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
    ]),
])


@app.callback(
    Output('square', 'children'),
    Output('cube', 'children'),
    Output('twos', 'children'),
    Output('threes', 'children'),
    Output('x^x', 'children'),
    Input('num-multi', 'value'))
def callback_a(x):
    return x**2, x**3, 2**x, 3**x, x**x


if __name__ == '__main__':
    app.run_server(debug=True)

#  Dash App With Chained Callbacks
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.RadioItems(
        id='countries-radio',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='America'
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-radio'),

    html.Hr(),

    html.Div(id='display-selected-values')
])


@app.callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )


if __name__ == '__main__':
    app.run_server(debug=True)

# Dash App With State
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id="input-1", type="text", value="Montréal"),
        dcc.Input(id="input-2", type="text", value="Canada"),
        html.Div(id="number-output"),
    ]
)


@app.callback(
    Output("number-output", "children"),
    Input("input-1", "value"),
    Input("input-2", "value"),
)
def update_output(input1, input2):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)


if __name__ == "__main__":
    app.run_server(debug=True)

##
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_design_kit as ddk

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)
````````````````````````````````````````````````````````
# Interactive Visualizations


# Dash 
## Library
import dash
import dash_design_kit as ddk
import plotly.express as px
import pandas as pd

## Theme
Mars Theme 
Neptune Theme 
Miller Theme 
Extrasolar Theme 
Design Kit Theme Editor
## Layout
app = dash.Dash(__name__)
server = app.server  # expose server variable for Procfile

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = ddk.App(show_editor=True, children=[
    ddk.Header([ddk.Title('Hello Dash')]) # 제목,
   # 플롯카드형식으로 메꿈 
    ddk.Card(children=[
        ddk.CardHeader(title='Dash: A Web application framework for Python.'),
        ddk.Graph(figure=fig) # 플롯그리기
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


## HTML Dash 그래프 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
) # 배경 및 텍스트 상자

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1( # 타이틀부분 
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
   # 그아래 
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
   # 그래프 그리기 
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

## Table 표시
import dash
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 함수화 시켜서 layout 아래 첨부하는게 더 효율적일듯!!
app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)


### 6.18
# Dash 
## Library
import dash
import dash_design_kit as ddk
import plotly.express as px
import pandas as pd

## Theme
Mars Theme 
Neptune Theme 
Miller Theme 
Extrasolar Theme 
Design Kit Theme Editor

## Layout
app = dash.Dash(__name__)
server = app.server  # expose server variable for Procfile

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = ddk.App(show_editor=True, children=[
    ddk.Header([ddk.Title('Hello Dash')]) # 제목,
   # 플롯카드형식으로 메꿈 
    ddk.Card(children=[
        ddk.CardHeader(title='Dash: A Web application framework for Python.'),
        ddk.Graph(figure=fig) # 플롯그리기
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


## HTML Dash 그래프 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
) # 배경 및 텍스트 상자

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1( # 타이틀부분 
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
   # 그아래 
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
   # 그래프 그리기 
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

## Table 표시
import dash
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 함수화 시켜서 layout 아래 첨부하는게 더 효율적일듯!!
app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)

@@
## scatter
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# callback - 반응형 프로그래밍
<- value_ID = my-input childern - my-output>

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

## 6.18
# Basic Callbacks
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"), # 타이틀
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
#Div- input output 원하는 text 설정 후 Br() 띄어쓰기?
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)

# children과 value 

if __name__ == '__main__':
    app.run_server(debug=True)

# 6.22
# dash 깃허브 사이트
https://github.com/asehmi/Data-Science-Meetup-Oxford/tree/master/GlobalCities

# pdk
## 정규화 
'''python
df_stop_1['norm_passengers'] = df_stop_1['passengers'].apply(np.log) / df_stop_1['passengers'].apply(np.log).max()

## pydeck 레이어
layer_poly = pdk.Layer(
    'PolygonLayer',
    background,
    get_polygon='coordinates',
    get_fill_color='[0, 0, 0, 50]',
    pickable=True,
    auto_highlight=True
)
layer_nodes = pdk.Layer(
    'ScatterplotLayer',
    df_stop_1,
    get_position='[lon, lat]',
    get_radius=80,
    get_fill_color='[0, 255*norm_passengers, 130]',
    pickable=True,
    auto_highlight=True
)
layer_edges = pdk.Layer(
    'LineLayer',
    df_graph1_edges,
    get_source_position='[src_pos_lon, src_pos_lat]',
    get_target_position='[dst_pos_lon, dst_pos_lat]',
    get_width='2',
    get_color='[240, 128, 128]',
    pickable=True,
    auto_highlight=True
)

r = pdk.Deck(layers=[layer_poly, layer_edges, layer_nodes],
            map_style='mapbox://styles/mapbox/outdoors-v11',
            mapbox_key = "pk.eyJ1IjoiemlnZ3VyYXQiLCJhIjoiY2ttY3hzczd5MGg3MTJwbWNnM3lhMTlxaCJ9.DS0K_9u4jtpIdR23jRXhRA",
            initial_view_state = view_state)
r.to_html()

## 텍스트만 출력 C G 7 M 
df['text'] = 'text'
layer = pdk.Layer(
    'TextLayer',
    df[:100],
    get_position='[lng, lat]',
    get_text='text',
    get_color='[0, 255, 255]',
    font_family='consolas',
    sizeScale=0.5,
    pickable=True,
    auto_highlight=True
)

center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.show()

## 텍스트 칼라
COLOUR_RANGE = [
    [29,53,87,220],
    [69,123,157,220],
    [168,218,220,220],
    [241,250,238,220],
    [239,35,60,220],
    [217,4,41,220]
]

TEXT_COLOUR = {
    'Black': [0,0,0,255],
    'Red': [189,27,33,255],
    'Green': [0,121,63,255],
    'Gold': [210,160,30,255]
}

scatterplot_layer = pdk.Layer(
    type='ScatterplotLayer',
    id='scatterplot-layer',
    data=mapdata,
    pickable=True,
    get_position=['longitude', 'latitude'],
    get_radius='normValue',
    radius_min_pixels=2*radius_scale,
    radius_max_pixels=30*radius_scale,
    get_fill_color='fill_color',
    get_line_color=[128,128,128, 200],
    get_line_width=4000,
    stroked=True,
    filled=True,
    opacity=opacity
)
text_layer = pdk.Layer(
    type='TextLayer',
    id='text-layer',
    data=mapdata,
    pickable=True,
    get_position=['longitude', 'latitude'],
    get_text='Location',
    get_color=text_colour,
    billboard=False,
    get_size=18,
    get_angle=0,
    # Note that string constants in pydeck are explicitly passed as strings
    # This distinguishes them from columns in a data set
    get_text_anchor='"middle"',
    get_alignment_baseline='"center"'
)

if layer_choice == 'Scatterplot':
    layers = [scatterplot_layer]
elif layer_choice == 'Text':
    layers = [text_layer]
else:
    layers = [scatterplot_layer, text_layer]
 
'''
