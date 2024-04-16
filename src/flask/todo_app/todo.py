from dataclasses import dataclass
from typing import Self

@dataclass
class Task:

    title: str = ""
    description: str = ""
    done: bool = False


    def to_dict(self) -> dict:
        return {"title": self.title, 
                "description": self.description, 
                "done": self.done}



class Todo:

    task_list: list[Task] = []

    @classmethod
    def get(cls, i: int):
        if isinstance(i, str): i = int(i)
        return cls.task_list[i]
    
    @classmethod
    def _append(cls: Self, task: Task):
        cls.task_list.append(task)
    
    @classmethod
    def create_task(cls: Self, title:str, description: str, done: str) -> None:
        cls._append(Task(title=title, description=description, done=done))

    @classmethod
    def all(cls) -> list[Task]:
        return cls.task_list
    
    @classmethod
    def clear(cls) -> None:
        cls.task_list.clear()

    @classmethod
    def count(cls):
        return len(cls.all())