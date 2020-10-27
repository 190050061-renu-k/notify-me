import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Validators } from '@angular/forms';
import { Forminfo } from '../forminfo';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  profileForm: FormGroup;

  constructor(private fb: FormBuilder,private _router: Router) { }

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      Username: ['',Validators.required],
      Password: ['',Validators.required],
    });
  }

  info: Forminfo;

  updateProfile() {
    this.profileForm.patchValue({
      Username: '',
      Password: '',
    });
  }

  onSubmit() {
    this.updateProfile();
    this._router.navigate(['/dashboard'])
  }
  
}
