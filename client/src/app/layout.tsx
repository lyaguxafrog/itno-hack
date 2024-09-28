export const Layout = ({ children }: { children?: React.ReactNode }) => {
  return (
    <>
      <header className="bg-gray-200 w-full h-16">header</header>
      <div className="flex">
        <aside className="bg-gray-200 w-[10%] h-[calc(100vh-64px)]">aside</aside>
        <div className="p-3">{children}</div>
      </div>
    </>
  );
};
