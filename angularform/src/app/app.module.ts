import { BrowserModule } from '@angular/platform-browser';
import { NgModule} from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CourseInfoComponent } from './course-info/course-info.component';
import { HeaderComponent } from './header/header.component';
import { LoginComponent } from './login/login.component';
import { TokenInterceptor } from './http.interceptor';
import { DatePipe } from '@angular/common';


import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatNativeDateModule} from '@angular/material/core';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { CreateCourseComponent } from './create-course/create-course.component';
import { DeadlinesComponent } from './deadlines/deadlines.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    CourseInfoComponent,
    HeaderComponent,
    LoginComponent,
    CreateCourseComponent,
    DeadlinesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatToolbarModule,
    BrowserAnimationsModule,
    MatButtonModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatTableModule,
    MatDatepickerModule,
    MatNativeDateModule
  ],
  providers: [{
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true},
      DatePipe
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
