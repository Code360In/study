# Streamlit
## refernece
- multi page & login
- https://github.com/TangleSpace/hydralit-example

## main_page
```html
main_bg = "pg_white.png"
main_bg_ext = "png"
side_bg = "pg_white.png"
side_bg_ext = "jpg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
```
## page_widget
```python
icon = Image.open("L로고.JPG")
st.set_page_config(
    page_title="탭title",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=icon
)
```

## html_title
```html
html_header="""
<head>
<title>PControlDB</title>
<meta charset="utf-8">
<meta name="keywords" content="타이틀 제목, dashboard, management, EVA">
<meta name="description" content="타이틀 제목 dashboard">
<meta name="author" content="Larry Prato">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#008080; font-family:Georgia"> 타이틀 제목 <br>
 <h2 style="color:#008080; font-family:Georgia"> DASHBOARD</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""
```

## html_subtitle
```html
html_subtitle = """
        <h2 style="color:#008080; font-family:Georgia;"> 서브 title: </h2>
        """
        st.markdown(html_subtitle, unsafe_allow_html=True)
```

## html_line
```html
html_line="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<p style="color:Gainsboro; text-align: right;">By: mun.js@lotte.net</p>
"""
st.markdown(html_line, unsafe_allow_html=True)
```

# hydrait
- page menu
``` python
pip install -U hydralit_components
pip install jwt
!pip install compress_pickle

import hydralit as hy

app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp()
def my_home():
 hy.info('Hello from app1')

@app.addapp()
def app2():
 hy.info('Hello from app 2')


#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()
```
