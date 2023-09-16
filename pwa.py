import streamlit as st
import functions
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass

todos = functions.get_todos()


def addTodo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def removeTodo():
    print(st.session_state)
    for selectedItem in st.session_state:
        if st.session_state[selectedItem]:
            todos.remove(selectedItem)
            functions.write_todos(todos)
            del st.session_state[selectedItem]


st.title('Todo Task application')
st.subheader('This is my Todo App.')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    todo = st.checkbox(todo, key=todo, on_change=removeTodo)


st.text_input(label="Add", label_visibility='hidden',
              placeholder="Add todo...", key="new_todo", on_change=addTodo)


st.session_state
