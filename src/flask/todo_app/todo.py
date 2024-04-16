from dataclasses import dataclass
from typing import Self

@dataclass
class Task:

    title: str = ""
    desc: str = ""
    done: bool = False

    def to_dict(self) -> dict[str, str, bool]:
        return {
                "title": self.title, 
                "description": self.desc, 
                "done": self.done
            }


class Todo:

    task_list: list[Task] = []

    @classmethod
    def get(cls, i: int) -> Task:
        if isinstance(i, str): i = int(i)
        return cls.task_list[i]
    
    @classmethod
    def _append(cls: Self, task: Task) -> None:
        cls.task_list.append(task)
    
    @classmethod
    def create_task(cls: Self, title:str, desc: str, done: bool = False) -> None:
        cls._append(Task(title=title, desc=desc, done=done))

    @classmethod
    def all(cls) -> list[Task]:
        return cls.task_list
    
    @classmethod
    def clear(cls: Self) -> None:
        cls.task_list.clear()

    @classmethod
    def count(cls: Self) -> int:
        return len(cls.all())