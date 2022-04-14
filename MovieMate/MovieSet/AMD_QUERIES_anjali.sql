____________________________________________________________________________________________________________________________________
Actual AMD PRoject Queires and tables 
____________________________________________________________________________________________________________________________________
#RegsiterUser function


create or replace function RegisterUser(uid integer, fn varchar, ln varchar, dob varchar, gndr varchar, ph varchar, em varchar, addr varchar ,cty varchar, pass varchar, ut varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."user_data" ("user_id","user_first_name","user_last_name","user_dob","user_gender","user_contact_number","user_email","user_address",
"user_city","user_password","user_type")
VALUES(uid ,fn, ln, dob, gndr, ph, em, addr, cty, pass, ut);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql


#query
select  RegisterUser(
cast('2' as integer),
cast('Ganesh' as varchar),
cast('Chile' as varchar),
cast('03.07.1996' as varchar),
cast('Male' as varchar),
cast('+491745344802' as varchar),
cast('ganeshchile3@gmail.com' as varchar),
cast('Germany' as varchar),
cast('Chemnitz' as varchar),
cast('Ganu@123' as varchar),
cast('admin' as varchar));
________________________________________________________________________________________________________________________________________________

#LoginUser Query


create or replace function LoginUser( un varchar, pass varchar ) returns varchar(255) as $$
declare
passwrd varchar(255);

begin

SELECT 	user_password INTO passwrd FROM "public"."user_data" WHERE "user_email" = un ;
if passwrd = pass then
return 'True';
else return 'False';
end if;
end;
$$ language plpgsql

select LoginUser('ganeshchile3@gmail.com','Ganu@123');


____________________________________________________________________________________________________________________________________
#UserType

create or replace function LoginUserType( un varchar  ) returns  varchar(100) as $$
declare
urtyp varchar(255);
begin

SELECT user_type into urtyp FROM "public"."user_data" WHERE "user_email" = usr;
return urtyp;
end;
$$ language plpgsql

select LoginUserType('ganeshchile3@gmail.com');

____________________________________________________________________________________________________________________________________
SELECT max("user_id") + 1 FROM "public"."user_data"  ;

create or replace function getmaxuserdataid() returns integer as $$
declare
uid integer;

begin

SELECT max("user_id") + 1 into uid FROM "public"."user_data" ;
return uid;
end;


$$ language plpgsql


______________________________________________________________________________________________________________________
add_artist

create or replace function add_artist(uid integer, fn varchar, ln varchar, dob varchar, gndr varchar, ph varchar, em varchar, addr varchar ,cty varchar, crty varchar, desrp varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."artist data" ("artist_id","artist_first_name",
"artist_last_name","artist_dob","artist_gender","artist_contact_number","artist_email","artist_address","artist_city",
"artist_country","artist_description")
VALUES(uid ,fn, ln, dob, gndr, ph, em, addr, cty, crty, desrp);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql


create or replace function add_artist(uid integer, fn varchar, ln varchar, dob varchar, gndr varchar, ph varchar, em varchar, addr varchar ,cty varchar, crty varchar, desrp varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."artist data" ("artist_id","artist_first_name",
"artist_last_name","artist_dob","artist_gender","artist_contact_number","artist_email","artist_address","artist_city",
"artist_country","artist_description")
VALUES(uid ,fn, ln, dob, gndr, ph, em, addr, cty, crty, desrp);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return EXCEPTION ;

end;
$$ language plpgsql


select  add_artist(
cast('6' as integer),
cast('Hritik' as varchar),
cast('Roshan' as varchar),
cast('07.02.1996' as varchar),
cast('Male' as varchar),
cast('+491745344802' as varchar),
cast('HRx3@gmail.com' as varchar),
cast('Bandra' as varchar),
cast('Mumbai' as varchar),
cast('India' as varchar),
cast('Good dancer and actor' as varchar));


____________________________________________________________________________________________________________________________________
#getmaxartistdataid

create or replace function getmaxartistdataid() returns integer as $$
declare
uid integer;

begin

SELECT max("artist_id") + 1 into uid FROM "public"."artist_data" ;
return uid;
end;


$$ language plpgsql

select getmaxartistdataid();


____________________________________________________________________________________________________________________________________
getartist data by id
____________________________________________________________________________________________________________________________________
Actual AMD PRoject Queires and tables 
____________________________________________________________________________________________________________________________________
#RegsiterUser function


create or replace function RegisterUser(uid integer, fn varchar, ln varchar, dob varchar, gndr varchar, ph varchar, em varchar, addr varchar ,cty varchar, pass varchar, ut varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."user_data" ("user_id","user_first_name","user_last_name","user_dob","user_gender","user_contact_number","user_email","user_address",
"user_city","user_password","user_type")
VALUES(uid ,fn, ln, dob, gndr, ph, em, addr, cty, pass, ut);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql


#query
select  RegisterUser(
cast('2' as integer),
cast('Ganesh' as varchar),
cast('Chile' as varchar),
cast('03.07.1996' as varchar),
cast('Male' as varchar),
cast('+491745344802' as varchar),
cast('ganeshchile3@gmail.com' as varchar),
cast('Germany' as varchar),
cast('Chemnitz' as varchar),
cast('Ganu@123' as varchar),
cast('admin' as varchar));
________________________________________________________________________________________________________________________________________________

#LoginUser Query


create or replace function LoginUser( un varchar, pass varchar ) returns varchar(255) as $$
declare
passwrd varchar(255);

begin

SELECT 	user_password INTO passwrd FROM "public"."user_data" WHERE "user_email" = un ;
if passwrd = pass then
return 'True';
else return 'False';
end if;
end;
$$ language plpgsql

select LoginUser('ganeshchile3@gmail.com','Ganu@123');


____________________________________________________________________________________________________________________________________
#UserType

create or replace function LoginUserType( un varchar  ) returns  varchar(100) as $$
declare
urtyp varchar(255);
begin

SELECT user_type into urtyp FROM "public"."user_data" WHERE "user_email" = usr;
return urtyp;
end;
$$ language plpgsql

select LoginUserType('ganeshchile3@gmail.com');

____________________________________________________________________________________________________________________________________
SELECT max("user_id") + 1 FROM "public"."user_data"  ;

create or replace function getmaxuserdataid() returns integer as $$
declare
uid integer;

begin

SELECT max("user_id") + 1 into uid FROM "public"."user_data" ;
return uid;
end;


$$ language plpgsql


______________________________________________________________________________________________________________________
add_artist

create or replace function add_artist(uid integer, fn varchar, ln varchar, dob varchar, gndr varchar, ph varchar, em varchar, addr varchar ,cty varchar, crty varchar, desrp varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."artist_data" ("artist_id","artist_first_name",
"artist_last_name","artist_dob","artist_gender","artist_contact_number","artist_email","artist_address","artist_city",
"artist_country","artist_description")
VALUES(uid ,fn, ln, dob, gndr, ph, em, addr, cty, crty, desrp);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql


create or replace function add_artist(uid integer, fn varchar, ln varchar, dob varchar, gndr varchar, ph varchar, em varchar, addr varchar ,cty varchar, crty varchar, desrp varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."artist_data" ("artist_id","artist_first_name",
"artist_last_name","artist_dob","artist_gender","artist_contact_number","artist_email","artist_address","artist_city",
"artist_country","artist_description")
VALUES(uid ,fn, ln, dob, gndr, ph, em, addr, cty, crty, desrp);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return EXCEPTION ;

end;
$$ language plpgsql


select  add_artist(
cast('6' as integer),
cast('Hritik' as varchar),
cast('Roshan' as varchar),
cast('07.02.1996' as varchar),
cast('Male' as varchar),
cast('+491745344802' as varchar),
cast('HRx3@gmail.com' as varchar),
cast('Bandra' as varchar),
cast('Mumbai' as varchar),
cast('India' as varchar),
cast('Good dancer and actor' as varchar));


____________________________________________________________________________________________________________________________________
#getmaxartistdataid

create or replace function getmaxartistdataid() returns integer as $$
declare
uid integer;

begin

SELECT max("artist_id") + 1 into uid FROM "public"."artist_data" ;
return uid;
end;


$$ language plpgsql

select getmaxartistdataid();


____________________________________________________________________________________________________________________________________
getartist data by id

create or replace function getartistdetailsbyid(aid integer) returns record as $$
declare
artis_details record ;

begin

SELECT * FROM into artis_details "public"."artist_data" WHERE "artist_id" = aid ;
return artis_details ;
end;


$$ language plpgsql

select  getartistdetailsbyid(cast('1' as integer));

____________________________________________________________________________________________________________________________________
update artist data 

create or replace function updateartistdata(aid integer, fn varchar, ln varchar, dob varchar, gndr varchar, ph varchar, em varchar, addr varchar ,cty varchar, crty varchar, desrp varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
update "public"."artist_data" set "artist_first_name" = fn,
"artist_last_name" = ln, "artist_dob" = dob, "artist_gender" = gndr, "artist_contact_number" = ph,
"artist_email" = em, "artist_address" = addr, "artist_city" = cty, "artist_country" = crty, "artist_description" = desrp 
where "artist_id" = aid ;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return EXCEPTION ;

end;
$$ language plpgsql

____________________________________________________________________________________________________________________________________
delete artist data

create or replace function deleteartistdatabyid(aid integer) returns varchar as $$
declare
status varchar;
begin
status='False';

DELETE FROM "public"."artist_data" WHERE "artist_id" = aid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql


select deleteartistdatabyid(6);

------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------

add movie data 

create or replace function add_movie(mid integer, mn varchar, desrp varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."movie_data" ("movie_id","movie_name","movie_description")
VALUES(mid, mn, desrp);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql

select  add_movie(
cast('11' as integer),
cast('Movie Test 1' as varchar),
cast('NA' as varchar));


------------------------------------------------------------------------------------------------------------

update movie data 

create or replace function updatemovie(mid integer, mn varchar, desrp varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
update "public"."movie_data" set "movie_name" = mn, "movie_description" = desrp 
where "movie_id" = mid ;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return EXCEPTION ;

end;
$$ language plpgsql

select  updatemovie(
cast('11' as integer),
cast('Movie Test 1' as varchar),
cast('NA' as varchar));

------------------------------------------------------------------------------------------------------------
get max movie id 

create or replace function getmaxmovieid() returns integer as $$
declare
mid integer;

begin

SELECT max("movie_id") + 1 into mid FROM "public"."movie_data" ;
return mid;
end;


$$ language plpgsql

select getmaxmovieid();

-----------------------------------------------------------------------------------------------------
get movie data by id

create or replace function getmoviedatabyid(mid integer) returns record as $$
declare
movie_data record ;

begin

SELECT * FROM into movie_data "public"."movie_data" WHERE "movie_id" = mid ;
return movie_data ;
end;


$$ language plpgsql

select  getmoviedatabyid(cast('1' as integer));

--------------------------------------------------------------------------------------------------------
delete movie data by id 

create or replace function deletemoviedatabyid(mid integer) returns varchar as $$
declare
status varchar;
begin
status='False';

DELETE FROM "public"."movie_data" WHERE "movie_id" = mid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql


select deletemoviedatabyid(11);

-------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------

add artist movie data 

create or replace function add_artist_movie(amid integer, mid integer, aid integer, artisttype varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."artist_movie_data" ("artist_movie_id","sub_movie_id","artist_id","artist_type")
VALUES(amid, mid, aid, artisttype);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql

select  add_artist_movie(
cast('23' as integer),
cast('1' as integer),
cast('1' as integer),
cast('Actor' as varchar));

----------------------------------------------------------------------------------------------------------
get max artist movie id 

create or replace function getmaxartistmovieid() returns integer as $$
declare
amid integer;

begin

SELECT max("artist_movie_id") + 1 into amid FROM "public"."artist_movie_data" ;
return amid;
end;


$$ language plpgsql

select getmaxartistmovieid();

--------------------------------------------------------------------------------------------------------

update artist movie data 

create or replace function updateartistmovie(amid integer, mid integer, aid integer, artisttype varchar) returns varchar as $$
declare
status varchar;
begin
status='False';
update "public"."artist_movie_data" set "sub_movie_id" = mn, "artist_id" = aid, "artist_type" = artisttype 
where "artist_movie_id" = amid ;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return EXCEPTION ;

end;
$$ language plpgsql

select  updateartistmovie(
cast('23' as integer),
cast('2' as integer),
cast('2' as integer),
cast('Actor, Director' as varchar));

------------------------------------------------------------------------------------------------------------

delete artist movie data by id 

create or replace function deleteartistmoviedatabyid(amid integer) returns varchar as $$
declare
status varchar;
begin
status='False';

DELETE FROM "public"."artist_movie_data" WHERE "artist_movie_id" = amid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql


select deleteartistmoviedatabyid(11);

-------------------------------------------------------------------------------------------------------------
get artist movie data by id

create or replace function getartistmoviedatabyid(amid integer) returns record as $$
declare
artist_movie_data record ;

begin

SELECT * FROM into artist_movie_data "public"."artist_movie_data" WHERE "artist_movie_id" = amid ;
return artist_movie_data ;
end;


$$ language plpgsql

select  getartistmoviedatabyid(cast('1' as integer));


CREATE TYPE getartistmoviedatatype AS (amid integer, smid integer,  aid intege , atype varchar);

----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------


