import { routes } from '@/helpers/consts';
import Login from '@/pages/login';
import Organizations from '@/pages/organizations';
import { Project } from '@/pages/project';
import Projects from '@/pages/projects';
import Register from '@/pages/register';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { Route, Routes } from 'react-router-dom';
import { Layout } from './layout';
import { CombinedProviders } from './providers';
import { PrivateRoute } from './private-route';

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
          path={routes.project}
          element={
            <Layout>
              <PrivateRoute>
                <DndProvider backend={HTML5Backend}>
                  <Project />
                </DndProvider>
              </PrivateRoute>
            </Layout>
          }
        />
        <Route
          path={routes.projects}
          element={
            <Layout>
              <PrivateRoute>
                <Projects />
              </PrivateRoute>
            </Layout>
          }
        />
        <Route
          path={routes.home}
          element={
            <Layout>
              <PrivateRoute>
                <Organizations />
              </PrivateRoute>
            </Layout>
          }
        />

        <Route path={routes.login} element={<Login />} />
        <Route path={routes.register} element={<Register />} />

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
