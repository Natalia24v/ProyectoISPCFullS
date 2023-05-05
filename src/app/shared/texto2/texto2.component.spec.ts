import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Texto2Component } from './texto2.component';

describe('Texto2Component', () => {
  let component: Texto2Component;
  let fixture: ComponentFixture<Texto2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Texto2Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Texto2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
