import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

import { Forminfo } from './forminfo';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {

  constructor(private http: HttpClient) { }

postUrl = 'http://127.0.0.1:8000/users/';

addinfo(info: Forminfo): Observable<Forminfo> {
  return this.http.post<Forminfo>(this.postUrl, info);
}

}