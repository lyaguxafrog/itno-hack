import { useAppDispatch, useAppSelector } from '@/helpers/hooks';
import { Badge } from '';
import { useState } from 'react';

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

  const data = useAppSelector((state) => state.project.task.currentTasks);
  const dispatch = useAppDispatch();

  const modalUsersProps = useDisclosure();
  const modalTaskProps = useDisclosure();
  const modalArchiveProps = useDisclosure();

  const [pickedTask, setPickedTask] = useState<IModalTask | null>(null);

  const onDrop = (item: IDndItem, category: number) => {
    const newData = data.map((task) => {
      if (task.id === item.id) {
        return { ...task, columnId: category };
      }
      return task;
    });
    dispatch(projectActions.updateTasks(newData));
  };

  const moveItem = (dragId: number, hoverId: number) => {
    const dragIndex = data.findIndex((task) => task.id === dragId);
    const hoverIndex = data.findIndex((task) => task.id === hoverId);

    const dragCard = data[dragIndex];

    const newData = [...data];
    newData.splice(dragIndex, 1); // удалить перетаскиваемую карточку
    newData.splice(hoverIndex, 0, dragCard); // вставить перетаскиваемую карточку на новую позицию

    dispatch(projectActions.updateTasks(newData));
  };

  return (
    <div className="">
      <Header onOpenUsers={modalUsersProps.onOpen} onOpenArchive={modalArchiveProps.onOpen} />
      <Badge>Badge</Badge>
      <div py={3} spacing={3} width="calc(100vw - 282px)" maxH="93%">
        {mockSlices.map((slice) => (
          <Box bg={slice.color} borderRadius="md" paddingTop="5px" key={slice.id} minW="320px" h="100%">
            <Box bg="gray.50" p={3} borderRadius="md" h="100%">
              <Heading size="xs" mb={3}>
                {slice.title.toUpperCase()}
              </Heading>
              <DropWrapper addTaskCard={<AddTaskCard />} onDrop={onDrop} category={slice.id}>
                {data
                  .filter((task) => task.columnId === slice.id)
                  .map((task, i) => (
                    <Task
                      isDnd
                      moveItem={moveItem}
                      key={task.id}
                      index={i}
                      setPickedTask={setPickedTask}
                      {...modalTaskProps}
                      {...task}
                    />
                  ))}
              </DropWrapper>
            </Box>
          </Box>
        ))}
      </div>
    </div>
  );
};
