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

____________________________________________________________________________________________________________________________________
get user by id

create or replace function getuserdetailsbyid( uid integer) returns record as $$
declare
user_details record ;

begin

SELECT * FROM into user_details "public"."user_data" WHERE "user_id" = uid;
return user_details ;
end;

$$ language plpgsql

select getuserdetailsbyid(2);
____________________________________________________________________________________________________________________________________
by email

create or replace function getuserdetailsby_email( email varchar) returns record as $$
declare
user_details record ;

begin

SELECT * FROM into user_details "public"."user_data" WHERE "user_email" = email;
return user_details ;
end;

$$ language plpgsql

select getuserdetailsby_email('ganeshchile3@gmail.com');



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



____________________________________________________________________________________________________________________________________
#user_movie_track_data
getmaxid

create or replace function get_user_movie_track_data_id() returns integer as $$
declare
uid integer;

begin

SELECT max("user_movie_track_id") + 1 into uid FROM "public"."user_movie_track_data" ;
return uid;
end;


$$ language plpgsql

select get_user_movie_track_data_id() ;
________________________________________________________________________________________________________________________________

#add
create or replace function add_movie_track_data(mtdid integer, uid integer, smid integer) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."user_movie_track_data" ("user_movie_track_id", "user_id", "sub_movie_id") VALUES(mtdid, uid, smid);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False'; 
return status ;

end;
$$ language plpgsql

select add_movie_track_data(46 , 6,8)

____________________________________________________________________________________________________________________________________
#get_details_by_id
create or replace function get_movie_track_data_by_id( umti integer) returns record as $$
declare
track_details record ;

begin

SELECT * FROM into track_details "public"."user_movie_track_data" WHERE "user_movie_track_id" = umti;
return track_details;
end;


$$ language plpgsql

select get_movie_track_data_by_id (46)


____________________________________________________________________________________________________________________________________
delete movie track data
create or replace function delete_movie_track_data(umtid integer) returns varchar as $$
declare
status varchar;
begin
status='False';

DELETE FROM "public"."user_movie_track_data" WHERE "user_movie_track_id" = umtid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql

select delete_movie_track_data(46)

____________________________________________________________________________________________________________________________________
#update


create or replace function updat_user_movie_track_data(umtdid integer, uid integer, smid integer,) returns varchar as $$
declare
status varchar;
begin
status='False';
update "public"."user_movie_track_data" set "user_id" = uid, "sub_movie_id" = smid where "user_movie_track_id" = umtid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql

____________________________________________________________________________________________________________________________________

#rating
create or replace function get_max_user_movie_rating_data_id() returns integer as $$
declare
umrid integer;

begin

SELECT max("user_movie_rating_id") + 1 into umrid FROM "public"."user_movie_rating_data";
return umrid;
end;


$$ language plpgsql

select get_max_user_movie_rating_data_id()

____________________________________________________________________________________________________________________________________
add rating


create or replace function add_movie_rating_data(mrdid integer, uid integer, smid integer , umr integer) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."user_movie_rating_data"("user_movie_rating_id", "user_id", "sub_movie_id" , "user_movie_rating") VALUES(mrdid, uid, smid, umr);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;


end;
$$ language plpgsql

select add_movie_rating_data(45,7,7,7)

__________________________________________________________________________________________________________________________________


create or replace function get_movie_rating_data_by_id( umrid integer) returns record as $$
declare
rating_details record ;

begin

SELECT * FROM into rating_details "public"."user_movie_rating_data" WHERE "user_movie_rating_id" = umrid;
return rating_details;
end;


$$ language plpgsql

select get_movie_rating_data_by_id(45)

____________________________________________________________________________________________________________________________________

create or replace function delete_movie_rating_data(umrid integer) returns varchar as $$
declare
status varchar;
begin
status='False';

DELETE FROM "public"."user_movie_rating_data" WHERE "user_movie_rating_id" = umrid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql

select delete_movie_rating_data(45)

____________________________________________________________________________________________________________________________________


create or replace function update_movie_rating_data(umrid integer, uid integer, smid integer,umr integer) returns varchar as $$
declare
status varchar;
begin
status='False';
update "public"."user_movie_rating_data" set "user_id" = uid, "sub_movie_id" = smid  , "user_movie_rating" = umr 
where "user_movie_rating_id" = umrid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql

