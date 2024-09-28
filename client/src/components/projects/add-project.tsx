import { PlusIcon } from '../icons';
import { Button } from '../ui/button';
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '../ui/dialog';
import { Input } from '../ui/input';
import { Label } from '../ui/label';

export default function AddProject() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <div className="rounded-md border-[2px] border-gray-200 flex w-72 h-60 justify-center items-center cursor-pointer hover:border-gray-300 transition-colors">
          <PlusIcon />
        </div>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Создание проекта</DialogTitle>
          <DialogDescription>Введите название нового проекта, чтобы добавить его в список.</DialogDescription>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="flex flex-col gap-2">
            <Label htmlFor="name">Название проекта</Label>
            <Input placeholder="Введите название проекта" />
          </div>
        </div>
        <DialogFooter>
          <DialogClose className="flex w-full justify-between">
            <Button type="button" variant="secondary">
              Close
            </Button>
            <Button type="submit">Создать проект</Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
