import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CourseInfoComponent } from './course-info/course-info.component';
import { DashboardComponent } from './dashboard/dashboard.component'
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: '', redirectTo: '/login' , pathMatch: 'full'},
  { path: 'dashboard', component: DashboardComponent},
  { path: 'detail/:coursecode', component: CourseInfoComponent },
  { path: 'login', component: LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
      