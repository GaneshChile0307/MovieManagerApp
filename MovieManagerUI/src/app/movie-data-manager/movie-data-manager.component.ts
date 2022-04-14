import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { AlertService, UserService } from '../_services';

@Component({
  selector: 'app-movie-data-manager',
  templateUrl: './movie-data-manager.component.html',
  styleUrls: ['./movie-data-manager.component.css']
})
export class MovieDataManagerComponent implements OnInit {
  
  adminId: any;
  movieData: any;
  movie_name: any;
  movie_description; any;
  private routeSub: Subscription;
  constructor(private formBuilder: FormBuilder,
    private router: Router,
    private userService: UserService,
    private alertService: AlertService,
    private route: ActivatedRoute) { }

  ngOnInit() {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.adminId = params['id'];
    });

    this.userService.getGetAllMovieData()
      .subscribe(
        data => {
          console.log(data);
          this.movieData = data.moviedata;
        }
      )
  }

  deleteMovie(id){
    let obj = {
      "movie_id": id 
    }

    this.userService.deleteMovieById(obj)
      .subscribe(
        data => {
          console.log(data);
          if(data.status == 'success'){
            Swal.fire('Deleted Movie Successfully');
            this.ngOnInit();
          }
          else{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in deleting movie, Please try again!'
            });
            this.ngOnInit();
          }
        },
        error => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in deleting movie, Please try again!'
          });
          this.ngOnInit();
        }
      )
  }

  updateMovie(movieId){
    // let obj= {
    //   "movieid": movieId,
    //   "moviename": movieName,
    //   "description": description
    // }
    this.router.navigate(['admin/moviemanager/'+this.adminId+'/'+movieId+'/update'])
  }

  addMovie(){
    // let obj= {
    //   "moviename": this.movie_name,
    //   "description": this.movie_description
    // }
    this.router.navigate(['admin/moviemanager/'+this.adminId+'/add'])
  }

  backButton(){
    this.router.navigate(['admin/'+this.adminId])
  }


}
