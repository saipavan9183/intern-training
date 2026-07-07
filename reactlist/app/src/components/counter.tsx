import { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  return (
    <div style={{ marginBottom: "20px" }}>
      <h2>Counter</h2>
      <p>Count: {count}</p>

      <button onClick={() => setCount(count + 1)}>Increment</button>

      <button
        onClick={() => setCount(count - 1)}
        style={{ marginLeft: "10px" }}
      >
        Decrement
      </button>
    </div>
  );
};

export default Counter;