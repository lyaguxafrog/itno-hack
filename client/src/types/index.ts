import { SVGProps } from 'react';

export interface ITask {
  id: number;
  title: string;
  status: number;
}

export interface IBox {
  id: number;
  title: string;
  color: string;
}

export interface ITasksResponse {
  allTasks: {
    edges: {
      node: ITask;
    }[];
  };
}

export type IconSvgProps = SVGProps<SVGSVGElement> & {
  size?: number;
};
