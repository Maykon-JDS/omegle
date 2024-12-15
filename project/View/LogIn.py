import streamlit as st
from Controller.UserController import UserController

st.session_state.respose = {} if ("respose" not in st.session_state) else st.session_state.respose

if ("respose" in st.session_state and st.session_state.respose != None and (not st.session_state.respose) != True):

    if st.session_state.respose["status"] == "ok":

        st.success(st.session_state.respose["messages"])

    elif st.session_state.respose["status"] == "error":

        if "messages" in st.session_state.respose:

            if (type(st.session_state.respose.get('messages'))) is dict:

                for message in st.session_state.respose.get('messages').values():

                    st.error(message, icon=":material/error:")

            else:

                st.error(st.session_state.respose.get('messages'), icon=":material/error:")


    st.session_state.respose = {}


st.title("Sign Up")

with st.form("login_form"):

    username = st.text_input("Username", value=None, key="username")

    password = st.text_input("Password", value=None, key="password", type="password")

    # TODO: Create Login Function
    st.session_state.login_formSubmitter = st.form_submit_button("Login", on_click=UserController.signUp)


print(f"View: {st.session_state}")