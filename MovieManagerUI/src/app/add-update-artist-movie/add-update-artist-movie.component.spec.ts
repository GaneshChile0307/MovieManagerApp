import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddUpdateArtistMovieComponent } from './add-update-artist-movie.component';

describe('AddUpdateArtistMovieComponent', () => {
  let component: AddUpdateArtistMovieComponent;
  let fixture: ComponentFixture<AddUpdateArtistMovieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddUpdateArtistMovieComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddUpdateArtistMovieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
