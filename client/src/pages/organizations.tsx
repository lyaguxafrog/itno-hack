import AddOrganization from '@/components/organizations/add-organization';
import OrganizationCard from '@/components/organizations/organization-card';

export default function Organizations() {
  return (
    <div className="h-full">
      <h1 className="text-2xl font-semibold mb-10">Ваши организации:</h1>
      <div className="flex flex-wrap gap-5">
        <OrganizationCard />
        <OrganizationCard />
        <OrganizationCard />
        <OrganizationCard />
        <AddOrganization />
      </div>
    </div>
  );
}
