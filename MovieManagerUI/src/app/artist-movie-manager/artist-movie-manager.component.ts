import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { AlertService, UserService } from '../_services';

@Component({
  selector: 'app-artist-movie-manager',
  templateUrl: './artist-movie-manager.component.html',
  styleUrls: ['./artist-movie-manager.component.css']
})
export class ArtistMovieManagerComponent implements OnInit {

  adminId: any;
  artistMovieData: any = [];
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

    this.userService.getAllArtistMovieData()
      .subscribe(
        data => {
          console.log(data);
          if(data.status == 'success'){
            this.artistMovieData = data.artist_moviedata;
          }   
        }
      )
  }

  deleteArtistMovieData(artistMovieId){
    let obj = {
      "artistmovieid": artistMovieId 
    }

    this.userService.deleteArtistMovieData(obj)
      .subscribe(
        data => {
          console.log(data);
          if(data.status == 'success'){
            Swal.fire('Deleted Artist Movie data Successfully');
            this.ngOnInit();
          }
          else{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in deleting artist movie data, Please try again!'
            });
            this.ngOnInit();
          }
        },
        error => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in deleting artist movie data, Please try again!'
          });
          this.ngOnInit();
        }
      )
  }

  updateArtistMovieData(artistMovieId){
    this.router.navigate(['admin/artistmoviemanager/'+this.adminId+'/'+artistMovieId+'/update'])
  }

  addArtistMovieData(){
    this.router.navigate(['admin/artistmoviemanager/'+this.adminId+'/add'])
  }

  backButton(){
    this.router.navigate(['admin/'+this.adminId])
  }

}
