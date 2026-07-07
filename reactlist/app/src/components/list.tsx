const items = [
  { id: 1, name: "React", completed: true },
  { id: 2, name: "TypeScript", completed: false },
  { id: 3, name: "Vite", completed: true },
  { id: 4, name: "Hooks", completed: false },
];

const List = () => {
  return (
    <div>
      <h2>Technology List</h2>

      <ul>
        {items.map((item) => (
          <li
            key={item.id}
            style={{
              color: item.completed ? "green" : "red",
              fontWeight: item.completed ? "bold" : "normal",
            }}
          >
            {item.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default List;