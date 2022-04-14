import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { AlertService, UserService } from '../_services';

@Component({
  selector: 'app-add-update-movie',
  templateUrl: './add-update-movie.component.html',
  styleUrls: ['./add-update-movie.component.css']
})
export class AddUpdateMovieComponent implements OnInit {

  movieId: any = 0;
  movieName: any = '';
  movieDescription: String = '';
  pageHeading: String;
  buttonTitle: String;
  private routeSub: Subscription;
  adminId: any;
  operation: any;

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
        this.movieId = params['mid']
      }
    })
    
    if(this.operation == 'add'){
      this.pageHeading = "Add Movie Data";
      this.buttonTitle = "ADD"
    }
    else{
      this.pageHeading = "Update Movie Data",
      this.buttonTitle = "UPDATE"
    }

    if(this.movieId != 0){
      this.userService.getMovieDataById(this.movieId)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              this.movieName = data.movie_data[0].mn;
              this.movieDescription = data.movie_data[0].mdescp
            }
          }
        )
    }
  }

  onSubmit(){

    if(this.operation == 'add'){
      let obj= {
        "moviename": this.movieName,
        "description": this.movieDescription
      }

      this.userService.addMovie(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Movie Added Successfully');
              this.router.navigate(['admin/moviemanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in adding movie, Please try again!'
              });
              this.router.navigate(['admin/moviemanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in adding movie, Please try again!'
            });
            this.router.navigate(['admin/moviemanager/'+this.adminId])
          }
        )

    }
    else if(this.operation == 'update'){
      let obj= {
        "movieid": this.movieId,
        "moviename": this.movieName,
        "description": this.movieDescription
      }

      this.userService.updateMovie(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Movie Updated Successfully');
              this.router.navigate(['admin/moviemanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in updating movie, Please try again!'
              });
              this.router.navigate(['admin/moviemanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in updating movie, Please try again!'
            });
            this.router.navigate(['admin/moviemanager/'+this.adminId])
          }
        )

    }
    else{
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Error in adding/updating movie, Please try again!'
      });
      this.router.navigate(['admin/moviemanager/'+this.adminId])
    }
  }

  backButton(){
    this.router.navigate(['admin/moviemanager/'+this.adminId])
  }

}
