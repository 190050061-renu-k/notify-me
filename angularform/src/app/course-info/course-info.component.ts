import { Component, OnInit } from '@angular/core';
import { Course } from '../course'
import { FormBuilder, FormGroup } from '@angular/forms'

@Component({
  selector: 'app-course-info',
  templateUrl: './course-info.component.html',
  styleUrls: ['./course-info.component.scss']
})
export class CourseInfoComponent implements OnInit {
  course: Course;
  constructor(){

  }

  ngOnInit(): void {

  }

}
