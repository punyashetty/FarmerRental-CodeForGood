import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { LogoutComponent } from './logout/logout.component';
import { BookComponent } from './book/book.component';
import { PaymentComponent } from './payment/payment.component';
import { PageComponent} from './page/page.component'
import { RepositoryComponent } from './repository/repository.component';

const routes: Routes = [
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path:'logout',
    component: LogoutComponent
  },
  {
    path:'book',
    component: BookComponent
  },
  {
    path:'repository',
    component:RepositoryComponent
  },
  {
    path:'payment',
    component: PaymentComponent
  },
  {
    path:'page/:machine',
    component:PageComponent
  },
  

  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
