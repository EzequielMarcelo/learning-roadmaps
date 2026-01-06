import { Sidebar } from "./components/Sidebar";
import { Tasks } from "./pages/Tasks";

function App() {
  return (
    <div className="app-layout d-flex">
      <Sidebar start_expanded={false} title="Task List" />

      <main className="content flex-grow-1 p-4">
        <Tasks />
      </main>
    </div>
  );
}

export default App;
