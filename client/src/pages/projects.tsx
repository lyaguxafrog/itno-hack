import AddProject from '@/components/projects/add-project';
import ProjectsCard from '@/components/projects/projects-card';
import { IProject } from '@/types';

export default function Projects() {
  const projects = [] as IProject[]; // TODO: redux import

  return (
    <div className="h-full">
      <h1 className="text-2xl font-medium mb-10">
        Проекты организации <span className="font-semibold">[Название организации]</span>:
      </h1>
      <div className="flex flex-wrap gap-5">
        {projects.map((project) => (
          <ProjectsCard {...project} />
        ))}
        <AddProject />
      </div>
    </div>
  );
}