select update_movie_rating_data(45,7,7,6)

___________________________________________________________________________________________________________________________________

sub_movie
max id
create or replace function get_max_sub_movie_rating_data_id() returns integer as $$
declare
uid integer;

begin

SELECT max("sub_movie_rating_id") + 1 into uid FROM "public"."sub_movie_rating_data" ;
return uid;
end;


$$ language plpgsql

select get_max_sub_movie_rating_data_id();

____________________________________________________________________________________________________________________________________

add sub movies
create or replace function add_sub_movie_rating_data(smrid integer, smid integer , smr integer) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."sub_movie_rating_data"("sub_movie_rating_id", "sub_movie_id" , "sub_movie_rating") VALUES(smrid, smid, smr);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;


end;
$$ language plpgsql

select add_sub_movie_rating_data(15,14,3)  ;

____________________________________________________________________________________________________________________________________

getby id

create or replace function get_sub_movie_rating_data_by_id( smrid integer) returns record as $$
declare
sub_rating_details record ;

begin

SELECT * FROM into sub_rating_details "public"."sub_movie_rating_data" WHERE "sub_movie_rating_id" = smrid;
return sub_rating_details;
end;


$$ language plpgsql

select get_sub_movie_rating_data_by_id(15)  ;

____________________________________________________________________________________________________________________________________
delete sub 

create or replace function delete_sub_movie_rating_data(smrid integer) returns varchar as $$
declare
status varchar;
begin
status='False';

DELETE FROM "public"."sub_movie_rating_data" WHERE "sub_movie_rating_id" = smrid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql

select delete_sub_movie_rating_data(15)  ;

____________________________________________________________________________________________________________________________________
update sub

create or replace function update_sub_movie_rating_data(smrid integer,  smid integer, smr integer) returns varchar as $$
declare
status varchar;
begin
status='False';
update "public"."sub_movie_rating_data" set  "sub_movie_id" = smid  , "sub_movie_rating" = smr 
where "sub_movie_rating_id" = smrid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql

select update_sub_movie_rating_data(15,14,4)  ;


__________________________________________________________________________________


create or replace function get_max_sub_movie_data_id() returns integer as $$
declare
uid integer;

begin

SELECT max("sub_movie_id") + 1 into uid FROM "public"."sub_movie_data";
return uid;
end;


$$ language plpgsql

select get_max_sub_movie_data_id()  ;

___________________________________________________

add sub_movie

create or replace function add_sub_movie_data(smid integer, sub_name varchar, mv_id integer, sub_mov_descrp varchar, sub_mv_categ varchar, sub_mv_sq_num integer) returns varchar as $$
declare
status varchar;
begin
status='False';
INSERT INTO "public"."sub_movie_data"("sub_movie_id","sub_movie_name","movie_id","sub_movie_description","sub_movie_category","sub_movie_sequel_number")
VALUES(smid, sub_name, mv_id , sub_mov_descrp , sub_mv_categ , sub_mv_sq_num);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql


select  add_sub_movie_data(
cast('15' as integer),
cast('Ganesh' as varchar),
cast('10' as integer),
cast('woww' as varchar),
cast('sexyy' as varchar),
cast('2' as integer));

____________________________________________________________________________________________________________________________________

get sub movie by id

create or replace function get_sub_movie_data_by_id( smid integer) returns record as $$
declare
sub_movie_details record ;

begin

SELECT * FROM into sub_movie_details "public"."sub_movie_data" WHERE "sub_movie_id" = smid;
return sub_movie_details ;
end;

$$ language plpgsql

select  get_sub_movie_data_by_id(15);

____________________________________________________________________________________________________________________________________
deleet sub movie data


create or replace function delete_sub_movie_data(smid integer) returns varchar as $$
declare
status varchar;
begin
status='False';

DELETE FROM "public"."sub_movie_data" WHERE "sub_movie_id" = smid;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status;

end;
$$ language plpgsql


select  delete_sub_movie_data(15);


____________________________________________________________________________________________________________________________________

update


