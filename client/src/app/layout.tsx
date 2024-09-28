export const Layout = ({ children }: { children?: React.ReactNode }) => {
  return <>
    <header className="bg-gray-200 w-full h-16">header</header>
    <aside className="bg-gray-200 w-48 h-screen">aside</aside>
    {children}
  </>
}
