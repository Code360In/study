import streamlit as st
from pathlib import Path
import base64
from hydralit import HydraHeadApp


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


class CheatApp(HydraHeadApp):

    def run(self):
        self._cs_sidebar()
        self._cs_body()
        return None

    # sidebar
    def _cs_sidebar(self):
        st.sidebar.header('데이터정의서')

        st.sidebar.markdown('''
    <small>데이터 정의서 소개입니다..</small>
        ''', unsafe_allow_html=True)

        st.sidebar.markdown('__How to install and import__')

        st.sidebar.markdown(
            '''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://github.com/daniellewisDL/streamlit-cheat-sheet) <small>st.cheat_sheet v0.81.0 | May 2021</small>'''.format(
                img_to_bytes("./resources/L로고.jpg")), unsafe_allow_html=True)

        return None

    ##########################
    # Main body of cheat sheet
    ##########################

    def _cs_body(self):
        # Magic commands

        st.subheader(
            '데이터 정의서 ')
        st.markdown('<br><br>', unsafe_allow_html=True)

        col1, col2 = st.beta_columns(2)

        col1.subheader('Magic commands')
        col1.code('''# Magic commands implicitly `st.write()`
    \'\'\' _This_ is some __Markdown__ \'\'\'
    a=3
    'dataframe:', data
        ''')

        col2.subheader('Control flow')
        col2.code('''
    st.stop()
        ''')

        return None