create or replace function update_sub_movie_data(smid integer, sub_name varchar, mv_id integer, sub_mov_descrp varchar, sub_mv_categ varchar, sub_mv_sq_num integer) returns varchar as $$
declare
status varchar;
begin
status='False';
update "public"."sub_movie_data" set "sub_movie_name" = sub_name ,
"movie_id" = mv_id , "sub_movie_description" = sub_mov_descrp , "sub_movie_category" = sub_mv_categ , 
"sub_movie_sequel_number" = sub_mv_sq_num where "sub_movie_id" = smid ;
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return EXCEPTION ;

end;
$$ language plpgsql

select  update_sub_movie_data(
cast('15' as integer),
cast('ganesh' as varchar),
cast('10' as integer),
cast('woww' as varchar),
cast('sexyy' as varchar),
cast('2' as integer));


____________________________________________________________________________________________________________________________________
select distinct
"user_movie_track_data"."user_id",
"sub_movie_data"."movie_id", 
"sub_movie_data"."sub_movie_name" 
from "public"."sub_movie_data" 
JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = 4 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id")


____________________________________________________________________________________________________________________________________
#get user movie trackd data based on user id

create or replace function get_user_movie_track_data_by_userid( smrid integer) returns record as $$
declare
user_movie_details record ;
begin
select distinct
"user_movie_track_data"."user_id",
"sub_movie_data"."movie_id", 
"sub_movie_data"."sub_movie_name" 
from "public"."sub_movie_data"  
into  user_movie_details
JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = 4 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id")
return user_movie_details;

end;
$$ language plpgsql


CREATE OR REPLACE FUNCTION get_user_movie_track_data_by_userid(uid integer) RETURNS TABLE(ui integer, smd integer, smn varchar) AS $$
    BEGIN
    RETURN QUERY select distinct
"user_movie_track_data"."user_id",
"sub_movie_data"."movie_id", 
"sub_movie_data"."sub_movie_name" 
from "public"."sub_movie_data"  
JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = uid 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id");
    END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_user_movie_track_data_by_userid(uid integer) RETURNS TABLE(umtid integer,
ui integer, smd integer, smn varchar) AS $$
    BEGIN
    RETURN QUERY select distinct
"user_movie_track_data"."user_movie_track_id",
"user_movie_track_data"."user_id",
"sub_movie_data"."movie_id", 
"sub_movie_data"."sub_movie_name" 
from "public"."sub_movie_data"  
JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = uid 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id");
    END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_user_movie_track_data_by_userid(uid integer) RETURNS TABLE(umtid integer,
ui integer, smd integer, smn varchar) AS $$
    BEGIN
    RETURN QUERY select distinct
"user_movie_track_data"."user_movie_track_id",
"user_movie_track_data"."user_id",
"sub_movie_data"."sub_movie_id", 
"sub_movie_data"."sub_movie_name",
"sub_movie_data"."sub_movie_category"
from "public"."sub_movie_data"  
JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = uid 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id");
    END;
$$ LANGUAGE plpgsql;

select * from get_user_movie_track_data_by_userid(7);
____________________________________________________________________________________________________________________________________
not watched
CREATE OR REPLACE FUNCTION movie_not_watch_by_user(uid integer) RETURNS TABLE(smd integer, 
smn varchar) AS $$
    BEGIN
    RETURN QUERY select 
"sub_movie_data"."movie_id", 
"sub_movie_data"."sub_movie_name" 
from "public"."sub_movie_data"  
left JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = uid 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id")
where "public"."user_movie_track_data"."sub_movie_id" is NULL ;
    END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION movie_not_watch_by_user(uid integer) RETURNS TABLE(smd integer, 
smn varchar , mvtyp varchar) AS $$
    BEGIN
    RETURN QUERY select 
"sub_movie_data"."movie_id", 
"sub_movie_data"."sub_movie_name" , 
"sub_movie_data"."sub_movie_category" 
from "public"."sub_movie_data"  
left JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = uid 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id")
where "public"."user_movie_track_data"."sub_movie_id" is NULL ;
    END;
$$ LANGUAGE plpgsql;


____________________________________________________________________________________________________________________________________
get user rating by userid

CREATE OR REPLACE FUNCTION get_user_movie_rating_by_userid(uid integer) RETURNS TABLE(umrid integer,
 smd integer, smn varchar , umr numeric, sm_cat varchar) AS $$
    BEGIN
    RETURN QUERY select distinct
