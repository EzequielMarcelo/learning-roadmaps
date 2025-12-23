import Button from "./components/Button";

function App() {
  return (
    <div>
      <Button
        color="dark"
        text="Click Me"
        onClick={() => console.log("Button Click")}
      />
    </div>
  );
}

export default App;
