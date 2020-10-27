import { Component, OnInit } from '@angular/core';
import { Course } from '../course'

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
 
  allcourses: Course[] = [{name:"DSA",coursecode:"CS 213"},{name:"DAI",coursecode:"CS 215"},{name:"DS",coursecode:"CS 207"}];

  constructor() { }

  ngOnInit(): void {
  }

}
