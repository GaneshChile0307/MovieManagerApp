import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AddUpdateArtistComponent } from './add-update-artist.component';

describe('AddUpdateArtistComponent', () => {
  let component: AddUpdateArtistComponent;
  let fixture: ComponentFixture<AddUpdateArtistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AddUpdateArtistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AddUpdateArtistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
