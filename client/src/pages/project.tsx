import { Box } from '@/components/kanban/box';
import { Task } from '@/components/kanban/task';

interface DropResult {
  name: string;
}
const ItemTypes = {
  BOX: 'box',
};

export const Project = () => {
  const mockSlices = [
    {
      id: 1,
      title: 'backlog',
      color: '#5a688d',
    },
    {
      id: 2,
      title: 'todo',
      color: '#9466ff',
    },
    {
      id: 3,
      title: 'in progress',
      color: '#47d3af',
    },
    {
      id: 4,
      title: 'done',
      color: '#ffb608',
    },
  ];

  const data = [
    { id: 0, title: 'something 0', columnId: 1 },
    { id: 1, title: 'title 1', columnId: 1 },
    { id: 2, title: 'title 2', columnId: 1 },
  ];

  return (
    <div className="py-3 flex w-[calc(100vw - 282px)]">
      {mockSlices.map((slice) => (
        <Box key={slice.id}>asda sdasda</Box>
      ))}
    </div>
  );
};
