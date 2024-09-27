import { useDrag } from 'react-dnd';

interface DropResult {
  name: string;
}

const ItemTypes = {
  BOX: 'box',
};

export const Box = ({ children }: { children: React.ReactNode }) => {
  const [{ isDragging }, drop] = useDrag(() => ({
    type: ItemTypes.BOX,
    end: (item, monitor) => {
      const dropResult = monitor.getDropResult<DropResult>();
      if (item && dropResult) {
        alert(`You dropped into ${dropResult.name}!`);
      }
    },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
      handlerId: monitor.getHandlerId(),
    }),
  }));

  return (
    <div ref={drop} data-testid={`box`}>
      {children}
    </div>
  );
};
