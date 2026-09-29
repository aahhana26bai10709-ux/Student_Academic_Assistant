import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Student Academic Assistant",
    page_icon="🎓",
    layout="wide"
)

if "subjects" not in st.session_state:
    st.session_state.subjects = []

if "marks" not in st.session_state:
    st.session_state.marks = []

if "attendance" not in st.session_state:
    st.session_state.attendance = []


st.title("🎓 Student Academic Assistant")
st.subheader("Academic Performance Dashboard")

st.write(
    "Add your subject details and check your marks "
    "and attendance using the dashboard."
)

st.sidebar.header("Add Academic Record")

subject = st.sidebar.text_input("Subject Name")
mark_input = st.sidebar.text_input("Marks")
att_input = st.sidebar.text_input("Attendance (%)")


if st.sidebar.button("Add Record"):

    if subject.strip() == "":
        st.sidebar.error("Please enter a subject name.")

    elif mark_input.strip() == "":
        st.sidebar.error("Please enter marks.")

    elif att_input.strip() == "":
        st.sidebar.error("Please enter attendance.")

    else:

        try:
            mark = int(mark_input)

            if mark < 0 or mark > 100:
                st.sidebar.error("Marks should be between 0 and 100.")

            else:

                try:
                    att = int(att_input)

                    if att < 0 or att > 100:
                        st.sidebar.error(
                            "Attendance should be between 0 and 100."
                        )

                    else:
                        st.session_state.subjects.append(subject.strip())
                        st.session_state.marks.append(mark)
                        st.session_state.attendance.append(att)

                        st.sidebar.success(
                            "Academic record added!"
                        )

                except ValueError:
                    st.sidebar.error(
                        "Attendance must be a number."
                    )

        except ValueError:
            st.sidebar.error(
                "Marks must be a number."
            )

subjects = st.session_state.subjects
marks = st.session_state.marks
attendance = st.session_state.attendance


if len(subjects) == 0:

    st.info(
        "No records have been added yet. "
        "Use the sidebar to add a subject."
    )

else:

    df = pd.DataFrame({
        "Subject": subjects,
        "Marks": marks,
        "Attendance": attendance
    })

    total_marks = 0

    for value in marks:
        total_marks += value

    average_marks = total_marks / len(marks)

    highest_marks = marks[0]

    for value in marks:
        if value > highest_marks:
            highest_marks = value

    lowest_marks = marks[0]

    for value in marks:
        if value < lowest_marks:
            lowest_marks = value

    average_attendance = sum(attendance) / len(attendance)


    st.markdown("### 📊 Academic Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Subjects", len(subjects))

    with col2:
        st.metric(
            "📈 Average Marks",
            round(average_marks, 2)
        )

    with col3:
        st.metric(
            "🏆 Highest Marks",
            highest_marks
        )

    with col4:
        st.metric(
            "📅 Average Attendance",
            str(round(average_attendance, 2)) + "%"
        )


    st.divider()

    st.markdown("### 📈 Marks by Subject")

    marks_graph = px.bar(
        df,
        x="Subject",
        y="Marks",
        text="Marks",
        title="Marks in Each Subject"
    )

    marks_graph.update_traces(
        textposition="outside"
    )

    marks_graph.update_layout(
        yaxis_title="Marks",
        xaxis_title="Subject",
        yaxis_range=[0, 100]
    )

    st.plotly_chart(
        marks_graph,
        use_container_width=True
    )

    st.markdown("### 📅 Attendance by Subject")

    attendance_graph = px.bar(
        df,
        x="Subject",
        y="Attendance",
        text="Attendance",
        title="Attendance in Each Subject"
    )

    attendance_graph.update_traces(
        texttemplate="%{text}%",
        textposition="outside"
    )

    attendance_graph.update_layout(
        yaxis_title="Attendance (%)",
        xaxis_title="Subject",
        yaxis_range=[0, 100]
    )

    st.plotly_chart(
        attendance_graph,
        use_container_width=True
    )


    # Show all records
    st.markdown("### 📋 Academic Records")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    # Performance messages
    st.markdown("### 📝 Performance")

    if average_marks >= 75:
        st.success(
            "Your average marks are 75 or above."
        )

    elif average_marks >= 50:
        st.info(
            "Your average marks are between 50 and 75."
        )

    else:
        st.warning(
            "Your average marks are below 50."
        )


    if average_attendance >= 75:
        st.success(
            "Your average attendance is 75% or above."
        )

    else:
        st.warning(
            "Your average attendance is below 75%."
        )