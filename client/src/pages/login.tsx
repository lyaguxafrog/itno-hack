import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { routes } from '@/helpers/consts';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const navigate = useNavigate();

  const loginClickHandler = () => {
    navigate(routes.home);
  };

  return (
    <div className="w-full h-screen flex justify-center items-center">
      <form className="border border-black rounded-md p-10 flex-col w-[25%]">
        <h1 className="text-2xl font-semibold mb-5">Авторизация</h1>

        <div className="flex flex-col gap-5">
          <Label htmlFor="email">Email</Label>
          <Input placeholder="Email" type="email" />
          <Label htmlFor="password">Password</Label>
          <Input placeholder="Password" type="password" />

          <Button onClick={loginClickHandler}>Войти</Button>
          <div className="flex items-center mt-5">
            <span className="mr-2">Нет аккаунта?</span>
            <a href="register" className="text-blue-400">
              Зарегистрироваться
            </a>
          </div>
        </div>
      </form>
    </div>
  );
}
