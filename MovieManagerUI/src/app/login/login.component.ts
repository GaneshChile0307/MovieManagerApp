import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

import { AlertService, AuthenticationService, UserService } from '../_services';
import Swal from 'sweetalert2';

@Component({templateUrl: 'login.component.html'})
export class LoginComponent implements OnInit {
    loginForm: FormGroup;
    loading = false;
    submitted = false;
    returnUrl: string;
    id: string = '-1';

    constructor(
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private router: Router,
        private authenticationService: AuthenticationService,
        private userService: UserService,
        private alertService: AlertService) {}
        

    ngOnInit() {
        this.loginForm = this.formBuilder.group({
            username: ['', Validators.required],
            password: ['', Validators.required]
        });

        // reset login status
        this.authenticationService.logout();

        // get return url from route parameters or default to '/'
        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
    }

    // convenience getter for easy access to form fields
    get f() { return this.loginForm.controls; }

    onSubmit() {
        this.submitted = true;

        // stop here if form is invalid
        if (this.loginForm.invalid) {
            return;
        }

        this.loading = true;

        let user = {
            "username": this.loginForm.controls.username.value,
            "password": this.loginForm.controls.password.value
        }

        this.userService.loginUser(user)
            .subscribe(
                data => {
                    console.log(data);
                    if(data.status == "success"){
                        this.userService.getUserData(this.loginForm.controls.username.value)
                            .subscribe(
                                data1 => {
                                    console.log(data1);
                                    if(data1.status == 'success'){
                                        console.log(this.id)
                                        this.id = data1.user_data[0].uid
                                        console.log(this.id)
                                        if(data.user_type == 'user'){
                                            console.log("User");
                                            this.router.navigate(['/user/'+this.id]);
                                        }
                                        else{
                                            console.log(data.user_type);
                                            this.router.navigate(['/admin/'+this.id]);
                                        }   
                                    }
                                    else{
                                        Swal.fire('User does not exist. Please register first!');
                                        this.router.navigate(['/register']);
                                    }
                                }
                            )
                    }
                    else{
                        Swal.fire('User does not exist. Please register first!');
                        this.router.navigate(['/register']);
                    }    
                }
            );
    }
}
