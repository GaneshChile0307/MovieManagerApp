import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { UserService } from '../_services';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  private routeSub: Subscription;
  currentUserName: String;
  userId = String;
  constructor(private route: ActivatedRoute,
    private userService: UserService,
    private router: Router) { }

  ngOnInit() {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.userId = params['id'];
      this.userService.getUserDataById(this.userId)
        .subscribe(
          data => {
            console.log(data)
            this.currentUserName = data.user_data[0].fn+ ' '+ data.user_data[0].ln
            console.log(this.currentUserName)
          }
        )
    });
  }


  addWatchedMovies(event: Event) { 
    console.log("‘Click!", event) 
    this.router.navigate(['user/addwatchedmovies/'+this.userId]);
  } 

  updateWatchedMovies(event: Event) { 
    console.log("‘Click!", event) 
    this.router.navigate(['user/updatewatchedmovies/'+this.userId]);
  } 

  suggestMovies(event: Event) { 
    console.log("‘Click!", event) 
    this.router.navigate(['user/suggestmovies/'+this.userId]);
  } 

  rateMovies(event: Event) { 
    console.log("‘Click!", event) 
    this.router.navigate(['user/ratemovies/'+this.userId]);
  } 

  updateRating(event: Event) { 
    console.log("‘Click!", event) 
    this.router.navigate(['user/updaterating/'+this.userId]);
  } 

  movieRatings(event: Event) { 
    console.log("‘Click!", event) 
    this.router.navigate(['user/movieratings/'+this.userId+'/user']);
  } 

  BackButton(){
    this.router.navigate(['login'])
  }
}
