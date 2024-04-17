import streamlit as st
st.graphviz_chart('''
    digraph {
        while -> condetion
        condetion -> true
        condetion -> false
        true -> while_body
        while_body -> condetion
        false -> end
    }
''')