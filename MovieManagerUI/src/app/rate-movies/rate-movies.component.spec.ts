import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RateMoviesComponent } from './rate-movies.component';

describe('RateMoviesComponent', () => {
  let component: RateMoviesComponent;
  let fixture: ComponentFixture<RateMoviesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RateMoviesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RateMoviesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
