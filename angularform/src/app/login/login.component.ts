import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Validators } from '@angular/forms';
import { Forminfo } from '../forminfo';
import { Router } from '@angular/router';

import { ConfigService } from '../config.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {



  constructor(private configService: ConfigService,private fb: FormBuilder,private _router: Router) { }

  profileForm: FormGroup;

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      Username: ['',Validators.required],
      Email: ['',[Validators.required,Validators.email]],
      Password: ['',Validators.required],
    });
  }
  info: Forminfo;

  updateProfile() {
    this.profileForm.patchValue({
      Username: '',
      Email: '',
      Password: '',
    });
  }

  onSubmit() {
    
    this.configService.addinfo(this.profileForm.value).subscribe(
      data => {
        this.updateProfile();
        this._router.navigate(['/dashboard']);
      },
      error => {
        this.updateProfile();
      }
    );
  
   this.updateProfile();
   this._router.navigate(['/dashboard']); 
  } 
  
}
