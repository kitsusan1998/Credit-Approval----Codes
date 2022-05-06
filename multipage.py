import streamlit as st

global _global_form
_global_form = None


def set_form_value(submit_form):
    _global_form = submit_form


class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        self.pages.append({'title': title, 'function': func})

    def run(self):
        page = st.sidebar.radio('app navigation',
                                self.pages,
                                format_func=lambda page: page['title'])
        page['function']()

