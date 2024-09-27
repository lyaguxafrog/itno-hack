import { ITask } from '@/types';
import { useDrag } from 'react-dnd';

interface ItaskData {
  data: ITask;
}
interface DropResult {
  name: string;
}
const ItemTypes = {
  BOX: 'box',
};

export const Task = ({ data }: ItaskData) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: ItemTypes.BOX,
    item: { name },
    end: (item, monitor) => {
      const dropResult = monitor.getDropResult<DropResult>();
      if (item && dropResult) {
        alert(`You dropped ${item.name} into ${dropResult.name}!`);
      }
    },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
      handlerId: monitor.getHandlerId(),
    }),
  }));

  return (
    <div ref={drag} draggable="true" data-id={data.id}>
      {data.title}
    </div>
  );
};
