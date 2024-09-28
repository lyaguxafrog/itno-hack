import { SVGProps } from 'react';

export interface ITask {
  id: string;
  title: string;
  status: number;
  project: IProject;
}

export interface iOrg {
  id: string;
  name: string;
  createDate: string;
  owner: IUser;
  user: IUser[];
}

export interface IProject {
  id: string;
  name: string;
  createDate: string;
  owner: IUser;
  user: IUser[];
}

export interface IDetailedProject extends IProject {
  tasks: ITask[];
}

export interface IUser {
  id: string;
  username: string;
  email: string;
  dateJoined: string;
}

// toremove
export interface IBox {
  id: number;
  title: string;
  color: string;
}

export type IconSvgProps = SVGProps<SVGSVGElement> & {
  size?: number;
};
