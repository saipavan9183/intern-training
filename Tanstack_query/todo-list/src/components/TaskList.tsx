import { useQuery } from "@tanstack/react-query";
import { getTasks } from "../api/tasks";

export default function TaskList() {
  const {
    data: tasks,
    isLoading,
    isError,
  } = useQuery({
    queryKey: ["tasks"],
    queryFn: getTasks,
  });

  if (isLoading) return <p className="loading">Loading...</p>;

  if (isError) return <p className="error">Something went wrong.</p>;

  return (
    <div className="task-list">
      <h2>Tasks</h2>

      {tasks?.map((task) => (
        <div
          key={task.id}
          className="task-item"
        >
          <p>{task.title}</p>

          <span
            className={
              task.completed ? "status completed" : "status pending"
            }
          >
            {task.completed ? "Completed" : "Pending"}
          </span>
        </div>
      ))}
    </div>
  );
}