import { SliceNames } from '@/helpers/consts';
import { ITask, IUser } from '@/types';
import { createSlice } from '@reduxjs/toolkit';
import { moveTask, updateTask } from './actions';
import { getTasks, registerUser, signIn, signOut } from './api-actions';

interface IDataInitialState {
  tasks: { [key: number]: ITask[] };
  user: IUser | null;
}
const dataInitialState: IDataInitialState = {
  tasks: {
    1: [
      { id: 2, title: 'title 2', status: 1 },
      { id: 1, title: 'title 1', status: 1 },
      { id: 0, title: 'something 0', status: 1 },
    ],
    2: [{ id: 3, title: 'column2', status: 2 }],
  },
  user: null,
};

export const dataSlice = createSlice({
  name: SliceNames.data,
  initialState: dataInitialState,
  reducers: {},
  extraReducers(builder) {
    builder
      .addCase(updateTask, (state, { payload }) => {
        const prevId = payload.task.status;
        const nextId = payload.columnId;
        const newTask = { ...payload.task, status: payload.columnId };
        if (prevId !== nextId) {
          state.tasks[prevId] = state.tasks[prevId].filter((task) => task.id !== payload.task.id);
          state.tasks[nextId] ? state.tasks[nextId].push(newTask) : (state.tasks[nextId] = [newTask]);
        }
      })
      .addCase(moveTask, (state, { payload }) => {
        // получим список карточек колонки
        const newCards = JSON.parse(JSON.stringify(state.tasks[payload.columnId]));

        newCards.splice(payload.dragIndex, 1);
        newCards.splice(payload.hoverIndex, 0, { ...newCards[payload.dragIndex], index: payload.hoverIndex });
        console.log(payload.hoverIndex);

        state.tasks[payload.columnId] = newCards;
      })
      .addCase(getTasks.fulfilled, (state, { payload }) => {
        const res: { [key: number]: ITask[] } = {};
        payload.allTasks.edges.forEach((edge) => res[edge.node.status].push(edge.node));
        state.tasks = res;
      })
      .addCase(registerUser.fulfilled, (state, { payload }) => {
        state.user = payload.registerUser.user;
      })
      .addCase(signIn.fulfilled, (state, { payload }) => {
        state.user = {
          id: '1',
          email: 'user@example.com',
          username: payload.signIn.payload.username,
          dateJoined: 'last',
        };
      })
      .addCase(signOut.fulfilled, (state, { payload }) => {
        state.user = null;
      });
  },
});
