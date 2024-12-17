import streamlit as st
import os
import random

# Title of the app
st.title("Trả bài lý thuyết")

# Initialize session states
if 'current_image' not in st.session_state:
    st.session_state.current_image = None
if 'solution_image' not in st.session_state:
    st.session_state.solution_image = None
if 'selected_chapters' not in st.session_state:
    st.session_state.selected_chapters = []

# Function to get available chapters dynamically
def get_available_chapters(folder):
    try:
        if os.path.exists(folder):
            # Lấy danh sách tất cả các thư mục con trong folder
            return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
        else:
            st.warning(f"Thư mục {folder} không tồn tại.")
            return []
    except Exception as e:
        st.error(f"Lỗi khi truy xuất thư mục: {e}")
        return []

# Function to get a random image without "_loigiai" from the selected chapters
def get_random_question(folder, chapters):
    images = []
    for chapter in chapters:
        chapter_folder = os.path.join(folder, chapter)
        if os.path.exists(chapter_folder):
            images += [os.path.join(chapter_folder, f) for f in os.listdir(chapter_folder)
                       if f.lower().endswith(('.png', '.jpg', '.jpeg')) and '_loigiai' not in f]
    if images:
        selected_image = random.choice(images)
        solution_image = selected_image.replace(".png", "_loigiai.png").replace(".jpg", "_loigiai.jpg").replace(".jpeg", "_loigiai.jpeg")
        return selected_image, solution_image if os.path.exists(solution_image) else None
    else:
        return None, None

# Tabs for Class 11 and Class 12
tab1, tab2 = st.tabs(["Lớp 11", "Lớp 12"])

with tab1:
    st.header("Lớp 11")
    available_chapters = get_available_chapters("data11")
    if available_chapters:
        selected_chapters = st.sidebar.multiselect(
            "Chọn các chương:", available_chapters, default=available_chapters, key="chapters11")
        st.session_state.selected_chapters = selected_chapters

        if st.button("Bấm để chọn câu hỏi", key="class11"):
            question_image, solution_image = get_random_question("data11", st.session_state.selected_chapters)
            if question_image:
                st.session_state.current_image = question_image
                st.session_state.solution_image = solution_image
            else:
                st.warning("Không tìm thấy câu hỏi nào phù hợp trong các chương đã chọn.")
    else:
        st.warning("Không có chương nào trong thư mục.")

with tab2:
    st.header("Lớp 12")
    available_chapters = get_available_chapters("data12")
    if available_chapters:
        selected_chapters = st.sidebar.multiselect(
            "Chọn các chương:", available_chapters, default=available_chapters, key="chapters12")
        st.session_state.selected_chapters = selected_chapters

        if st.button("Bấm để chọn câu hỏi", key="class12"):
            question_image, solution_image = get_random_question("data12", st.session_state.selected_chapters)
            if question_image:
                st.session_state.current_image = question_image
                st.session_state.solution_image = solution_image
            else:
                st.warning("Không tìm thấy câu hỏi nào phù hợp trong các chương đã chọn.")
    else:
        st.warning("Không có chương nào trong thư mục.")

# Display the image if one is selected
if st.session_state.current_image:
    st.image(st.session_state.current_image, caption="Câu hỏi", use_container_width=True)

    # Display solution button if solution exists
    if st.session_state.solution_image:
        if st.button("Xem lời giải"):
            st.image(st.session_state.solution_image, caption="Lời giải", use_container_width=True)
