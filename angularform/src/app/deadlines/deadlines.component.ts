import { Component, OnInit } from '@angular/core';
import { Deadline } from '../deadline';
import { DashboardService } from '../dashboard.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-deadlines',
  templateUrl: './deadlines.component.html',
  styleUrls: ['./deadlines.component.scss']
})
export class DeadlinesComponent implements OnInit {

  constructor(private dashboard:DashboardService,private fb: FormBuilder,private _router: Router, private activatedroute:ActivatedRoute) { }
  code:String;
  createform: FormGroup;
  ngOnInit(): void {
  	this.code=this.activatedroute.snapshot.params['code'];
	this.createform = this.fb.group({
		message: ['',Validators.required],
		hard: ['',Validators.required],
		end_date:['', Validators.required]
	});

  }
  create(){
		this.dashboard.createDeadline(this.createform.value, this.code).subscribe(
			data=>{
				alert('Successfully created the deadline '+data['message']+'!');
				this._router.navigate(['/detail/'+this.code]);
			},
			error=>{
				alert("Please login again");
			}
		)
	}


}
