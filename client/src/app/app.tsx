import { routes } from '@/helpers/consts';
import Organizations from '@/pages/organizations';
import { Project } from '@/pages/project';
import Projects from '@/pages/projects';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { Route, Routes } from 'react-router-dom';
import { CombinedProviders } from './providers';

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
        <Route
          path={routes.login}
          element={
            <DndProvider backend={HTML5Backend}>
              <Project />
            </DndProvider>
          }
        />
        <Route
          path={routes.projects}
          element={
            <DndProvider backend={HTML5Backend}>
              <Projects />
            </DndProvider>
          }
        />
        <Route
          path={routes.organizations}
          element={
            <DndProvider backend={HTML5Backend}>
              <Organizations />
            </DndProvider>
          }
        />
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