"user_movie_rating_data"."user_movie_rating_id",
"user_movie_rating_data"."sub_movie_id",
"sub_movie_data"."sub_movie_name", 
"user_movie_rating_data"."user_movie_rating",
"sub_movie_data"."sub_movie_category"
from "public"."sub_movie_data"  
JOIN 
"public"."user_movie_rating_data" 
on ("public"."user_movie_rating_data"."user_id" = uid 
AND 
    "public"."user_movie_rating_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id");
    END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION no_movie_rating_by_userid(uid integer) RETURNS TABLE(
 smd integer, smn varchar ,sm_cat varchar) AS $$
    BEGIN
    RETURN QUERY select 
"user_movie_rating_data"."sub_movie_id",
"sub_movie_data"."sub_movie_name", 
"sub_movie_data"."sub_movie_category"
from "public"."sub_movie_data"  
LEFT JOIN 
"public"."user_movie_rating_data" 
on ("public"."user_movie_rating_data"."user_id" = uid 
AND 
"public"."user_movie_rating_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id")
where "public"."user_movie_rating_data"."sub_movie_id" is NULL;
   END;
$$ LANGUAGE plpgsql;


____________________________________________________________________________________________________________________________________
suggest movies

select  sub_movie_data.sub_movie_id ,sub_movie_data.sub_movie_name from sub_movie_data where sub_movie_data.sub_movie_id NOT in 
(
select distinct "sub_movie_data"."sub_movie_id"
from "public"."sub_movie_data"  
JOIN 
"public"."user_movie_track_data" 
on ("public"."user_movie_track_data"."user_id" = 8 
AND 
"public"."user_movie_track_data"."sub_movie_id" = "public"."sub_movie_data"."sub_movie_id")
)
AND string_to_array(sub_movie_category ,',') && array['Thriller'];



____________________________________________________________________________________________________________________________________

cascade delete

alter table artist_movie_data
drop constraint artist_movie_datafkey;

alter table artist_movie_data
add constraint artist_movie_datafkey
foreign key (artist_id)
references artist_data(	artist_id)
on delete cascade;
ON DELETE SET NULL

delete from artist_data where artist_id = 11;
______________________________________________

alter table sub_movie_data
drop constraint sub_movie_datafkey;

alter table sub_movie_data
add constraint sub_movie_datafkey
foreign key (movie_id)
references movie_data(movie_id)
on delete cascade;
ON DELETE SET NULL

delete from movie_data where movie_id = 11;


____________________________________________________________________________________________________________________________________
 delete from sub_movie_data where sub_movie_id = (select sub_movie_id from artist_movie_data 
where artist_id = 11 )


____________________________________________________________________________________________________________________________________
test Queires

deleting 3rd table based on id
select distinct contacts.contact_id 
FROM contacts
join
customers
on
contacts.customer_id= customers.customer_id
where customers.customer_id = 3;

DELETE from location WHERE contact_id IN (3);
DELETE from contacts WHERE contact_id IN (3);
DELETE from customers where customer_id = 3;

SELECT location.location_id
FROM location
INNER JOIN contacts ON location.contact_id = contacts.contact_id
LEFT OUTER JOIN customers on customers.customer_id=contacts.customer_id
where customers.customer_id = 3;

SELECT distinct *
FROM sub_movie_data
 left join artist_movie_data ON artist_movie_data.sub_movie_id= sub_movie_data.sub_movie_id
 LEFT  JOIN artist_data on artist_data.artist_id=artist_data.artist_id 
 where artist_data.artist_id = 11


 two tables artist and atist data

select distinct artist_movie_data.sub_movie_id
FROM artist_movie_data
join
artist_data
on
artist_data.artist_id= artist_movie_data.artist_id
where artist_data.artist_id = 11;


DELETE from artist_movie_data WHERE sub_movie_id IN (15);
DELETE from user_movie_track_data WHERE sub_movie_id IN (15);
DELETE from user_movie_rating_data WHERE sub_movie_id IN (15);
DELETE from sub_movie_rating_data WHERE sub_movie_id IN (15);
DELETE from sub_movie_data WHERE sub_movie_id IN (15);
DELETE from artist_data WHERE artist_id IN (11);


