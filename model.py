from pydantic import BaseModel

class Todo(BaseModel): # 예외처리용 post 포멧
    id: int
    item: str