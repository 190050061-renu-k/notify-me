import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddTAComponent } from './add-ta.component';

describe('AddTAComponent', () => {
  let component: AddTAComponent;
  let fixture: ComponentFixture<AddTAComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddTAComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddTAComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
