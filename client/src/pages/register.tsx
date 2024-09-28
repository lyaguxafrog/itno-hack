import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

export default function Register() {
  return (
    <div className="w-full h-screen flex justify-center items-center">
      <form className="border border-black rounded-md p-10 flex-col w-[25%]">
        <h1 className="text-2xl font-semibold mb-5">Регистрация</h1>

        <div className="flex flex-col gap-5">
          <Label htmlFor="email">Email</Label>
          <Input placeholder="Email" type="email" />
          <Label htmlFor="password">Password</Label>
          <Input placeholder="Password" type="password" />
          <Label htmlFor="password">Repeat Password</Label>
          <Input placeholder="Repeat password" type="password" />
          <Button>Войти</Button>
          <div className="flex items-center mt-5">
            <span className="mr-2">Есть аккаунт?</span>
            <a href="login" className="text-blue-400">
              Авторизоваться
            </a>
          </div>
        </div>
      </form>
    </div>
  );
}
