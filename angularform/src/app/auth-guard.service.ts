import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { ConfigService } from './config.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate{

  constructor(public config:ConfigService, public router:Router) { }
  canActivate():boolean{
  	if(!this.config.isLoggedIn()){
  		this.router.navigate(['login']);
  		return false;
  	}
  	return true;
  }

}