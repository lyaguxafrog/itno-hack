import AddOrganization from '@/components/organizations/add-organization';
import OrganizationCard from '@/components/organizations/organization-card';
import { iOrg } from '@/types';

export default function Organizations() {
  const organizations = [] as iOrg[];

  return (
    <div className="h-full">
      <h1 className="text-2xl font-semibold mb-10">Ваши организации:</h1>
      <div className="flex flex-wrap gap-5">
        {organizations.map((organization) => (
          <OrganizationCard {...organization} />
        ))}
        <AddOrganization />
      </div>
    </div>
  );
}
