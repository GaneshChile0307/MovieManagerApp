import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { UserService } from '../_services';

@Component({
  selector: 'app-artist-data-manager',
  templateUrl: './artist-data-manager.component.html',
  styleUrls: ['./artist-data-manager.component.css']
})
export class ArtistDataManagerComponent implements OnInit {
  private routeSub: Subscription;
  currentUserName: String;
  adminId: String
  artistData: any = [];
  constructor(private route: ActivatedRoute,
    private userService: UserService,
    private router: Router) { }
  
  
  ngOnInit(): void {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.adminId = params['id'];
    });

    this.userService.getAllArtist()
      .subscribe(
        data => {
          console.log(data);
          if(data.status == "success"){
            this.artistData = data.artist_data;
          }
        }
      )
  }

  deleteArtist(id){
    let obj = {
      "artist_id": id 
    }

    this.userService.deleteArtist(obj)
      .subscribe(
        data => {
          console.log(data);
          if(data.status == 'success'){
            Swal.fire('Deleted Artist Successfully');
            this.ngOnInit();
          }
          else{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in deleting artist, Please try again!'
            });
            this.ngOnInit();
          }
        },
        error => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in deleting artist, Please try again!'
          });
          this.ngOnInit();
        }
      )

  }

  updateArtist(artistId){
    // let obj= {
    //   "artistid": artistId,
    //   "firstname": firstName,
    //   "lastname": lastname,
    //   "dateofbirth": dateofbirth,
    //   "gender": gender,
    //   "phone": phone,
    //   "email": email,
    //   "address": address,
    //   "city": city,
    //   "country": country,
    //   "description": description
    // }
    this.router.navigate(['admin/artistmanager/'+this.adminId+'/'+artistId+'/update'])
  }

  addArtist(){
    this.router.navigate(['admin/artistmanager/'+this.adminId+'/add'])
  }

  backButton(){
    this.router.navigate(['admin/'+this.adminId])
  }

}
