import { routes } from '@/helpers/consts';
import { Navigate, useLocation } from 'react-router-dom';

export const PrivateRoute = ({ children }: { children?: React.ReactNode }) => {
  const isLoggedIn = true;
  const location = useLocation();

  if (!isLoggedIn) {
    localStorage.setItem('intendedUrl', location.pathname + location.search);
    return <Navigate to={routes.login} />;
  }

  return <>{children}</>;
};
