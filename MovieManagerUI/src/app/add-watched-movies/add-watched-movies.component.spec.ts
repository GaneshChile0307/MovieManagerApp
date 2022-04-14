import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddWatchedMoviesComponent } from './add-watched-movies.component';

describe('AddWatchedMoviesComponent', () => {
  let component: AddWatchedMoviesComponent;
  let fixture: ComponentFixture<AddWatchedMoviesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddWatchedMoviesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddWatchedMoviesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
