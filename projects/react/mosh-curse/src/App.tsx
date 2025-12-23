import { useState } from "react";
import Alert from "./components/Alert";
import Button from "./components/Button";

function App() {
  const [isAlertVisible, setIsAlertVisible] = useState(false);

  return (
    <div>
      {isAlertVisible && <Alert>Button Click Alert</Alert>}
      <Button
        color="dark"
        text="Click Me"
        onClick={() => setIsAlertVisible(true)}
      />
    </div>
  );
}

export default App;
