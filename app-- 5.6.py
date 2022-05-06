import streamlit as st
from multipage import MultiPage
import form
import result
import global_var

st.set_page_config(page_title='Loan', page_icon=':tiger:', layout='wide')
st.title('Loan Application')

app = MultiPage()

app.add_page('Application Form', form.app)
app.add_page('Application Result', result.app)

if __name__ == '__main__':
    global_var._init()
    app.run()
