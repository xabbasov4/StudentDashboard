import streamlit as st
import pandas as pd
from database import init_db, add_student, get_students, get_student
from services import calculate_grade, calculate_statistics

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Bazanı başlanğıcda hazırlayırıq
init_db()

st.title("🎓 Student Performance Dashboard")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard & Siyahı", "➕ Yeni Tələbə", "🔍 Axtarış"])

# Tab 1: Siyahı və Statistikalar
with tab1:
    st.subheader("Tələbə Statistikaları")
    raw_students = get_students()
    stats = calculate_statistics(raw_students)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", stats["total_students"])
    col2.metric("Average Score", stats["average_score"])
    col3.metric("Highest Score", stats["highest_score"])
    col4.metric("Lowest Score", stats["lowest_score"])

    st.divider()
    st.subheader("Bütün Tələbələr")
    if raw_students:
        formatted_data = [
            {
                "Name": student[1],
                "Score": student[2],
                "Grade": calculate_grade(student[2])
            }
            for student in raw_students
        ]
        df = pd.DataFrame(formatted_data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Məlumat bazasında heç bir tələbə tapılmadı.")

# Tab 2: Tələbə Əlavə Etmək
with tab2:
    st.subheader("Yeni Tələbə Əlavə Et")
    with st.form("add_student_form", clear_on_submit=True):
        student_name = st.text_input("Student Name")
        student_score = st.number_input("Score", min_value=0.0, max_value=100.0, step=1.0)
        submit_button = st.form_submit_button("Add Student")

        if submit_button:
            if student_name.strip():
                if add_student(student_name.strip(), student_score):
                    st.success(f"{student_name} uğurla əlavə edildi!")
                    st.rerun()
                else:
                    st.error("Xəta baş verdi! Tələbə əlavə oluna bilmədi.")
            else:
                st.warning("Lütfən tələbə adını daxil edin.")

# Tab 3: Axtarış
with tab3:
    st.subheader("Tələbə Axtarışı")
    search_query = st.text_input("Search Student")
    if search_query:
        search_results = get_student(search_query)
        if search_results:
            formatted_results = [
                {
                    "Name": student[1],
                    "Score": student[2],
                    "Grade": calculate_grade(student[2])
                }
                for student in search_results
            ]
            st.dataframe(pd.DataFrame(formatted_results), use_container_width=True)
        else:
            st.warning("Axtarışa uyğun tələbə tapılmadı.")