import { useState } from "react";
import { TaskItem } from "./TaskItem";
import { TaskForm } from "./TaskForm";

/** Modelo da tarefa */
export interface Task {
  id: number;
  title: string;
  done: boolean;
}

export function TaskList() {
  const [tasks, setTasks] = useState<Task[]>([]);

  function addTask(title: string) {
    const newTask: Task = {
      id: Date.now(),
      title,
      done: false,
    };

    setTasks((prev) => [...prev, newTask]);
  }

  function toggleTask(id: number) {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id ? { ...task, done: !task.done } : task
      )
    );
  }

  function removeTask(id: number) {
    setTasks((prev) => prev.filter((task) => task.id !== id));
  }

  return (
    <>
      <TaskForm onAdd={addTask} />

      <ul className="list-group mt-3">
        {tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            onToggle={toggleTask}
            onRemove={removeTask}
          />
        ))}
      </ul>
    </>
  );
}
