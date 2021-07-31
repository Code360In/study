import time
from typing import Dict
import streamlit as st
from hydralit import HydraHeadApp

class LoginApp(HydraHeadApp):
    def __init__(self, title='', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self) -> None:
        st.markdown("<h1 style='text-align: center;'>Dashboard Login</h1>", unsafe_allow_html=True)
        code_expander = st.beta_expander('🔥 주의사항')
        code_expander.code(
            """
         대시보드는 상권분석을 위한 대시보드입니다.
            """
        )

        c1, c2, c3 = st.beta_columns([2, 2, 2])
        c3.image("L로고.jpg", width=100, )
        c3.image("7Logo.png", width=100, )

        form_data = self._create_login_form(c2)

        if form_data['submitted']:
            self._do_login(form_data, c2)

    def _create_login_form(self, parent_container) -> Dict:

        login_form = parent_container.form(key="login_form")

        form_state = {}
        form_state['ID'] = login_form.text_input('ID')
        form_state['Password'] = login_form.text_input('Password', type="password")
        form_state['access_level'] = login_form.selectbox('Example Access Level', (1, 2))
        form_state['submitted'] = login_form.form_submit_button('Login')

        #parent_container.write("sample login -> joe & joe")
        return form_state

    def _do_login(self, form_data, msg_container) -> None:
        # access_level=0 Access denied!
        access_level = self._check_login(form_data)

        if access_level > 0:
            msg_container.success(f"✔️ Login success")
            with st.spinner("🤓 now redirecting to application...."):
                time.sleep(1)

                self.set_access(form_data['access_level'], form_data['username'])

                self.do_redirect()
        else:
            self.session_state.allow_access = 0
            self.session_state.current_user = None

            msg_container.error(f"❌ Login unsuccessful, 😕 please check your username and password and try again.")

    def _check_login(self, login_data) -> int:
        if login_data['username'] == '123' and login_data['password'] == '123':
            return 1
        else:
            return 0
