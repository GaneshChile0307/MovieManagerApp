import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

import { AlertService, UserService } from '../_services';
import { e } from '@angular/core/src/render3';
import Swal from 'sweetalert2';

@Component({templateUrl: 'register.component.html'})
export class RegisterComponent implements OnInit {
    registerForm: FormGroup;
    loading = false;
    submitted = false;

    constructor(
        private formBuilder: FormBuilder,
        private router: Router,
        private userService: UserService,
        private alertService: AlertService) { }

    ngOnInit() {
        this.registerForm = this.formBuilder.group({
            firstName: ['', Validators.required],
            lastName: ['', Validators.required],
            username: ['', Validators.required],
            password: ['', [Validators.required, Validators.minLength(6)]],
            dob: ['', Validators.required],
            gender: ['', Validators.required],
            address: ['', Validators.required],
            contact: ['', Validators.required],
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }

    onSubmit() {
        this.submitted = true;
        // stop here if form is invalid
        if (this.registerForm.invalid) {
            return;
        }

        this.loading = true;
        console.log(this.registerForm.controls.firstName.value)
        var user = {
            "firstname" : this.registerForm.controls.firstName.value,
            "lastname" : this.registerForm.controls.lastName.value,
            "dateofbirth": this.registerForm.controls.dob.value,
            "gender": this.registerForm.controls.gender.value,
            "phone": this.registerForm.controls.contact.value,
            "email": this.registerForm.controls.username.value,
            "address": this.registerForm.controls.address.value,
            "city": this.registerForm.controls.address.value,
            "password": this.registerForm.controls.password.value,
            "usertype":"user"
            }
        this.userService.registerUser(user)
                .pipe(first())
                .subscribe(
                    data => {
                        console.log(data)
                        if(data.status == 'success'){
                            console.log("User Registration Successful!!");
                            Swal.fire('User Registration Successful!');
                            this.router.navigate(['/login']);
                        }
                        else{
                            console.log("User Registration Failed. Please try again.")
                            Swal.fire({
                                icon: 'error',
                                title: 'Oops...',
                                text: 'User already exists! Please try again with new email id!'
                              })
                            this.registerForm.controls.username.reset();
                            this.loading = false;

                        }
                        
                    },
                    error => {
                        this.alertService.error(error);
                        this.loading = false;
                    }
                    
                );
    
    }
}
