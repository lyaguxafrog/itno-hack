import { useRef } from 'react';
import { useDrag, useDrop } from 'react-dnd';

interface IDndItem {
  id: number;
  index: number;
  type: string;
}

export const useDnd = ({
  id,
  index,
  isDnd,
  moveItem,
}: {
  isDnd: boolean;
  id: number;
  index: number;
  moveItem: (dragId: number, hoverId: number) => void;
}) => {
  const ref = useRef<HTMLDivElement>(null);

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const [{ handlerId }, drop] = useDrop<IDndItem, any, any>({
    accept: 'task',
    collect(monitor) {
      return {
        handlerId: monitor.getHandlerId(),
      };
    },
    hover(item, monitor) {
      if (!ref.current) {
        return;
      }
      const dragIndex = item.index;
      const hoverIndex = index;

      if (dragIndex === hoverIndex) {
        return;
      }

      const hoverBoundingRect = ref.current?.getBoundingClientRect();
      const hoverMiddleY = (hoverBoundingRect.bottom - hoverBoundingRect.top) / 2;
      const clientOffset = monitor.getClientOffset() || { x: 0, y: 0 };
      const hoverClientY = clientOffset.y - hoverBoundingRect.top;

      if (dragIndex < hoverIndex && hoverClientY < hoverMiddleY) {
        return;
      }

      if (dragIndex > hoverIndex && hoverClientY > hoverMiddleY) {
        return;
      }

      moveItem(+item.id, id);

      // без этой строки происходят баги
      // eslint-disable-next-line no-param-reassign
      item.index = hoverIndex;
    },
  });

  const [{ isDragging }, drag] = useDrag({
    type: 'task',
    item: { id, index },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
  });

  drag(drop(ref));

  if (!isDnd) {
    return { ref: null, isDragging: false, handlerId: null };
  }

  return { ref, isDragging, handlerId };
};
