import { Link } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';

export default function OrganizationCard() {
  return (
    <Link to="/projects">
      <Card className="bg-white shadow-md rounded-lg h-60 w-72 hover:-translate-y-3 transition-all cursor-pointer">
        <CardHeader>
          <CardTitle className="text-xl font-semibold text-gray-800">Название организации</CardTitle>
          <div className="h-[2px] bg-gray-300 w-full my-2" />
        </CardHeader>
        <CardContent>
          <ul className="overflow-y-auto max-h-[120px] text-gray-700">
            <li className="py-1">[Название проекта]</li>
            <li className="py-1">[Название проекта]</li>
            <li className="py-1">[Название проекта]</li>
          </ul>
        </CardContent>
      </Card>
    </Link>
  );
}
