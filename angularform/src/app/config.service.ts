import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

import { Forminfo } from './forminfo';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {

	private httpOptions: any;
	public errors: any = [];

	constructor(private cookie:CookieService,private http: HttpClient,private _router: Router) {
		this.httpOptions = {
			headers: new HttpHeaders({'Content-Type': 'application/json'})
		};
	}

	public register(user: Forminfo): Observable<Forminfo> {
	  return this.http.post<Forminfo>('http://127.0.0.1:8000/dashboardapi/users', user);
	}
	public login(user){
		this.http.post('http://127.0.0.1:8000/api-token-auth/', JSON.stringify(user), this.httpOptions).subscribe(
	      data => {
	        this.updateData(data['token']);
	        this._router.navigate(['/dashboard']);
	      },
	      err => {
	        this.errors = err['error'];
	        console.log(err);
	      }
	    );
	}
	public refreshToken() {
	    this.http.post('http://127.0.0.1:8000/api-token-refresh/', JSON.stringify({token: this.cookie.get("JWT")}), this.httpOptions).subscribe(
	      data => {
	        this.updateData(data['token']);
	      },
	      err => {
	        this.errors = err['error'];
	      }
	    );
  	}
  	public logout() {
	    this.cookie.delete("JWT");
	}
	public isLoggedIn(){
		return !!this.cookie.get("JWT");
	}
	private updateData(token) {
		this.cookie.set("JWT",token);
		this.errors = [];
	}

}