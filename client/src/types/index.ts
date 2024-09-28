import { SVGProps } from 'react';

export interface ITask {
  id: number;
  title: string;
  columnId: number;
}

export type IconSvgProps = SVGProps<SVGSVGElement> & {
  size?: number;
};
