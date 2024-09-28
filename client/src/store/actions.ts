import { ITask } from '@/types';
import { createAction } from '@reduxjs/toolkit';

export const updateTask = createAction<{task: ITask, columnId: number}>('updateTask');
export const moveTask = createAction<{dragIndex: number, hoverIndex: number, columnId: number}>('moveTask');
