import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SuggestMoviesComponent } from './suggest-movies.component';

describe('SuggestMoviesComponent', () => {
  let component: SuggestMoviesComponent;
  let fixture: ComponentFixture<SuggestMoviesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SuggestMoviesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SuggestMoviesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
