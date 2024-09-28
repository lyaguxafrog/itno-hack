import { ApolloClient, ApolloError, gql, InMemoryCache } from '@apollo/client';
import { AppDispatchType, StateType } from '@/helpers/hooks';
import { createAsyncThunk } from '@reduxjs/toolkit';
import { ITasksResponse } from '@/types';

type ThunkConfig = {
  dispatch: AppDispatchType;
  state: StateType;
};

export const endpoint = new ApolloClient({
  cache: new InMemoryCache(),
  uri: 'https://it-innohack.makridenko.ru/api/',
});

export const getTasks = createAsyncThunk<ITasksResponse, void, ThunkConfig>('GET_TASKS', async (_, { rejectWithValue }) => {
  try {
    const result = await endpoint.query({
      query: gql`
        query MyQuery {
          allTasks {
            edges {
              node {
                title
                status
                id
              }
            }
          }
        }
      `,
    });
    console.log(result.data);
    return result.data;
  } catch (err) {
    if (err instanceof ApolloError) {
      return rejectWithValue({
        message: err.message,
        networkError: err.networkError,
      });
    }

    return rejectWithValue({ message: 'Unknown error occurred' });
  }
});
