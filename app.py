import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase

st.set_page_config(page_title="Langchain:chat with sql database")
st.title("Chat with your SQL Database")

Localdb="USE_LOCALDB"
MYSQL="USE_MYSQL"

radio_opt=["Use SQLlite 3 database- student.db","connect to your sql database"]
selected_opt=st.sidebar.radio(label="choose the db you want to chat with",options=radio_opt)
if radio_opt.index(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Enter the host name of your sql database")
    mysql_user=st.sidebar.text_input("Enter the user name of your sql database")
    mysql_password=st.sidebar.text_input("Enter the password of your sql database",type="password")
    mysql_db=st.sidebar.text_input("Enter the database name of your sql database")
else:
    db_uri=Localdb

api_key=st.sidebar.text_input("Enter your groq api key",type="password")
if not api_key:
    st.warning("Please enter your groq api key to proceed further")
    st.stop()
if not db_uri:
    st.warning("Please select the database you want to connect to")
    st.stop()

llm=ChatGroq(groq_api_key=api_key,model_name="meta-llama/llama-4-scout-17b-16e-instruct",streaming=True)

@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri==Localdb:
        dffilepath=(Path(__file__).parent/"student.db")
        print(dffilepath)
        creator=lambda: sqlite3.connect(f"file:{dffilepath}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite://",creator=creator))
    else:
        if not mysql_host or not mysql_user or not mysql_password or not mysql_db:
            st.warning("Please enter all the details of your sql database to proceed further")
            st.stop()
        else:
            return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))


if db_uri==MYSQL:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)

toolkit=SQLDatabaseToolkit(db=db,llm=llm)
agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True
)
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"]=[{"role":"assistant","content":"How can I help you?"}] 

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.messages.append({"role":"user","content":user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)