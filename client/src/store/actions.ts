import { ITask } from '@/types';
import { createAction } from '@reduxjs/toolkit';

export const updateTasks = createAction<ITask[]>('updateTasks');
