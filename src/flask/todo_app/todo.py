from dataclasses import dataclass
from typing import Self

@dataclass
class Task:

    id: int 
    title: str = ""
    desc: str = ""
    done: bool = False

    def to_dict(self) -> dict[str, str, bool]:
        return {
                "id": self.id,
                "title": self.title, 
                "description": self.desc, 
                "done": self.done
            }


class Todo:

    task_list: list[Task] = []
    curr_id: int = 0 

    @classmethod
    def get(cls, i: int) -> Task:
        if isinstance(i, str): i = int(i)
        return cls.task_list[i]
    
    @classmethod
    def add_task(cls: Self, task: Task) -> None:
        cls.task_list.append(task)
    
    @classmethod
    def create_task(cls: Self, title:str, desc: str, done: bool = False) -> None:
        cls.add_task(Task(id= cls.curr_id , title=title, desc=desc, done=done))
        cls.curr_id += 1

    @classmethod
    def delete_task_by_id(cls, id: int) -> None:
        if not isinstance(id, int): id = int(id)
        cls.task_list = [task for task in cls.all() if task.id != id]

    @classmethod
    def all(cls) -> list[Task]:
        return cls.task_list
    
    @classmethod
    def clear(cls: Self) -> None:
        cls.task_list.clear()

    @classmethod
    def count(cls: Self) -> int:
        return len(cls.all())