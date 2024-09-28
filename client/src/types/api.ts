import { ITask, IUser } from '.';

export interface ITasksResponse {
  allTasks: {
    edges: {
      node: ITask;
    }[];
  };
}

// register user
export type registerUserInput = {
  username: string;
  email: string;
  password: string;
  repeatPassword: string;
};

export type registerUserOutput = {
  registerUser: {
    user: IUser;
  };
};

// sign in
export type signInInput = {
  username: string;
  password: string;
};

export type signInOutput = {
  signIn: {
    payload: {
      username: string;
    };
  };
};

// sign Out
export type signOutOutput = {
  signOut: {
    deleted: boolean;
  };
};
