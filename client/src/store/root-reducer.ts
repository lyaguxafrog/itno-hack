import { SliceNames } from '@/helpers/consts';
import { combineReducers } from '@reduxjs/toolkit';
import { dataSlice } from './data-reducer';

export const rootReducer = combineReducers({
  [SliceNames.data]: dataSlice.reducer,
});
