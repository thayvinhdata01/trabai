import streamlit as st
import os

# Title of the app
st.title("Kiểm tra cấu trúc thư mục")

# Function to recursively list directories and files
def list_directory_structure(startpath):
    structure = ""
    for root, dirs, files in os.walk(startpath):
        # Calculate indentation based on the depth of the directory
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        structure += f"{indent}{os.path.basename(root)}/\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            structure += f"{subindent}{f}\n"
    return structure

# Input box for directory path
base_dir = st.text_input("Nhập đường dẫn thư mục muốn kiểm tra:", value=os.getcwd())

# Button to display directory structure
if st.button("Hiển thị cấu trúc thư mục"):
    if os.path.exists(base_dir):
        st.success(f"Đang hiển thị cấu trúc thư mục: {base_dir}")
        structure = list_directory_structure(base_dir)
        st.code(structure, language='plaintext')
    else:
        st.error("Đường dẫn không tồn tại. Vui lòng kiểm tra lại.")
