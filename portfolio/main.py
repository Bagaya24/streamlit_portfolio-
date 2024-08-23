import streamlit as st


# --- PAGE SETUP --- #
about_me = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

projet_page_1 = st.Page(
    page="views/projets.py",
    title="Mes projets",
    icon=":material/bar_chart:",
)

projet_page_2 = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:",
)

# -- NAVIGATION SETUP (without sections) --- #

# pg = st.navigation(pages=[about_me, projet_page_1, projet_page_2])

# --- navigation setup (with sections) --- #

pg = st.navigation(
    {
        "Info": [about_me],
        "Mes projets": [projet_page_1, projet_page_2]
    }
)


# -- shared on all pages --- #
st.logo("assets/icons8-bouclier-100.png")
st.sidebar.text("J'aime code ❤️")
# --- run navigation --- #

pg.run()
