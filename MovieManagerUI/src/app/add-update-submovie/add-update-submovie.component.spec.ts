import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddUpdateSubmovieComponent } from './add-update-submovie.component';

describe('AddUpdateSubmovieComponent', () => {
  let component: AddUpdateSubmovieComponent;
  let fixture: ComponentFixture<AddUpdateSubmovieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddUpdateSubmovieComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddUpdateSubmovieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
