import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

import { AlertService, UserService } from '../_services';
import { e } from '@angular/core/src/render3';
import Swal from 'sweetalert2';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-rate-movies',
  templateUrl: './rate-movies.component.html',
  styleUrls: ['./rate-movies.component.css']
})
export class RateMoviesComponent implements OnInit {

  private routeSub: Subscription
  addWatchedMovieForm: FormGroup;
  loading = false;
  submitted = false;
  selectedMovie : any;
  subMovieId: any = -1;
  userId: any;
  movieData: any;
  movieRating: any = 0;
  data = {
    "movie_data": [
      {
        "subMovieId": 1,
        "subMovieName": "Tere Naam"
      },
      {
        "subMovieId": 4,
        "subMovieName": "Dhadkan"
      },
      {
        "subMovieId": 3,
        "subMovieName": "Aashqi"
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
    this.userService.getUserNotRatedMovies(this.userId)
        .subscribe(
          data => {
            console.log(data);
            if(data.status == 'success'){
              this.movieData = data.not_rated_movies;
            }
            else{
              this.movieData = [];
            }
          }
        )
  }


  selectChangeHandler (event: any) {
    //update the ui
    this.selectedMovie = event.target.value;
    this.subMovieId = this.selectedMovie;
    console.log(this.movieData);
  }

  onSubmit($event) {

    let obj = {
      "user_id": this.userId,
      "sub_movie_id": this.selectedMovie,
      "user_movie_rating": this.movieRating
    }

    console.log(obj);

    this.userService.addUserRating(obj)
      .subscribe(
        data => {
          console.log(data)
          if(data.status == 'success'){
            Swal.fire('User Movie Rating Added Successfully');
            this.router.navigate(['user/'+this.userId]);
          }
          else{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in adding movie rating, Please try again!'
            })
            this.router.navigate(['user/'+this.userId]);
          }
        },
        error => {
          this.router.navigate(['user/'+this.userId]);
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in adding movie rating, Please try again!'
          })
        }
                  
      )
  }

  backButton(){
    this.router.navigate(['user/'+this.userId])
  }

}
