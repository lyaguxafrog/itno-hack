import { useAppDispatch } from '@/helpers/hooks';
import { updateTask } from '@/store/actions';
import { ITask } from '@/types';
import { useDrag } from 'react-dnd';

interface ItaskProps {
  data: ITask;
  index: number;
}

export const Task = ({ data, index }: ItaskProps) => {
  const dispatch = useAppDispatch();

  const [_, drag] = useDrag(() => ({
    type: 'task',
    item: () => {
      return { id: data.id, index };
    },
    end: (item, monitor) => {
      const dropResult = monitor.getDropResult<{ name: string; columnId: number }>();
      if (item && dropResult) {
        dispatch(updateTask({ task: data, columnId: dropResult.columnId }));
      }
    },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
      handlerId: monitor.getHandlerId(),
    }),
  }));

  return (
    <div ref={drag} data-id={data.id} className="w-full h-10 bg-cyan-600">
      {data.title}
    </div>
  );
};
