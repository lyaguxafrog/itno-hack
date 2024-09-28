export const routes = {
  profile: '/profile',
  projects: '/projects',
  organizations: '/organizations',
  project: '/project',
  login: '/',
  register: '/register',
  notFound: '/*',
} as const;

export const links = {
  //
} as const;

export const SliceNames = {
  state: 'state-slice',
  data: 'data-slice',
} as const;
