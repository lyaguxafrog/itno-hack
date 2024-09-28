import { AppDispatchType, StateType } from '@/helpers/hooks';
import {
  ITasksResponse,
  registerUserInput,
  registerUserOutput,
  signInInput,
  signInOutput,
  signOutOutput,
} from '@/types/api';
import { ApolloClient, ApolloError, gql, InMemoryCache } from '@apollo/client';
import { createAsyncThunk } from '@reduxjs/toolkit';

type ThunkConfig = {
  dispatch: AppDispatchType;
  state: StateType;
};

export const endpoint = new ApolloClient({
  cache: new InMemoryCache(),
  uri: 'https://it-innohack.makridenko.ru/api/',
});

export const getTasks = createAsyncThunk<ITasksResponse, void, ThunkConfig>(
  'GET_TASKS',
  async (_, { rejectWithValue }) => {
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
  },
);

export const registerUser = createAsyncThunk<
  registerUserOutput,
  {
    registerUserInput: registerUserInput;
  },
  ThunkConfig
>('REGISTER_USER', async ({ registerUserInput }, { rejectWithValue }) => {
  try {
    const result = await endpoint.mutate({
      mutation: gql`
        mutation RegisterUser {
          registerUser(input: {
            username: "${registerUserInput.username}",
            email: "${registerUserInput.email}",
            password: "${registerUserInput.password}",
            repeatPassword: "${registerUserInput.repeatPassword}",
          }) {
            user {
              id
              email
              username
              dateJoined
            }  
          }
        }
      `,
      variables: registerUserInput,
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

export const signIn = createAsyncThunk<
  signInOutput,
  {
    signInInput: signInInput;
  },
  ThunkConfig
>('SIGN_IN', async ({ signInInput }, { rejectWithValue }) => {
  try {
    const result = await endpoint.mutate({
      mutation: gql`
        mutation SignIn {
          signIn(
            username: "${signInInput.username}",
            password: "${signInInput.password}"
          ){
            payload  
          }
        }
      `,
      variables: signInInput,
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

export const signOut = createAsyncThunk<signOutOutput, void, ThunkConfig>(
  'SIGN_OUT',
  async (_, { rejectWithValue }) => {
    try {
      const result = await endpoint.mutate({
        mutation: gql`
          mutation SignOut {
            signOut {
              deleted
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
  },
);
