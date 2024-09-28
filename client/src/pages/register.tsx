import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { routes } from '@/helpers/consts';
import { useAppDispatch } from '@/helpers/hooks';
import { registerUser } from '@/store/api-actions';
import { registerUserInput } from '@/types/api';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

export default function Register() {
  const dispatch = useAppDispatch();
  const { register, handleSubmit } = useForm<registerUserInput>();
  const navigate = useNavigate();

  const onSubmit = (data: registerUserInput) => {
    dispatch(registerUser({ registerUserInput: data })).then((reqData) => {
      if (reqData.meta.requestStatus === 'fulfilled') {
        navigate(routes.login);
      } else {
        console.log(reqData.meta.requestStatus);
      }
    });
  };
  return (
    <div className="w-full h-screen flex justify-center items-center">
      <form className="border border-black rounded-md p-10 flex-col w-[25%]">
        <h1 className="text-2xl font-semibold mb-5">Регистрация</h1>

        <div className="flex flex-col gap-5">
          <Label htmlFor="email">Email</Label>
          <Input
            placeholder="Email"
            type="email"
            {...register('email', {
              required: 'Обязательное поле',
              pattern: {
                value: /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/,
                message: 'Неверный формат email',
              },
            })}
          />
          <Label htmlFor="username">Username</Label>
          <Input placeholder="Username" {...register('username', { required: true })} />
          <Label htmlFor="password">Password</Label>
          <Input placeholder="Password" type="password" {...register('password', { required: true })} />
          <Label htmlFor="password">Repeat Password</Label>
          <Input placeholder="Repeat password" type="password" {...register('repeatPassword', { required: true })} />
          <Button onClick={handleSubmit(onSubmit)}>Войти</Button>
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
