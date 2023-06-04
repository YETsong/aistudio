from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo) # DB 저장으로 내용 대체 필요
    return {
        "msg" : "todo added successfully"
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos" : todo_list
    }

@todo_router.get("/todo/{todo_id}") # {todo_id} 이거 url에서 받아온 파라미터 숫자가 id로 인식해서 연결해주는거임
async def get_single_todo(todo_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return { "todo" : todo}
    return {"msg" : "todo with supplied ID doesn't exist"}