import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieDataManagerComponent } from './movie-data-manager.component';

describe('MovieDataManagerComponent', () => {
  let component: MovieDataManagerComponent;
  let fixture: ComponentFixture<MovieDataManagerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MovieDataManagerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MovieDataManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
