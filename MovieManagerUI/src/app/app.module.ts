import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule }    from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

// used to create fake backend
import { fakeBackendProvider } from './_helpers';

import { AppComponent }  from './app.component';
import { routing }        from './app.routing';

import { AlertComponent } from './_directives';
import { AuthGuard } from './_guards';
import { JwtInterceptor, ErrorInterceptor } from './_helpers';
import { AlertService, AuthenticationService, UserService } from './_services';
import { HomeComponent } from './home';
import { LoginComponent } from './login';
import { RegisterComponent } from './register';;
import { UserComponent } from './user/user.component'
;
import { AdminComponent } from './admin/admin.component'
;
import { AddWatchedMoviesComponent } from './add-watched-movies/add-watched-movies.component';
import { UpdateWatchedMoviesComponent } from './update-watched-movies/update-watched-movies.component'
import { RateMoviesComponent } from './rate-movies/rate-movies.component';
import { SuggestMoviesComponent } from './suggest-movies/suggest-movies.component';
import { UpdateRatingComponent } from './update-rating/update-rating.component';;
import { MovieDataManagerComponent } from './movie-data-manager/movie-data-manager.component'
;
import { SubmovieDataManagerComponent } from './submovie-data-manager/submovie-data-manager.component'
import { ArtistDataManagerComponent } from './artist-data-manager/artist-data-manager.component';;
import { AddUpdateMovieComponent } from './add-update-movie/add-update-movie.component'
;
import { AddUpdateArtistComponent } from './add-update-artist/add-update-artist.component'
;
import { AddUpdateSubmovieComponent } from './add-update-submovie/add-update-submovie.component'
import { NgMultiSelectDropDownModule } from 'ng-multiselect-dropdown';;
import { MovieRatingManagerComponent } from './movie-rating-manager/movie-rating-manager.component'
;
import { ArtistMovieManagerComponent } from './artist-movie-manager/artist-movie-manager.component'
;
import { AddUpdateArtistMovieComponent } from './add-update-artist-movie/add-update-artist-movie.component'
@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        HttpClientModule,
        routing,
        FormsModule,
        NgMultiSelectDropDownModule.forRoot()
    ],
    declarations: [
        AppComponent,
        AlertComponent,
        HomeComponent,
        LoginComponent,
        RegisterComponent,
        UserComponent ,
        AdminComponent ,
        AddWatchedMoviesComponent ,
        UpdateWatchedMoviesComponent,
        RateMoviesComponent,
        SuggestMoviesComponent,
        UpdateRatingComponent ,
        MovieDataManagerComponent,
        SubmovieDataManagerComponent,
        ArtistDataManagerComponent,
        AddUpdateMovieComponent,
        AddUpdateArtistComponent,
        AddUpdateSubmovieComponent,
        MovieRatingManagerComponent,
        ArtistMovieManagerComponent,
        AddUpdateArtistMovieComponent],
    providers: [
        AuthGuard,
        AlertService,
        AuthenticationService,
        UserService,
        { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
        { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

        // provider used to create fake backend
        fakeBackendProvider
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }