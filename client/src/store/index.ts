import { configureStore } from '@reduxjs/toolkit';
import { rootReducer } from './root-reducer';

export const store = configureStore({
  reducer: rootReducer,
  // middleware: (getDefaultMiddleware) =>
  //   getDefaultMiddleware({
  //     thunk: {
  //       extraArgument: api,
  //     },
  //     serializableCheck: false,
  //   }),
});

export type RootState = ReturnType<typeof store.getState>;
