import { Box } from '@/components/kanban/box';
import { useAppSelector } from '@/helpers/hooks';
import { IBox } from '@/types';

export const Project = () => {
  const mockSlices: IBox[] = [
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

  const data = useAppSelector((state) => state['data-slice'].tasks)

  // useEffect(() => {
  //   dispatch(getTasks());
  // }, [])

  return (
    <div className="flex gap-3">
      {mockSlices.map((slice) => (
        <Box key={slice.id} data={slice} tasks={data[slice.id] ?? []}/>
      ))}
    </div>
  );
};
