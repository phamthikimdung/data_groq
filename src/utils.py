import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def execute_plt_code(code, df):
    try:
        # Tạo một figure mới để tránh việc ghi đè
        plt.figure(figsize=(12, 6))
        # Thực thi mã vẽ biểu đồ với df và plt trong namespace
        exec(code, {'df': df, 'plt': plt})

        # Đảm bảo có ít nhất một đối tượng hình ảnh để trả về
        if plt.get_fignums():  # Kiểm tra có figure nào đã được tạo không
            return plt.gcf()  # Trả về figure hiện tại
        else:
            st.error("No figure was created.")
            return None
    except Exception as e:
        st.error(f"Error executing code: {e}")
        return None
