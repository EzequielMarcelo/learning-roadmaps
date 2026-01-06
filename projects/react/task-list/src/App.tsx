import { Sidebar } from "./components/Sidebar";

function App() {

  return (
    <>
      <div>
        <Sidebar start_expanded={false} title="Task List" />
      </div>
    </>
  );
}

export default App;
