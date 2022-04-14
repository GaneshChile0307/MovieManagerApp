import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { AlertService, UserService } from '../_services';
import { IDropdownSettings } from 'ng-multiselect-dropdown';

@Component({
  selector: 'app-add-update-artist-movie',
  templateUrl: './add-update-artist-movie.component.html',
  styleUrls: ['./add-update-artist-movie.component.css']
})
export class AddUpdateArtistMovieComponent implements OnInit {

  artistMovieId: any = 0;
  subMovieId: any = 0;
  pageHeading: String;
  buttonTitle: String;
  private routeSub: Subscription;
  adminId: any;
  operation: any;
  artistsTypeData: any = [];
  selectedArtistType: any = [];
  dropdownSettings:IDropdownSettings;
  subMovieName: any;
  subMovieDescription: any;
  subMovieCategory: String = '';
  subMovieSequelNumber: any;
  submovieData: any = [];
  artistData: any = [];
  movieId: any;
  artistId: any;
  artistType: any = '';

  constructor(private formBuilder: FormBuilder,
    private router: Router,
    private userService: UserService,
    private alertService: AlertService,
    private route: ActivatedRoute) { }

  ngOnInit() {

    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.adminId = params['id']
      this.operation = params['operation']
      if(this.operation == 'update'){
        // console.log("Hi I am update")
        this.artistMovieId = params['amid']
      }
    })

    if(this.operation == 'add'){
      this.pageHeading = "Add Artist Movie Data";
      this.buttonTitle = "ADD"
    }
    else{
      this.pageHeading = "Update Artist Movie Data",
      this.buttonTitle = "UPDATE"
    }

    this.userService.getAllArtistType()
      .subscribe(
        data => {
          console.log(data)
          if(data.status == 'success'){
            this.artistsTypeData = data.artist_typedata;
            console.log(this.artistsTypeData);
          }
        }
      )

      this.userService.getAllSubMovie()
      .subscribe(
        data => {
          console.log(data)
          if(data.status == 'success'){
            this.submovieData = data.sub_movie_data;
          }
        }
      )

      this.userService.getAllArtist()
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              this.artistData = data.artist_data;
            }
          }
        )
      
      if(this.artistMovieId != 0){
        this.userService.getArtistMovieDataById(this.artistMovieId)
          .subscribe(
            data => {
              console.log("Hello");
              console.log(data)
              if(data.status == 'success'){
                this.subMovieId = data.artist_moviedata[0].sub_movie_id;
                this.artistId = data.artist_moviedata[0].artist_id;
              }
            }
          )
      }

      this.dropdownSettings = {
        singleSelection: false,
        idField: 'aid',
        textField: 'atype',
        selectAllText: 'Select All',
        unSelectAllText: 'UnSelect All',
        itemsShowLimit: 3,
        allowSearchFilter: true
      };
  }

  selectChangeSubMovieHandler(event: any) {
    this.subMovieId = event.target.value;
    console.log(this.subMovieId)
  }

  selectChangeArtistHandler(event: any) {
    this.artistId = event.target.value;
    console.log(this.artistId)
  }

  onItemSelect(item: any) { 
    console.log(item)
  }

  onSelectAll(items: any) {
    console.log(items);
  }

  onDeSelect(item: any){
    console.log(item);
  }

  onSubmit(){

    for(let i =0; i< this.selectedArtistType.length; i++){
      this.artistType = this.artistType + this.selectedArtistType[i].atype + ', ';
    }

    if(this.operation == 'add'){
      let obj= {
        "submovieid": this.subMovieId,
        "artistid": this.artistId,
        "artisttype": this.artistType.slice(0,-2)
      };

      console.log(obj);

      this.userService.addArtistMovieData(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Artist Movie Added Successfully');
              this.router.navigate(['admin/artistmoviemanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in adding artist movie data, Please try again!'
              });
              this.router.navigate(['admin/artistmoviemanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in adding artist movie data, Please try again!'
            });
            this.router.navigate(['admin/artistmoviemanager/'+this.adminId])
          }
        )

    }
    else if(this.operation == 'update'){
      let obj= {
        "artistmovieid": this.artistMovieId,
        "submovieid": this.subMovieId,
        "artistid": this.artistId,
        "artisttype": this.artistType.slice(0,-2)
      };

      console.log(obj);

      this.userService.updateArtistMovieData(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Artist Movie Data Updated Successfully');
              this.router.navigate(['admin/artistmoviemanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in updating artist movie data, Please try again!'
              });
              this.router.navigate(['admin/artistmoviemanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in updating artist movie data, Please try again!'
            });
            this.router.navigate(['admin/artistmoviemanager/'+this.adminId])
          }
        )

    }
    else{
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Error in adding/updating artist movie data, Please try again!'
      });
      this.router.navigate(['admin/artistmoviemanager/'+this.adminId])
    }
  }

  backButton(){
    this.router.navigate(['admin/artistmoviemanager/'+this.adminId])
  }
}
