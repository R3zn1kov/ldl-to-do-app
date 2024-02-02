import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"]
    if todo_local not in todos and todo_local:
        todos.append(todo_local + '\n')
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("Luigi DL: My Todo App")
st.subheader("Python bootcamp project: 1")
st.write("2024")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="1", label_visibility='hidden', placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
