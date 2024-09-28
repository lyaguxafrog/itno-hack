import { Loading } from '@/pages/loading';
import { store } from '@/store';
import React, { Suspense } from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';

export const CombinedProviders = ({ children }: { children?: React.ReactNode }) => (
  <React.StrictMode>
    <BrowserRouter>
      <Suspense fallback={<Loading />}>
        <Provider store={store}>{children}</Provider>
      </Suspense>
    </BrowserRouter>
  </React.StrictMode>
);
