import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Validators } from '@angular/forms';
import {Course} from '../course';
import { Router } from '@angular/router';
import { DashboardService } from '../dashboard.service';

@Component({
  selector: 'app-create-course',
  templateUrl: './create-course.component.html',
  styleUrls: ['./create-course.component.scss']
})
export class CreateCourseComponent implements OnInit {

  constructor(private dashboard:DashboardService,private fb: FormBuilder,private _router: Router) { }
  createform: FormGroup;
	ngOnInit(): void {
		this.createform = this.fb.group({
			code: ['',Validators.required],
			name: ['',Validators.required]
    	});		
	}

	create(){
		this.dashboard.create(this.createform.value).subscribe(
			data=>{
				alert('Successfully created the course '+data['name']+'!');
				this._router.navigate(['/dashboard']);
			},
			error=>{
				alert("Course with this code already exists");
			}
		)
	}

}
