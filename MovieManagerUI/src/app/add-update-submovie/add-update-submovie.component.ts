import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { AlertService, UserService } from '../_services';
import { IDropdownSettings } from 'ng-multiselect-dropdown';

@Component({
  selector: 'app-add-update-submovie',
  templateUrl: './add-update-submovie.component.html',
  styleUrls: ['./add-update-submovie.component.css']
})
export class AddUpdateSubmovieComponent implements OnInit {

  subMovieId: any = 0;
  pageHeading: String;
  buttonTitle: String;
  private routeSub: Subscription;
  adminId: any;
  operation: any;
  subMoviesCategory: any = [];
  selectedMovieCategory: any = [];
  dropdownSettings:IDropdownSettings;
  subMovieName: any;
  subMovieDescription: any;
  subMovieCategory: String = '';
  subMovieSequelNumber: any;
  movieData: any = [];
  movieId: any;

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
        this.subMovieId = params['smid']
      }
    })
    
    if(this.operation == 'add'){
      this.pageHeading = "Add Subordinate Movie Data";
      this.buttonTitle = "ADD"
    }
    else{
      this.pageHeading = "Update Subordinate Movie Data",
      this.buttonTitle = "UPDATE"
    }

    this.userService.getAllMovieCategory()
      .subscribe(
        data => {
          console.log(data)
          this.subMoviesCategory = data.movie_categorydata;
          console.log(this.subMoviesCategory);
        }
      )

    this.userService.getGetAllMovieData()
        .subscribe(
          data => {
            console.log(data)
            this.movieData = data.moviedata;
          }
        )

    if(this.subMovieId != 0){
      this.userService.getSubMovieById(this.subMovieId)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              this.subMovieName = data.sub_movie_data[0].smn;
              this.subMovieSequelNumber = data.sub_movie_data[0].sm_sq;
              this.subMovieDescription = data.sub_movie_data[0].sm_descp;
              // this.subMovieCategory = data.sub_movie_data[0].sm_cat;
              this.movieId = data.sub_movie_data[0].mid;
    
              for(let i = 0; i< this.subMoviesCategory.length; i++){
                const movieCat = this.subMovieCategory+ ""
                if(movieCat.includes(this.subMoviesCategory[i].mcateg)){
                  this.selectedMovieCategory.push(this.subMoviesCategory[i])
                }
              }
            }
            console.log(this.selectedMovieCategory)
          }
        )
    }

    this.dropdownSettings = {
    singleSelection: false,
    idField: 'mcid',
    textField: 'mcateg',
    selectAllText: 'Select All',
    unSelectAllText: 'UnSelect All',
    itemsShowLimit: 3,
    allowSearchFilter: true
    };
  }

  selectChangeHandler(event: any) {
    this.movieId = event.target.value;
    console.log(this.movieId)
  }

  onItemSelect(item: any) {
    // this.subMovieCategory = this.subMovieCategory + item.mcateg + ', ';
    console.log(this.subMovieCategory);
    console.log(this.selectedMovieCategory);
  }
  onSelectAll(items: any) {
    console.log(items);
  }

  onDeSelect(item: any){
    console.log(item);
  }


  onSubmit(){

    for(let i =0; i< this.selectedMovieCategory.length; i++){
      this.subMovieCategory = this.subMovieCategory + this.selectedMovieCategory[i].mcateg + ', ';
    }

    if(this.operation == 'add'){
      let obj= {
        "sub_movie_name": this.subMovieName,
        "movie_id": this.movieId,
        "sub_movie_descrip": this.subMovieDescription,
        "sub_movie_category": (this.subMovieCategory).slice(0,-1),
        "sub_movie_sequel_number": this.subMovieSequelNumber
      };

      console.log(obj);

      this.userService.addSubMovie(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Subordinated Movie Added Successfully');
              this.router.navigate(['admin/submoviemanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in adding sub movie, Please try again!'
              });
              this.router.navigate(['admin/submoviemanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in adding sub movie, Please try again!'
            });
            this.router.navigate(['admin/submoviemanager/'+this.adminId])
          }
        )

    }
    else if(this.operation == 'update'){
      let obj= {
        "sub_movie_id": this.subMovieId,
        "sub_movie_name": this.subMovieName,
        "movie_id": this.movieId,
        "sub_movie_descrip": this.subMovieDescription,
        "sub_movie_category": this.subMovieCategory.slice(0,-2),
        "sub_movie_sequel_number": this.subMovieSequelNumber
      }

      console.log(obj);

      this.userService.updateSubMovie(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Subordinated Movie Updated Successfully');
              this.router.navigate(['admin/submoviemanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in updating sub movie, Please try again!'
              });
              this.router.navigate(['admin/submoviemanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in updating sub movie, Please try again!'
            });
            this.router.navigate(['admin/submoviemanager/'+this.adminId])
          }
        )

    }
    else{
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Error in adding/updating movie, Please try again!'
      });
      this.router.navigate(['admin/submoviemanager/'+this.adminId])
    }
  }

  backButton(){
    this.router.navigate(['admin/submoviemanager/'+this.adminId])
  }

}
