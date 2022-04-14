import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import Swal from 'sweetalert2';
import { AlertService, UserService } from '../_services';

@Component({
  selector: 'app-submovie-data-manager',
  templateUrl: './submovie-data-manager.component.html',
  styleUrls: ['./submovie-data-manager.component.css']
})
export class SubmovieDataManagerComponent implements OnInit {

  adminId: any;
  subMovieData: any = [];
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

    this.userService.getAllSubMovie()
      .subscribe(
        data => {
          console.log(data);
          this.subMovieData = data.sub_movie_data;
        }
      )
  }

  deleteSubMovie(id){
    let obj = {
      "submovie_id": id 
    }

    this.userService.deleteSubMovie(obj)
      .subscribe(
        data => {
          console.log(data);
          if(data.status == 'success'){
            Swal.fire('Deleted Sub Movie Successfully');
            this.ngOnInit();
          }
          else{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error in deleting sub movie, Please try again!'
            });
            this.ngOnInit();
          }
        },
        error => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Error in deleting sub movie, Please try again!'
          });
          this.ngOnInit();
        }
      )
  }

  updateSubMovie(subMovieId){
    this.router.navigate(['admin/submoviemanager/'+this.adminId+'/'+subMovieId+'/update'])
  }

  addSubMovie(){
    this.router.navigate(['admin/submoviemanager/'+this.adminId+'/add'])
  }

  backButton(){
    this.router.navigate(['admin/'+this.adminId])
  }

}
