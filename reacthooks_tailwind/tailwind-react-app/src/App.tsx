import { useEffect, useState } from "react";

function App() {
  const [task, setTask] = useState<string>("");
  const [tasks, setTasks] = useState<string[]>([]);

  useEffect(() => {
    console.log("Component Mounted");

    const initialTasks = [
      "Learn React",
      "Learn TypeScript",
      "Practice Tailwind CSS",
    ];

    setTasks(initialTasks);
  }, []);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (task.trim() === "") return;

    setTasks([...tasks, task]);
    setTask("");
  };

  return (
    <div className="min-h-screen bg-gray-200 flex items-center justify-center px-4 py-10">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-2xl border border-gray-300 overflow-hidden">
        {/* Header */}
        <div className="bg-gray-800 px-6 py-5">
          <h1 className="text-3xl font-bold text-center text-white">
            Todo List
          </h1>
          <p className="text-center text-gray-300 mt-2">
            Stay organized, one task at a time.
          </p>
        </div>

     {/* Form */}
        <div className="p-6">
          <form onSubmit={handleSubmit} className="space-y-4">
            <input
              type="text"
              placeholder="Enter your task..."
              value={task}
              onChange={(e) => setTask(e.target.value)}
              className="w-full rounded-lg border border-gray-300 bg-gray-100 px-4 py-3 text-gray-800 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-gray-600"
            />

            <button
              type="submit"
              className="w-full rounded-lg bg-gray-800 py-3 text-white font-semibold transition hover:bg-gray-700"
            >
              Add Task
            </button>
          </form>

          {/* Task List */}
          <div className="mt-8">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-lg font-semibold text-gray-700">
                Your Tasks
              </h2>

              <span className="bg-gray-800 text-white px-3 py-1 rounded-full text-sm">
                {tasks.length}
              </span>
            </div>

            {tasks.length === 0 ? (
              <div className="bg-gray-100 rounded-lg p-6 text-center text-gray-500">
                No tasks available.
              </div>
            ) : (
              <ul className="space-y-3">
                {tasks.map((item, index) => (
                  <li
                    key={index}
                    className="flex justify-between items-center bg-gray-100 border border-gray-300 rounded-lg px-4 py-3 hover:bg-gray-200 transition"
                  >
                    <span className="text-gray-800">{item}</span>

                    <span className="bg-gray-700 text-white text-xs px-3 py-1 rounded-full">
                      #{index + 1}
                    </span>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;