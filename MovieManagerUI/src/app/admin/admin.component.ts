import { Component, OnInit , Injectable} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { UserService } from '../_services';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})

export class AdminComponent implements OnInit {
  private routeSub: Subscription;
  currentUserName: String;
  adminId: String
  constructor(private route: ActivatedRoute,
    private userService: UserService,
    private router: Router) { }
  
  
  ngOnInit(): void {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.adminId = params['id'];
      this.userService.getUserDataById(params['id'])
        .subscribe(
          data => {
            console.log(data)
            this.currentUserName = data.user_data[0].fn+ ' '+ data.user_data[0].ln 
            console.log(this.currentUserName)
          }
        )
    });
  }


  ManageArtistData(event: Event) { 
    this.router.navigate(['admin/artistdatamanager/'+this.adminId])
    console.log("‘Click!", event)
  }

  ManageMovieData(event: Event) { 
    this.router.navigate(['admin/moviemanager/'+this.adminId])
    console.log("‘Click!", event) 
  }

  ManageSubordinateMovie(event: Event) { 
    this.router.navigate(['admin/submoviemanager/'+this.adminId])
    console.log("‘Click!", event) 
  }

  MovieRating(event: Event) {
    this.router.navigate(['admin/movieratings/'+this.adminId+'/admin'])
    console.log("‘Click!", event) 
  }

  ManageArtistMovieData(event: Event){
    this.router.navigate(['admin/artistmoviemanager/'+this.adminId])
    console.log("‘Click!", event)
  }

  BackButton(){
    this.router.navigate(['login'])
  }

}
