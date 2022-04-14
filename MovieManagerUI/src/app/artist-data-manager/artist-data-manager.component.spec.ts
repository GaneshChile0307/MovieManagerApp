import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtistDataManagerComponent } from './artist-data-manager.component';

describe('ArtistDataManagerComponent', () => {
  let component: ArtistDataManagerComponent;
  let fixture: ComponentFixture<ArtistDataManagerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ArtistDataManagerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ArtistDataManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
