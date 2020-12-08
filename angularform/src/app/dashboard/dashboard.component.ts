import { Component, OnInit } from '@angular/core';
import { Course } from '../course';
import {DashboardService} from '../dashboard.service';
import {ConfigService} from'../config.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
 	role;
	courses;
	constructor(private dashboardService: DashboardService, private configservice:ConfigService, private router:Router) { }

	ngOnInit(): void {
		this.getCourses();
		this.role=localStorage.getItem("Role");
	}
	getCourses(){
		this.dashboardService.list().subscribe(
			data=>{
				this.courses=data;
			},
			err=>{
				console.log(err);
			},
			() => {console.log('done loading courses');}
		);
	}
	create(){
		this.router.navigate(['/createcourse']);
	}
}
