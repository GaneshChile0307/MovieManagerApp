import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateWatchedMoviesComponent } from './update-watched-movies.component';

describe('UpdateWatchedMoviesComponent', () => {
  let component: UpdateWatchedMoviesComponent;
  let fixture: ComponentFixture<UpdateWatchedMoviesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateWatchedMoviesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateWatchedMoviesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
