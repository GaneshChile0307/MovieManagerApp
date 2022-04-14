import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { UserService } from '../_services';

@Component({
  selector: 'app-movie-rating-manager',
  templateUrl: './movie-rating-manager.component.html',
  styleUrls: ['./movie-rating-manager.component.css']
})
export class MovieRatingManagerComponent implements OnInit {

  ratingData: any;
  id: any;
  user: any;
  private routeSub: Subscription;
  constructor(private route: ActivatedRoute,
    private userService: UserService,
    private router: Router) { }

  ngOnInit() {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.id = params['id'];
      this.user = [params['user']]
    });

    this.userService.getAllMovieRating()
      .subscribe(
        data => {
          console.log(data);
          if(data.status == "success"){
            this.ratingData = data.rating_data;
            console.log(this.ratingData)
            
          }
        }
      )
  }

  onSumbit(){
    if(this.user == 'admin'){
      this.router.navigate(['admin/'+this.id])
    }
    else{
      this.router.navigate(['user/'+this.id])
    }
  }

}