CREATE OR REPLACE FUNCTION get_movieid_based_atist_id(aid integer) RETURNS TABLE(smid integer) AS $$
    BEGIN
    RETURN QUERY select distinct artist_movie_data.sub_movie_id
FROM artist_movie_data
join
artist_data
on
artist_data.artist_id= artist_movie_data.artist_id
where artist_data.artist_id = aid ;
    END;
$$ LANGUAGE plpgsql;

cur.execute("DELETE from artist_movie_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
cur.execute("DELETE from user_movie_track_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
cur.execute("DELETE from user_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
cur.execute("DELETE from sub_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
cur.execute("DELETE from sub_movie_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
cur.execute("DELETE from artist_data WHERE artist_id IN (cast(%s as integer));",(aid,))


____________________________________________________________________________________________________________________________________

delete movie data based on admin

select distinct sub_movie_data.sub_movie_id
FROM sub_movie_data
join
movie_data
on
sub_movie_data.movie_id= movie_data.movie_id
where sub_movie_data.movie_id = 11;


CREATE OR REPLACE FUNCTION delete_movie_data_based_admin(mvid integer) RETURNS TABLE(smid integer) AS $$
    BEGIN
    RETURN QUERY select distinct sub_movie_data.sub_movie_id
FROM sub_movie_data
join
movie_data
on
sub_movie_data.movie_id= movie_data.movie_id
where sub_movie_data.movie_id = 11;
   END;
$$ LANGUAGE plpgsql;


user_movie_rating data
sub_movie_rating data
artist_movie_data
user_movie_track_data   
sub movie data


DELETE from sub_movie_data WHERE sub_movie_id IN (16 );


____________________________________________________________________________________________________________________________________
average
select sub_movie_id , round(avg(user_movie_rating),0) from user_movie_rating_data group by sub_movie_id;


WITH umrd AS (
    SELECT distinct sub_movie_id , avg(user_movie_rating) as average
    FROM user_movie_rating_data group by sub_movie_id
)
UPDATE sub_movie_rating_data  smrd
SET sub_movie_rating = umrd.average
FROM umrd 



UPDATE sub_movie_rating_data
   SET sub_movie_rating =(select  round(avg(user_movie_rating),0) as sub_movie_rating from user_movie_rating_data  where sub_movie_rating_data.sub_movie_id = user_movie_rating_data.sub_movie_id 
group by sub_movie_id order by sub_movie_id);

create or replace function update_avg_sub_movie_rating() returns varchar as $$
declare
status varchar;
begin
UPDATE sub_movie_rating_data
   SET sub_movie_rating =(select  round(avg(user_movie_rating),0) as sub_movie_rating from user_movie_rating_data  where sub_movie_rating_data.sub_movie_id = user_movie_rating_data.sub_movie_id 
group by sub_movie_id order by sub_movie_id);
status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql

____________________________________________________________________________________________________________________________________

get all rating movie data
select 
movie_data.movie_id ,
movie_data.movie_name,
movie_data.movie_description ,
sub_movie_data.sub_movie_id ,
sub_movie_data.sub_movie_name , 
sub_movie_data.sub_movie_description ,
sub_movie_data.sub_movie_category ,
sub_movie_data.sub_movie_sequel_number ,
sub_movie_rating_data.sub_movie_rating 
from sub_movie_data 
join  sub_movie_rating_data on (sub_movie_rating_data.sub_movie_id = sub_movie_data.sub_movie_id)
join  movie_data on (sub_movie_data .movie_id = movie_data.movie_id);


get all rating movie data
select 
movie_data.movie_id ,
movie_data.movie_name,
movie_data.movie_description ,
sub_movie_data.sub_movie_id ,
sub_movie_data.sub_movie_name , 
sub_movie_data.sub_movie_description ,
sub_movie_data.sub_movie_category ,
sub_movie_data.sub_movie_sequel_number ,
sub_movie_rating_data.sub_movie_rating ,
artist_data.artist_first_name ,
artist_data.artist_last_name 
from sub_movie_data 
join  sub_movie_rating_data on (sub_movie_rating_data.sub_movie_id = sub_movie_data.sub_movie_id)
join  movie_data on (sub_movie_data.movie_id = movie_data.movie_id)
join artist_movie_data on (artist_movie_data.sub_movie_id = sub_movie_data.sub_movie_id) 
join artist_data on (artist_movie_data.artist_id= artist_data.artist_id) ;
____________________________________________________________________________________________________________________________________

get_sub_movie_data_by_id along with movie name in it


select 
movie_data.movie_name ,
sub_movie_data.sub_movie_id , 
sub_movie_data.sub_movie_name ,
sub_movie_data.sub_movie_description ,
sub_movie_data.sub_movie_category,
sub_movie_data.sub_movie_sequel_number
from sub_movie_data 
JOIN 
movie_data
on
(movie_data.movie_id = sub_movie_data.movie_id) 
where 
sub_movie_data.sub_movie_id = 1;

CREATE OR REPLACE FUNCTION get_sub_movie_data_by__id(smid integer) RETURNS TABLE(
 mvn varchar , smd integer, smn varchar ,sm_descp varchar ,sm_cat varchar, sm_sq integer) AS $$
    BEGIN
    RETURN QUERY select 
movie_data.movie_name ,
sub_movie_data.sub_movie_id , 
sub_movie_data.sub_movie_name ,
sub_movie_data.sub_movie_description ,
sub_movie_data.sub_movie_category,
sub_movie_data.sub_movie_sequel_number
from sub_movie_data 
JOIN 
movie_data
on
(movie_data.movie_id = sub_movie_data.movie_id) 
where 
sub_movie_data.sub_movie_id = smid;
   END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_sub_movie_data_by___id(smid integer) RETURNS TABLE(mid integer,
 mvn varchar , smd integer, smn varchar ,sm_descp varchar ,sm_cat varchar, sm_sq integer) AS $$
    BEGIN
    RETURN QUERY select 
movie_data.movie_id ,
movie_data.movie_name ,
sub_movie_data.sub_movie_id , 
sub_movie_data.sub_movie_name ,
sub_movie_data.sub_movie_description ,
sub_movie_data.sub_movie_category,
sub_movie_data.sub_movie_sequel_number
from sub_movie_data 
JOIN 
movie_data
on
(movie_data.movie_id = sub_movie_data.movie_id) 
where 
sub_movie_data.sub_movie_id = smid;
   END;
$$ LANGUAGE plpgsql;

____________________________________________________________________________________________

select sub_movie_data.* ,
movie_data.movie_name ,
movie_data.movie_description
FROM sub_movie_data
left join
movie_data
on
sub_movie_data.movie_id= movie_data.movie_id


____________________________________________________________________________________________________________________________________
get all movie artist data 

select 
artist_data.artist_id,
artist_data.artist_first_name,
artist_data.artist_last_name ,
artist_movie_data.artist_movie_id ,
artist_movie_data.artist_type,	
sub_movie_data.sub_movie_id ,
sub_movie_data.sub_movie_name , 
sub_movie_data.sub_movie_description ,
sub_movie_data.sub_movie_category ,
sub_movie_data.sub_movie_sequel_number  
from sub_movie_data 
join artist_movie_data on (artist_movie_data.sub_movie_id = sub_movie_data.sub_movie_id) 
join artist_data on (artist_movie_data.artist_id= artist_data.artist_id);



CREATE OR REPLACE FUNCTION get_all_artist__movie_data() RETURNS TABLE(aid integer,
 afn varchar, aln varchar , amid integer , amtype varchar , smid integer , smn varchar , sm_decrp varchar ,
sm_categ varchar , sub_seq integer) AS $$
    BEGIN
    RETURN QUERY select 
artist_data.artist_id,
artist_data.artist_first_name,
artist_data.artist_last_name ,
artist_movie_data.artist_movie_id ,
artist_movie_data.artist_type,	
sub_movie_data.sub_movie_id ,
sub_movie_data.sub_movie_name , 
sub_movie_data.sub_movie_description ,
sub_movie_data.sub_movie_category ,
sub_movie_data.sub_movie_sequel_number  
from sub_movie_data 
join artist_movie_data on (artist_movie_data.sub_movie_id = sub_movie_data.sub_movie_id) 
join artist_data on (artist_movie_data.artist_id= artist_data.artist_id);
    END;
$$ LANGUAGE plpgsql;



____________________________________________________________________________________________


UPDATE sub_movie_rating_data
   SET 	 sub_movie_rating =(select  round(avg(user_movie_rating),0) as sub_movie_rating from user_movie_rating_data  where sub_movie_rating_data.sub_movie_id 
group by sub_movie_id order by sub_movie_id);


select  distinct user_movie_rating_data.sub_movie_id from user_movie_rating_data
left join sub_movie_rating_data on user_movie_rating_data.sub_movie_id = sub_movie_rating_data.sub_movie_id
where sub_movie_rating_data.sub_movie_id is null;

select * from sub_movie_rating_data where sub_movie_id = 15 ;


create or replace function check_and_user_rating_wrt_sub_mv_rating(smid integer) returns varchar as $$
declare
data record ;

begin

select * from into data sub_movie_rating_data where sub_movie_id = smid ;

return data ;

EXCEPTION WHEN OTHERS THEN
return 'False' ;

END;
$$ LANGUAGE plpgsql;

__________________________________________________________________________________________________

create or replace function check_sub_movieid_in_both_rating_tables( smid integer) returns varchar as $$
declare
data varchar ;
res varchar ;

begin
 PERFORM 1 FROM sub_movie_rating_data  WHERE sub_movie_id = smid;
  IF FOUND THEN
      return 'True';    
  ELSE
      return 'False';
 END IF;

EXCEPTION WHEN OTHERS THEN
return 'False' ;
END;
$$ LANGUAGE plpgsql;


____________________________________________________________________________________________________________________________________


sequence delete movies

1]
CREATE OR REPLACE FUNCTION get_sub_movie_id_and_seq(smid integer) RETURNS TABLE(mid integer, sm_sq integer) AS $$
    BEGIN
    RETURN QUERY select 
sub_movie_data.movie_id , 
sub_movie_data.sub_movie_sequel_number
from sub_movie_data 
where 
sub_movie_data.sub_movie_id = smid;
   END;
$$ LANGUAGE plpgsql;

2]

CREATE OR REPLACE FUNCTION get_sub_movie_data_based_on_id_and_seq(mid integer , mv_seq_no integer) RETURNS TABLE(smid integer) AS $$
    BEGIN
    RETURN QUERY select 
sub_movie_data.sub_movie_id 
from sub_movie_data 
where 
sub_movie_data.movie_id = mid and sub_movie_data.sub_movie_sequel_number >= mv_seq_no ;
   END;
$$ LANGUAGE plpgsql;


3]
CREATE OR REPLACE FUNCTION delete_all_movie_related_data_based_on_smid(smid integer)returns varchar as $$
declare
status varchar;
begin
DELETE from user_movie_track_data WHERE sub_movie_id IN (smid);
DELETE from user_movie_rating_data WHERE sub_movie_id IN (smid);
DELETE from sub_movie_rating_data WHERE sub_movie_id IN (smid);
DELETE from sub_movie_rating_data WHERE sub_movie_id IN (smid);
DELETE from artist_movie_data WHERE sub_movie_id IN (smid);
DELETE from sub_movie_data WHERE sub_movie_id IN (smid);

status= 'True';
return status;
EXCEPTION WHEN OTHERS THEN
status='False';
return status ;

end;
$$ language plpgsql

____________________________________________________________________________________________________________________________________

CREATE OR REPLACE FUNCTION get_movie_ids_based_on_rating_ids(umrid integer ) RETURNS TABLE(smid integer) AS $$
    BEGIN
    RETURN QUERY select sub_movie_id 
from user_movie_rating_data
where 
user_movie_rating_id = umrid ;
   END;
$$ LANGUAGE plpgsql;

select * from get_movie_ids_based_on_rating_ids(48)


____________________________________________________________________________________________________________________________________
CREATE OR REPLACE FUNCTION check_if_if_only_one_rating_left(smid integer ) RETURNS TABLE(count integer) AS $$
    BEGIN
    RETURN QUERY select count(sub_movie_id )
from user_movie_rating_data
where 
sub_movie_id = smid ;
   END;
$$ LANGUAGE plpgsql;

