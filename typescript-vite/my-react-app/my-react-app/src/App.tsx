interface Student {
  name: string;
  age: number;
}

function getMessage(student: Student): string {
  return `Hello, ${student.name}. You are ${student.age} years old.`;
}

function App() {
  const student: Student = {
    name: "Sai Pavan",
    age: 22,
  };

  return (
    <div>
      <h1>TypeScript with React</h1>
      <p>{getMessage(student)}</p>
    </div>
  );
}

export default App;