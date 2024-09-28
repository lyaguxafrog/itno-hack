import { ITask } from '.';

export interface ITasksResponse {
  allTasks: {
    edges: {
      node: ITask;
    }[];
  };
}
