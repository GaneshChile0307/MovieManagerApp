import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

import { AlertService, UserService } from '../_services';
import { e } from '@angular/core/src/render3';
import Swal from 'sweetalert2';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-update-rating',
  templateUrl: './update-rating.component.html',
  styleUrls: ['./update-rating.component.css']
})
export class UpdateRatingComponent implements OnInit {

  private routeSub: Subscription
  addWatchedMovieForm: FormGroup;
  loading = false;
  submitted = false;
  selectedMovie : any;
  subMovieId: any = -1;
  userId: any;
  movieData: any;
  movieRating: any = 0;
  trackId: any;
  data = {
    "movie_data": [
      {
        "subMovieId": 1,
        "subMovieName": "Tere Naam",
        "movieRating": 4,
        "user_movie_rating_id": 1
      },
      {
        "subMovieId": 4,
        "subMovieName": "Dhadkan",
        "movieRating": 3,
        "user_movie_rating_id": 2
      },
      {
        "subMovieId": 3,
        "subMovieName": "Aashqi",
        "movieRating": 2,
        "user_movie_rating_id": 3
      }
    ],
    "status": "success"
  }

  constructor(
      private formBuilder: FormBuilder,
      private router: Router,
      private userService: UserService,
      private alertService: AlertService,
      private route: ActivatedRoute) { }

  ngOnInit() {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.userId = params['id'];
    });
    this.movieRating = 0;
    this.userService.getUserRatedMovies(this.userId)
        .subscribe(
          data => {
            console.log(data);
            if(data.status == 'success'){
              this.movieData = data.user_movie_rating;
            }
            else{
              this.movieData = [];
            }
          }
        )
  }


  selectChangeHandler(event: any) {
  
    this.selectedMovie = event.target.value;
    let index = this.selectedMovie;
    console.log("Index Id: "+index)
    this.trackId = this.movieData[index].umrid;
    console.log("Track Id: "+this.trackId)
    this.subMovieId = this.movieData[index].smd;
    console.log("Sub Movie Id: "+ this.subMovieId);
    this.movieRating =  this.movieData[index].umr;
    console.log("Movie Rating Id: "+ this.movieRating);

  }

  onSubmit($event) {

    let obj = {
      "user_movie_rating_id": this.trackId,
      "user_id": this.userId,
      "sub_movie_id": this.subMovieId,
      "user_movie_rating": this.movieRating
    }
    console.log(obj);
    this.userService.updateUserMovieRating(obj)
      .subscribe(
        data => {
          console.log(data)
          if(data.status == 'success'){
            Swal.fire('User Movie Rating Updated Successfully');
          }
          else{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in updating movie rating, Please try again!'
            })
          }
          this.ngOnInit();
        },
        error => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in adding movie rating, Please try again!'
          })
          this.ngOnInit();
        }  
      )

  }

  deleteUserMovieRating($event){
    let obj = {
      "rating_id": this.trackId
    }
    console.log(obj);

    this.userService.deleteUserRatedMovie(obj)
      .subscribe(
        data => {
          console.log(data)
          if(data.status == 'success'){
            Swal.fire('User Movie Rating Deleted Successfully');
          }
          else{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in deleting movie rating, Please try again!'
            })
          }
          this.ngOnInit();
        },
        error => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in adding movie rating, Please try again!'
          })
          this.ngOnInit();
        }  
      )
  }

  backButton(){
    this.router.navigate(['user/'+this.userId])
  }

}
