import { IProject } from '@/types';
import { Avatar, AvatarFallback, AvatarImage } from '../ui/avatar';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '../ui/card';

export default function ProjectsCard({ name, user }: IProject) {
  return (
    <Card className="bg-white shadow-md rounded-lg h-60 w-72 hover:-translate-y-3 transition-all cursor-pointer">
      <CardHeader>
        <CardTitle className="text-xl font-semibold text-gray-800">{name}</CardTitle>
      </CardHeader>
      <CardContent>
        <CardDescription className="mb-2">[Название группы]</CardDescription>
        <div className="flex gap-1">
          {user.map((item) => (
            <Avatar>
              <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
              <AvatarFallback>CN</AvatarFallback>
            </Avatar>
          ))}
        </div>
      </CardContent>
      <CardFooter>
        <h1>Текущая цель: [Цель]</h1>
      </CardFooter>
    </Card>
  );
}
