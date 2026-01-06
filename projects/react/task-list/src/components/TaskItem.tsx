import type { Task } from "./TaskList";

interface TaskItemProps {
  task: Task;
  onToggle: (id: number) => void;
  onRemove: (id: number) => void;
}

export function TaskItem({ task, onToggle, onRemove }: TaskItemProps) {
  return (
    <li className="list-group-item d-flex justify-content-between align-items-center">
      <div>
        <input
          type="checkbox"
          checked={task.done}
          onChange={() => onToggle(task.id)}
          className="me-2"
        />

        <span
          style={{
            textDecoration: task.done ? "line-through" : "none",
          }}
        >
          {task.title}
        </span>
      </div>

      <button
        className="btn btn-sm btn-danger"
        onClick={() => onRemove(task.id)}
      >
        X
      </button>
    </li>
  );
}
