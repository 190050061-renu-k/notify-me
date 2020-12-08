import { Component, OnInit } from '@angular/core';
import {ConfigService} from '../config.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor( private configservice:ConfigService, private router:Router) { }

  ngOnInit(): void {
  }
  logout(){
  	this.configservice.logout();
		this.router.navigate(['/login']);
  }
  loggedIn(){
  	return this.configservice.isLoggedIn();
  }

}

