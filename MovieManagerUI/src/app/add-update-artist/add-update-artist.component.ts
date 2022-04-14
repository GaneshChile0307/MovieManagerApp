import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { AlertService, UserService } from '../_services';


@Component({
  selector: 'app-add-update-artist',
  templateUrl: './add-update-artist.component.html',
  styleUrls: ['./add-update-artist.component.css']
})
export class AddUpdateArtistComponent implements OnInit {

  adminId: any;
  artistId: any = 0;
  artistFirstName: String = "";
  artistLastName: String = "";
  artistDOB: String = "";
  artistContact: String = "";
  artistAddress: String = "";
  artistCity: String = "";
  artistCountry: String = "";
  artistDescription: String = "";
  artistEmail: String = "";
  artistGender: String = "";

  pageHeading: String;
  buttonTitle: String;
  private routeSub: Subscription;
  operation: any;
  constructor(private formBuilder: FormBuilder,
    private router: Router,
    private userService: UserService,
    private alertService: AlertService,
    private route: ActivatedRoute) { }

  ngOnInit() {
    this.routeSub = this.route.params.subscribe(params => {
      console.log(params) //log the entire params object
      console.log(params['id']) //log the value of id
      this.adminId = params['id']
      this.operation = params['operation']
      if(this.operation == 'update'){
        // console.log("Hi I am update")
        this.artistId = params['aid']
      }
    })
    
    if(this.operation == 'add'){
      this.pageHeading = "Add Artist Data";
      this.buttonTitle = "ADD"
    }
    else{
      this.pageHeading = "Update Artist Data",
      this.buttonTitle = "UPDATE"
    }

    if(this.artistId != 0){
      this.userService.getArtistById(this.artistId)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              this.artistFirstName = data.artist_data[0].afn;
              this.artistLastName = data.artist_data[0].aln;
              this.artistDOB = data.artist_data[0].dob;
              this.artistContact = data.artist_data[0].acn;
              this.artistAddress = data.artist_data[0].addr;
              this.artistCity = data.artist_data[0].city;
              this.artistCountry= data.artist_data[0].ctry;
              this.artistDescription= data.artist_data[0].descrp;
              this.artistEmail= data.artist_data[0].email;
              this.artistGender = data.artist_data[0].ag;
            }
          }
        )
    }
  }

  onSubmit(){
    if(this.operation == 'add'){
      let obj= {
        "firstname": this.artistFirstName,
        "lastname": this.artistLastName,
        "dateofbirth": this.artistDOB,
        "gender": this.artistGender,
        "phone": this.artistContact,
        "email": this.artistEmail,
        "address": this.artistAddress,
        "city": this.artistCity,
        "country": this.artistCountry,
        "description": this.artistDescription
      }

      this.userService.addArtist(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Artist Added Successfully');
              this.router.navigate(['admin/artistdatamanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in adding artist, Please try again!'
              });
              this.router.navigate(['admin/artistdatamanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in adding artist, Please try again!'
            });
            this.router.navigate(['admin/artistdatamanager/'+this.adminId])
          }
        )

    }
    else if(this.operation == 'update'){
      let obj= {
        "artistid": this.artistId,
        "firstname": this.artistFirstName,
        "lastname": this.artistLastName,
        "dateofbirth": this.artistDOB,
        "gender": this.artistGender,
        "phone": this.artistContact,
        "email": this.artistEmail,
        "address": this.artistAddress,
        "city": this.artistCity,
        "country": this.artistCountry,
        "description": this.artistDescription
      }

      this.userService.updateArtist(obj)
        .subscribe(
          data => {
            console.log(data)
            if(data.status == 'success'){
              Swal.fire('Artist Updated Successfully');
              this.router.navigate(['admin/artistdatamanager/'+this.adminId]);
            }
            else{
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Error in updating artist, Please try again!'
              });
              this.router.navigate(['admin/artistdatamanager/'+this.adminId])
            }
          },
          error => {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in updating artist, Please try again!'
            });
            this.router.navigate(['admin/artistdatamanager/'+this.adminId])
          }
        )

    }
    else{
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Error in adding/updating artist, Please try again!'
      });
      this.router.navigate(['admin/artistdatamanager/'+this.adminId])
    }
  }

  backButton(){
    this.router.navigate(['admin/artistdatamanager/'+this.adminId])
  }

}
