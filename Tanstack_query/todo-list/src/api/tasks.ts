import axios from "axios";

const API = "http://127.0.0.1:8000";

export interface Task {
  id: number;
  title: string;
  completed: boolean;
}

export interface TaskCreate {
  title: string;
}

export const getTasks = async (): Promise<Task[]> => {
  const response = await axios.get(`${API}/tasks`);
  return response.data;
};

export const createTask = async (task: TaskCreate): Promise<Task> => {
  const response = await axios.post(`${API}/tasks`, task);
  return response.data;
};