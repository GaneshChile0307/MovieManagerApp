import { Routes, RouterModule } from '@angular/router';
import { AddUpdateArtistMovieComponent } from './add-update-artist-movie/add-update-artist-movie.component';
import { AddUpdateArtistComponent } from './add-update-artist/add-update-artist.component';
import { AddUpdateMovieComponent } from './add-update-movie/add-update-movie.component';
import { AddUpdateSubmovieComponent } from './add-update-submovie/add-update-submovie.component';
import { AddWatchedMoviesComponent } from './add-watched-movies/add-watched-movies.component';
import { AdminComponent } from './admin/admin.component';
import { ArtistDataManagerComponent } from './artist-data-manager/artist-data-manager.component';
import { ArtistMovieManagerComponent } from './artist-movie-manager/artist-movie-manager.component';

import { HomeComponent } from './home';
import { LoginComponent } from './login';
import { MovieDataManagerComponent } from './movie-data-manager/movie-data-manager.component';
import { MovieRatingManagerComponent } from './movie-rating-manager/movie-rating-manager.component';
import { RateMoviesComponent } from './rate-movies/rate-movies.component';
import { RegisterComponent } from './register';
import { SubmovieDataManagerComponent } from './submovie-data-manager/submovie-data-manager.component';
import { SuggestMoviesComponent } from './suggest-movies/suggest-movies.component';
import { UpdateRatingComponent } from './update-rating/update-rating.component';
import { UpdateWatchedMoviesComponent } from './update-watched-movies/update-watched-movies.component';
import { UserComponent } from './user/user.component';
import { AuthGuard } from './_guards';

const appRoutes: Routes = [
    { path: '', component: HomeComponent, canActivate: [AuthGuard] },
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    {path: 'user/:id', component: UserComponent},
    {path: 'admin/:id', component: AdminComponent},
    {path: 'user/addwatchedmovies/:id', component: AddWatchedMoviesComponent},
    {path: 'user/updatewatchedmovies/:id', component: UpdateWatchedMoviesComponent},
    {path: 'user/suggestmovies/:id', component: SuggestMoviesComponent},
    {path: 'user/ratemovies/:id', component: RateMoviesComponent},
    {path: 'user/updaterating/:id', component: UpdateRatingComponent},
    {path: 'admin/artistdatamanager/:id', component: ArtistDataManagerComponent},
    {path: 'admin/moviemanager/:id', component: MovieDataManagerComponent},
    {path: 'admin/submoviemanager/:id', component: SubmovieDataManagerComponent},
    {path: 'admin/moviemanager/:id/:mid/:operation', component: AddUpdateMovieComponent},
    {path: 'admin/moviemanager/:id/:operation', component: AddUpdateMovieComponent},
    {path: 'admin/artistmanager/:id/:aid/:operation', component: AddUpdateArtistComponent},
    {path: 'admin/artistmanager/:id/:operation', component: AddUpdateArtistComponent},
    {path: 'admin/submoviemanager/:id/:smid/:operation', component: AddUpdateSubmovieComponent},
    {path: 'admin/submoviemanager/:id/:operation', component: AddUpdateSubmovieComponent},
    {path: 'admin/movieratings/:id/:user', component: MovieRatingManagerComponent},
    {path: 'user/movieratings/:id/:user', component: MovieRatingManagerComponent},
    {path: 'admin/artistmoviemanager/:id', component: ArtistMovieManagerComponent},
    {path: 'admin/artistmoviemanager/:id/:amid/:operation', component: AddUpdateArtistMovieComponent},
    {path: 'admin/artistmoviemanager/:id/:operation', component: AddUpdateArtistMovieComponent},




    // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

export const routing = RouterModule.forRoot(appRoutes);