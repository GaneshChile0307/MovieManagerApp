import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { UserService } from '../_services';

@Component({
  selector: 'app-update-watched-movies',
  templateUrl: './update-watched-movies.component.html',
  styleUrls: ['./update-watched-movies.component.css']
})
export class UpdateWatchedMoviesComponent implements OnInit {

  private routeSub: Subscription;
  movie_data: any;
  userId: any;
  data = {
    "movie_data": [
      {
        "trackId": 1,
        "subMovieId": 1,
        "subMovieName": "Tere Naam"
      },
      {
        "trackId": 2,
        "subMovieId": 4,
        "subMovieName": "Dhadkan"
      },
      {
        "trackId": 3,
        "subMovieId": 3,
        "subMovieName": "Aashqi"
      }
    ],
    "status": "success"
  };

  constructor(private userService: UserService,
    private router: Router,
    private route: ActivatedRoute) { }

  ngOnInit() {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.userId = params['id'];
    });
    this.userService.getUserWatchedMovies(this.userId)
        .subscribe(
          data => {
            console.log(data);
            if(data.status == 'success'){
              this.movie_data = data.user_movie_track_data;
            }
            else{
              this.movie_data = [];
            }
          }
        )
  }

  deleteMovie(id){
    let obj = {
      "track_id" : id
    }

    this.userService.deleteUserMovieTrackData(obj)
      .subscribe(
        data => {
          console.log(data);
          if(data.status == 'success'){
            Swal.fire('Watched Movie deleted successfully!');
          }
          else{
            Swal.fire('Error in deleting watched movie data. Please try again!');
          }
          this.ngOnInit();
        },
        error => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in deleting watched movie data. Please try again!'
          })
        }
      )
    console.log(id);
  }

  backButton(){
    this.router.navigate(['user/'+this.userId])
  }

}
