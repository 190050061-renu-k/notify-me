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
      username: ['',Validators.required],
      email: ['',[Validators.required,Validators.email]],
      password: ['',Validators.required],
    });
  }
  info: Forminfo;

  updateProfile() {
    this.profileForm.patchValue({
      username: '',
      email: '',
      password: '',
    });
  }

  register() {
    
    this.configService.register(this.profileForm.value).subscribe(
      data => {
        this.updateProfile();
        this._router.navigate(['/dashboard']);
      },
      error => {
        this.updateProfile();
      }
    );
  }
  login(){
    this.configService.login(this.profileForm.value);
    
  }
  /*
   this.updateProfile();
   this._router.navigate(['/dashboard']); */
   
  }