import { IconSvgProps } from '@/types';

export const PlusIcon = (props: IconSvgProps) => (
  <svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill="none" {...props}>
    <path fill="#D9D9D9" d="M26 16H16v10a2 2 0 0 1-4 0V16H2a2 2 0 1 1 0-4h10V2a2 2 0 1 1 4 0v10h10a2 2 0 0 1 0 4Z" />
  </svg>
);
