import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { ConfigService } from './config.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard1Service implements CanActivate{

  constructor(public config:ConfigService, public router:Router) { }

  canActivate():boolean{
  	if(this.config.isLoggedIn()){
  		this.router.navigate(['dashboard']);
  		return false;
  	}
  	return true;
  }

}
