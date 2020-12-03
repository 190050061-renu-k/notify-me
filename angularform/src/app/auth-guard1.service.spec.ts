import { TestBed } from '@angular/core/testing';

import { AuthGuard1Service } from './auth-guard1.service';

describe('AuthGuard1Service', () => {
  let service: AuthGuard1Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AuthGuard1Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
