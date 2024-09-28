import { useDrop } from 'react-dnd';
import { Card, CardDescription, CardHeader, CardTitle } from '../ui/card';
import { IBox, ITask } from '@/types';
import clsx from 'clsx';
import { Task } from './task';

interface IBoxProps {
  tasks: ITask[];
  data: IBox;
}
export const Box = ({ tasks, data }: IBoxProps) => {
  const [{ canDrop, isOver }, drop] = useDrop(() => ({
    accept: 'task',
    drop: () => ({ columnId: data.id }),
    collect: (monitor) => ({
      isOver: monitor.isOver(),
      canDrop: monitor.canDrop(),
    }),
  }));

  return (
    <Card ref={drop} data-testid={`box`} className={clsx(canDrop && isOver ? 'border-sky-500' : '', 'border-2')}>
      <CardHeader>
        <CardTitle>{data.title.toUpperCase()}</CardTitle>
        <CardDescription>Deploy your new project in one-click.</CardDescription>
      </CardHeader>
      {tasks.map((item, i) => (
        <Task key={item.id} data={item} index={i} />
      ))}
    </Card>
  );
};
