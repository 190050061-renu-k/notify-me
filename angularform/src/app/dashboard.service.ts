import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor(private http: HttpClient, private cookie:CookieService){}
  private httpOptions;
  list() {
  	this.httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + this.cookie.get("JWT")
      })
	};
  return this.http.get('http://127.0.0.1:8000/dashboardapi/courses', this.httpOptions);
  }
}