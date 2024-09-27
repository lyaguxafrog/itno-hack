import { store } from '@/store';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';

export type StateType = ReturnType<typeof store.getState>;
export type AppDispatchType = typeof store.dispatch;

export const useAppDispatch = () => useDispatch<AppDispatchType>();
export const useAppSelector: TypedUseSelectorHook<StateType> = useSelector;

export { useDnd } from './useDnd';
