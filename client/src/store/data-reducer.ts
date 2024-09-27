import { SliceNames } from '@/helpers/consts';
import { createSlice } from '@reduxjs/toolkit';
import { updateTasks } from './actions';
import { ITask } from '@/types';

interface IDataInitialState {
  tasks: ITask[];
}
const dataInitialState: IDataInitialState = {
  tasks: [],
};

export const dataSlice = createSlice({
  name: SliceNames.data,
  initialState: dataInitialState,
  reducers: {},
  extraReducers(builder) {
    builder.addCase(updateTasks, (state, { payload }) => {
      state.tasks = payload;
    });
  },
});
