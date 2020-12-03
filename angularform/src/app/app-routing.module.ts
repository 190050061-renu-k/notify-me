import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CourseInfoComponent } from './course-info/course-info.component';
import { DashboardComponent } from './dashboard/dashboard.component'
import { LoginComponent } from './login/login.component';
import { AuthGuardService as AuthGuard } from './auth-guard.service';
import { AuthGuard1Service as AuthGuard1 } from './auth-guard1.service';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard' , pathMatch: 'full'},
  { path: 'dashboard', component: DashboardComponent, canActivate:[AuthGuard]},
  { path: 'detail/:coursecode', component: CourseInfoComponent },
  { path: 'login', component: LoginComponent, canActivate:[AuthGuard1]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
      