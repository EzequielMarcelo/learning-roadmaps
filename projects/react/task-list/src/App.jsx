import { useState } from "react";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState("");

  function addTask() {
    if (!input.trim()) return;
    setTasks([...tasks, { id: Date.now(), text: input }]);
    setInput("");
  }

  function removeTask(id) {
    setTasks(tasks.filter((t) => t.id !== id));
  }

  return (
    <>
      <h1>📝 TaskList</h1>

      <div className="card">
        <div className="input-area">
          <input
            type="text"
            value={input}
            placeholder="Adicionar tarefa..."
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && addTask()}
          />
          <button className="add-btn" onClick={addTask}>
            +
          </button>
        </div>

        <ul className="task-list">
          {tasks.map((task) => (
            <li key={task.id} className="task-item">
              <span>{task.text}</span>
              <button
                className="delete-btn"
                onClick={() => removeTask(task.id)}
              >
                ✕
              </button>
            </li>
          ))}
        </ul>
      </div>

      <p className="read-the-docs">
        React + Vite • TaskList
      </p>
    </>
  );
}

export default App;
