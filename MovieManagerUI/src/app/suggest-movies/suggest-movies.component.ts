import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AlertService, UserService } from '../_services';
import { e } from '@angular/core/src/render3';
import Swal from 'sweetalert2';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-suggest-movies',
  templateUrl: './suggest-movies.component.html',
  styleUrls: ['./suggest-movies.component.css']
})
export class SuggestMoviesComponent implements OnInit {

  private routeSub: Subscription;
  userId: any;
  movieCategory: any;
  movieCategories: any;
  suggestedMovies: any = '';
  constructor(private formBuilder: FormBuilder,
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

    this.userService.getAllMovieCategory()
      .subscribe(
        data => {
          if(data.status = "success"){
            this.movieCategories = data.movie_categorydata;
            console.log(this.movieCategories)
          }
        }
      )
  }

  onSubmit(){
    let data = {
      "uid": this.userId,
      "movie_category": this.movieCategory
    }

    this.userService.getSuggestedMovies(data)
      .subscribe(
        data => {
          console.log(data);
          this.suggestedMovies = '';
          if(data.status == "success"){
            for(let i =0; i< data.suggested_movies.length; i++){
              console.log(data.suggested_movies[i]);
              this.suggestedMovies = this.suggestedMovies + (i+1)+ ". "+ data.suggested_movies[i].smn + "\n";
            }
            Swal.fire({
              icon: 'success',
              text: 'Suggested Movies for you to watch',
              title: this.suggestedMovies
            })
            console.log(this.suggestedMovies);
          }
        }
      )
  }

  selectChangeHandler(event: any){
    this.movieCategory = event.target.value;
    console.log(this.movieCategory);
  }

  backButton(){
    this.router.navigate(['user/'+this.userId])
  }

}
