import { Route, Routes } from 'react-router-dom';
import { CombinedProviders } from './providers';
import { routes } from '@/helpers/consts';
import { Project } from '@/pages/project';

// const LoginPage = lazy(() => import('pages/login/ui'));
// const ProjectPage = lazy(() => import('pages/project/ui'));
// const RegisterPage = lazy(() => import('pages/register/ui'));

export default function App() {
  return (
    <CombinedProviders>
      <Routes>
        {/* <Route
          path={`${routes.project}/:projectId`}
          element={
            <DndProvider backend={HTML5Backend}>
              <Project />
            </DndProvider>
          }
        /> */}
        <Route path={routes.login} element={<Project />} />
        {/* <Route path={routes.register} element={<RegisterPage />} />
        <Route path={routes.notFound} element={<NotFound />} />
        <Route
          path={routes.profile}
          element={
            <SidebarLayout>
              <ProfilePage />
            </SidebarLayout>
          }
        />*/}
      </Routes>
    </CombinedProviders>
  );
}
