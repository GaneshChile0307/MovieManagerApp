import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { User } from '../_models';
import { JwtInterceptor } from '../_helpers';
import { catchError } from 'rxjs/operators';
// import { userInfo } from 'os';

@Injectable()
export class UserService {
    constructor(private http: HttpClient) { }
    
    baseUrl: String = 'http://localhost:8000/';

    getAll() {
        return this.http.get<User[]>(`${environment.apiUrl}/users`);
    }

    getById(id: number) {
        return this.http.get(`${environment.apiUrl}/users/` + id);
    }

    register(user: User) {
        return this.http.post(`${environment.apiUrl}/users/register`, user);
    }

    update(user: User) {
        return this.http.put(`${environment.apiUrl}/users/` + user.id, user);
    }

    delete(id: number) {
        return this.http.delete(`${environment.apiUrl}/users/` + id);
    }

    loginUser(user){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS,DELETE,PUT',
          });
        return this.http.post<any>(this.baseUrl+`login_user`, user, { headers: headers })
    }

    registerUser(user){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`register_user`, user, { headers: headers })
    }

    getArtistData(){
        return this.http.get<any>('http://127.0.0.1:8000/get_all_artist_details');
    }

    getUserData(email){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
        return this.http.get<any>(this.baseUrl+`get_user_details_by_email?email=`+email)
    }

    getUserDataById(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_user_details_by_id/`+id)
    }

    addUserMovieTrackData(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`add_movie_track_data`,obj, {headers: headers})
    }

    deleteUserMovieTrackData(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`delete_movie_track_data`,obj, {headers: headers})
    }

    addUserRating(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
        return this.http.post<any>(this.baseUrl+`add_movie_rating_data`, obj, {headers: headers})
    }

    updateUserRating(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
        return this.http.post<any>(this.baseUrl+`update_movie_rating_data`, obj, {headers: headers})
    }

    deleteUserRating(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
        return this.http.post<any>(this.baseUrl+`delete_movie_rating_data`, obj, {headers: headers})
    }

    getUserNotWatchedMovies(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`movie_not_watch_by_user/`+id)
    }

    getUserWatchedMovies(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_user_movie_track_data_by_userid/`+id)
    }

    getUserNotRatedMovies(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`no_movie_rating_by_userid/`+id)
    }

    getUserRatedMovies(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_user_movie_rating_by_userid/`+id)
    }

    deleteUserRatedMovie(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`delete_movie_rating_data`, obj, {headers: headers})
    }

    updateUserMovieRating(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`update_movie_rating_data`, obj, {headers: headers})
    }

    getGetAllMovieData(){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_all_movie_data`)
    }

    getMovieDataById(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_movie_data_by_id/`+id);
    }

    deleteMovieById(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`delete_movie_details_by_admin`, obj, {headers: headers})
    }

    updateMovie(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`update_movie`, obj, {headers: headers})
    }

    addMovie(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`add_movie`, obj, {headers: headers})
    }

    getAllArtist(){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_all_artist_details`)
    }

    getArtistById(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_artist_details_by_id/`+id)
    }

    addArtist(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`add_artist`, obj, {headers: headers})
    }

    updateArtist(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`update_artist`, obj, {headers: headers})
    }

    deleteArtist(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`delete_artist_details_by_admin`, obj, {headers: headers})
    }

    addSubMovie(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`add_sub_movie_data`, obj, {headers: headers})
    }

    updateSubMovie(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`update_sub_movie_data`, obj, {headers: headers})
    }

    deleteSubMovie(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`delete_sub_movie_details_by_admin`, obj, {headers: headers})
    }

    getSubMovieById(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_sub_movie_data_by_id/`+id)
    }

    getAllSubMovie(){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_all_sub_movie_data`)
    }

    getAllMovieCategory(){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_movie_category`)
    }

    getAllMovieRating(){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_all_movie_rating_data`)
    }

    getSuggestedMovies(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`get_suggest_movies_userid`, obj, {headers: headers})
    }

    getAllArtistMovieData(){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_all_artist_movie_data`)
    }

    getArtistMovieDataById(id){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_artist_movie_data_by_id/`+id)
    }

    addArtistMovieData(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`add_artist_movie`, obj, {headers: headers})
    }

    updateArtistMovieData(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`update_artist_movie`, obj, {headers: headers})
    }

    deleteArtistMovieData(obj){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.post<any>(this.baseUrl+`delete_artist_movie`, obj, {headers: headers})
    }

    getAllArtistType(){
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:8000',
            'Access-Control-Allow-Headers': 'X-Requested-With, Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
          });
          return this.http.get<any>(this.baseUrl+`get_artist_type`)
    }
}