import streamlit as st

# Define your pages here
def createPage(page, title=None, icon=None, url_path=None, default=False):

    try:

        return st.Page(page=page, title=title, icon=icon, url_path=url_path, default=default)

    except Exception as e:

        er = e
        def error():
            st.title("Error")

            st.write(f"error.\_\_cause\_\_: {er.__cause__}")
            st.write(f"error.\_\_context\_\_: {er.__context__}")
            st.write(f"error.\_\_suppress_context\_\_: {er.__suppress_context__}")
            st.write(er.__traceback__)
            st.write("Message:")
            st.write(er)

        return st.Page(error, title=f"Error ({page})", icon=":material/error:", url_path=f"error-{url_path}")


home = createPage(page="View/Home.py", title="Home", icon=":material/home:", url_path="home")
singup = createPage(page="View/SignUp.py", title="Sign Up", icon=":material/account_circle:", url_path="singup")
database = createPage(page="View/Database.py", title="Database", icon=":material/account_circle:", url_path="database")

# Define logic here

pages = [home, database]
position = "sidebar"

if not ("userId" in st.session_state):

    pages = [home, singup]
    # position = "hidden"

# Define your routes here
pg = st.navigation(pages=pages, position=position)

pg.run()
