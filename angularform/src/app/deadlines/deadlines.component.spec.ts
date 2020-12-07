import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeadlinesComponent } from './deadlines.component';

describe('DeadlinesComponent', () => {
  let component: DeadlinesComponent;
  let fixture: ComponentFixture<DeadlinesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeadlinesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DeadlinesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
