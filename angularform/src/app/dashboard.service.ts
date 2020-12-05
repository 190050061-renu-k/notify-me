import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor(private http: HttpClient){
  
      }
  private httpOptions;
  
  list() {
    this.httpOptions = {headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + localStorage.getItem("JWT")
    })
  };
    console.log(this.httpOptions);
    return this.http.get('http://127.0.0.1:8000/dashboardapi/courses', this.httpOptions);
  }
  create(data){
    this.httpOptions = {headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + localStorage.getItem("JWT")
    })
  };
    return this.http.post('http://127.0.0.1:8000/dashboardapi/courses', data, this.httpOptions);
  }
}