import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { ConfigService } from './config.service';


@Injectable({
  providedIn: 'root'
})
export class Auth1Guard implements CanActivate {

  constructor(public config:ConfigService, public router:Router) { }
  canActivate():boolean{
  	if(this.config.isLoggedIn()){
  		this.router.navigate(['dashboard']);
  		return false;
  	}
  	return true;
  }
  
}
