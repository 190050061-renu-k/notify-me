import { Component, OnInit } from '@angular/core';
import { Course } from '../course';
import { Deadline } from '../deadline';
import { Student } from '../student';
import {DashboardService} from '../dashboard.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';



@Component({
  selector: 'app-course-info',
  templateUrl: './course-info.component.html',
  styleUrls: ['./course-info.component.scss']
})
export class CourseInfoComponent implements OnInit {
  columns1:String[];
  columns2:String[];
  columns3:String[];
  deadlines;
  students;
  tas;
  code:String;
  role;
  constructor(private dashboardService: DashboardService, private router:Router, private activatedroute:ActivatedRoute){
  }

  ngOnInit(): void {
  	this.code=this.activatedroute.snapshot.params['code'];
  	this.getStudents();
  	this.getDeadlines();
    this.getTAs();
    this.role=localStorage.getItem("Role");
    if(this.role=="instructor"){
      this.columns1=['message', 'end_date', 'delete'];
      this.columns2=['user', 'delete'];
      this.columns3=['TA', 'delete'];
    }
    else{
      this.columns1=['message', 'end_date'];
      this.columns2=['user'];
    }
  }

  getStudents(){
  	this.dashboardService.studentlist(this.code).subscribe(
  		data=>{
  			this.students=data;
  		},
  		error=>{
  			console.log(error);
  		},
  		()=>{}
  	);
  }
  getDeadlines(){
  	this.dashboardService.deadlinelist(this.code).subscribe(
  		data=>{
  			this.deadlines=data;
  		},
  		error=>{
  			console.log(error);
  		},
  		()=>{}
  	);
  }
  getTAs(){
    this.dashboardService.TAlist(this.code).subscribe(
      data=>{
        this.tas=data;
        console.log(this.tas);
      },
      error=>{
        console.log(error);
      },
      ()=>{}
    );
  }
  deleteDeadline(deadline){
    this.dashboardService.deleteDeadline({'id':deadline.id}).subscribe(
      data=>{
        this.getDeadlines();
      },
      error=>{
        console.log("You are not authorized to delete the deadline");
      }
    );
  }
  removeStudent(student){
    this.dashboardService.removeStudent({'user':student.user, 'code':this.code}).subscribe(
      data=>{
        this.getStudents();
      },
      error=>{
        console.log("You are not authorized to delete the deadline");
      }
    );
  }
  removeTA(ta){
    this.dashboardService.removeTA({'user':ta.user, 'code':this.code}).subscribe(
      data=>{
        this.getTAs();
      },
      error=>{
        console.log("You are not authorized to remove the Student");
      }
    );
  }
  addTa(){
    this.router.navigate(['/addTA/'+this.code]);
  }
  create(){
    this.router.navigate(['/createdeadline/'+this.code]);
  }
}
