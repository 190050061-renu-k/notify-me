import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CourseInfoComponent } from './course-info/course-info.component';
import { DashboardComponent } from './dashboard/dashboard.component'
import { LoginComponent } from './login/login.component';
import { CreateCourseComponent } from './create-course/create-course.component';
import { DeadlinesComponent } from './deadlines/deadlines.component';
import { AuthGuard } from './auth.guard';
import { Auth1Guard } from './auth1.guard';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard' , pathMatch: 'full'},
  { path: 'dashboard', component: DashboardComponent, canActivate:[AuthGuard]},
  { path: 'detail/:code', component: CourseInfoComponent },
  { path: 'login', component: LoginComponent, canActivate:[Auth1Guard]},
  { path: 'createcourse', component: CreateCourseComponent, canActivate:[AuthGuard]},
  { path: 'createdeadline/:code', component:DeadlinesComponent, canActivate:[AuthGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
      