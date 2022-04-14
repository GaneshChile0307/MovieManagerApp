import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtistMovieManagerComponent } from './artist-movie-manager.component';

describe('ArtistMovieManagerComponent', () => {
  let component: ArtistMovieManagerComponent;
  let fixture: ComponentFixture<ArtistMovieManagerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ArtistMovieManagerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ArtistMovieManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
