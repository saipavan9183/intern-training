import Counter from "./components/counter";
import Card from "./components/card";
import List from "./components/list";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>React Components Demo</h1>

      <Counter />

      <h2>Cards</h2>

      <Card
        title="React"
        description="A JavaScript library for building user interfaces."
      />

      <Card
        title="TypeScript"
        description="JavaScript with static typing."
      />

      <Card
        title="Vite"
        description="A fast frontend build tool."
      />

      <List />
    </div>
  );
}

export default App;