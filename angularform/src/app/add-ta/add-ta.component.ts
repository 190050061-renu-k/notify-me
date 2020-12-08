import { Component, OnInit } from '@angular/core';
import { DashboardService } from '../dashboard.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-add-ta',
  templateUrl: './add-ta.component.html',
  styleUrls: ['./add-ta.component.scss']
})
export class AddTAComponent implements OnInit {

  constructor(private dashboard:DashboardService,private fb: FormBuilder,private _router: Router, private activatedroute:ActivatedRoute) { }
  code:String;
  createform: FormGroup;
  ngOnInit(): void {
  	this.code=this.activatedroute.snapshot.params['code'];
	this.createform = this.fb.group({
		username: ['',Validators.required]
	});

  }
  addTA(){
		this.dashboard.addTA(this.createform.value, this.code).subscribe(
			data=>{
				alert('Successfully added TA '+data['username']+'!');
				this._router.navigate(['/detail/'+this.code]);
			},
			error=>{
				alert("TA with the username doesn't exist");
			}
		)
	}


}
