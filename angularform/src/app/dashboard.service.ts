import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { DatePipe } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor(private http: HttpClient, private datePipe: DatePipe){}
  
  list() {
    return this.http.get('http://127.0.0.1:8000/dashboardapi/courses');
  }
  create(data){
    return this.http.post('http://127.0.0.1:8000/dashboardapi/courses', data);
  }

  studentlist(code){
    return this.http.get('http://127.0.0.1:8000/dashboardapi/students?code='+code);
  }
  deadlinelist(code){
    return this.http.get('http://127.0.0.1:8000/dashboardapi/deadlines?code='+code);
  }
  TAlist(code){
    return this.http.get('http://127.0.0.1:8000/dashboardapi/tas?code='+code);
  }
  deleteDeadline(data){
    return this.http.post('http://127.0.0.1:8000/dashboardapi/deleteDeadline', data);
  }
  removeStudent(data){
    return this.http.post('http://127.0.0.1:8000/dashboardapi/removeStudent', data);
  }
  createDeadline(data, code){
    data['date']=this.datePipe.transform(data['date'], "yyyy-MM-dd");
    return this.http.post('http://127.0.0.1:8000/dashboardapi/deadlines?code='+code, data);
  }
  addTA(data, code){
    data['code']=code;
    return this.http.post('http://127.0.0.1:8000/dashboardapi/addTa', data);
  }
  removeTA(data){
    return this.http.post('http://127.0.0.1:8000/dashboardapi/removeTa', data);
  }
}