import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieRatingManagerComponent } from './movie-rating-manager.component';

describe('MovieRatingManagerComponent', () => {
  let component: MovieRatingManagerComponent;
  let fixture: ComponentFixture<MovieRatingManagerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MovieRatingManagerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MovieRatingManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
