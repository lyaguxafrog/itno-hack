import AddOrganization from '@/components/organizations/add-organization';
import ProjectsCard from '@/components/projects/projects-card';

export default function Projects() {
  return (
    <div className="h-full">
      <h1 className="text-2xl font-medium mb-10">
        Проекты организации <span className="font-semibold">[Название организации]</span>:
      </h1>
      <div className="flex flex-wrap gap-5">
        <ProjectsCard />
        <ProjectsCard />
        <ProjectsCard />
        <ProjectsCard />
        <AddOrganization />
      </div>
    </div>
  );
}
