import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def execute_plt_code(code, df):
    try:
        plt.figure(figsize=(12, 6))
        exec(code, {'df': df, 'plt': plt})

        if plt.get_fignums():  
            return plt.gcf()  
        else:
            st.error("No figure was created.")
            return None
    except Exception as e:
        st.error(f"Error executing code: {e}")
        return None
