from itertools import count
from nntplib import ArticleInfo
from pydoc import describe
from django.shortcuts import render
import psycopg2
# from psycopg2.extensions import JSON
import json
from MovieSet.Config import config
import cx_Oracle
from django.http import HttpResponse
import ast
from ast import literal_eval as make_tuple
from ast import literal_eval
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import  pandas

@csrf_exempt
def add_movie_rating_data(request):

    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_id = body['user_id']   
        sub_movie_id = body['sub_movie_id']
        user_movie_rating = body['user_movie_rating']

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)    
        print(conn)       
		
        # create a cursor
        cur = conn.cursor()

        cur.execute("select * from check_sub_movieid_in_both_rating_tables(cast(%s as integer));",(sub_movie_id,));
        r = cur.fetchall()
        print(r[0][0])

        if r[0][0]!='True':
            cur.execute("select get_max_sub_movie_rating_data_id();")
            sub_movie_rating_id = cur.fetchone()
            sub_movie_rating_id = sub_movie_rating_id[0]
            print(sub_movie_rating_id)
      
            cur.execute("select add_sub_movie_rating_data(cast(%s as integer),cast(%s as integer), cast(%s as integer) );",(sub_movie_rating_id,sub_movie_id,user_movie_rating,));
            row = cur.fetchall()
            print(row[0][0])


        cur.execute("select update_avg_sub_movie_rating();");
        res = cur.fetchall()
        print(res[0][0])
        if res[0][0]!='True':
            print("Rating did not update")
        else:
            print("Rating updated")

        #get max_id before query
        cur.execute("select get_max_user_movie_rating_data_id();")
        user_movie_rating_id = cur.fetchone()
        user_movie_rating_id = user_movie_rating_id[0]
        print(user_movie_rating_id)
      
        cur.execute("select add_movie_rating_data (cast(%s as integer),cast(%s as integer), cast(%s as integer), cast(%s as integer) );",(user_movie_rating_id,user_id,sub_movie_id,user_movie_rating))
        row = cur.fetchall()
        print(row[0][0])
        
        if row[0][0]!= 'True':
            print('Please check the Database Operation !')
            msg =  row[0][0]
            user['status'] = 'failure'
            user['msg']=msg
            response = HttpResponse(json.dumps(user),content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response
            
        else:

            print('The user has been added successfully !')
            msg =  row[0][0]
            user['status'] = 'success'
            user['msg']=msg
            response = HttpResponse(json.dumps(user),content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response 
    
	# close the communication with the PostgreSQL
        
    except IndexError as e:
        #print(e)
        user['status']='failure'
        user['msg']= str(e)
        return HttpResponse(json.dumps(user),content_type="application/json")
    except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
        user['status']='failure'
        user['msg']= str(error)
        return HttpResponse(json.dumps(user),content_type="application/json")
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
                
    

def get_movie_rating_data_by_id(request,rating_id):
    user={}
    json_data=[]
    if request.method == "GET":
        umti  = rating_id

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)    
        print(conn)       
        
        # create a cursor
        cur = conn.cursor()

        #exceute cursor
        cur.execute("select get_movie_rating_data_by_id(cast(%s as integer));",(umti,));
        row = cur.fetchmany() 
        mt= make_tuple(str(row[0]))[0].strip(r'()').split(",")
        #print(mt)

        ratingdata= json.dumps(mt)
        ratingdata = ratingdata.replace('\\"', '')
        ratingdata=  json.loads(ratingdata)
        #artistdata= json.dumps(artistdata)
        print(ratingdata)

        df = pandas.DataFrame(ratingdata)
        df=df.T
        df.columns = ["umrid", "uid", "smid" ,"umr"]
        js = df.to_json(orient = 'records')
        json_data = js.replace('\\"', '')
        json_data =json.loads(json_data)


        if mt[0]== '':
            print('Please check the Username and Password again !')
            user['status']='failure'
            user['rating_data']=None
            user= json.dumps(user,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
            user= json.loads(user)
            user=  json.dumps(user)
            response = HttpResponse(user,content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response
            
        else:
            print('Retrived the Artist data successfully !') 
            user['rating_data']=json_data
            user['status'] = 'success'
            user= json.dumps(user,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
            user= json.loads(user)
            user=  json.dumps(user)
            response = HttpResponse(user,content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response

    # close the communication with the PostgreSQL
        
    except IndexError as e:
        #print(e)
        user['status']='failure'
        user['msg']= str(e)
        return HttpResponse(json.dumps(user),content_type="application/json")
    except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
        user['status']='failure'
        user['msg']= str(error)
        return HttpResponse(json.dumps(user),content_type="application/json")
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


@csrf_exempt
def delete_movie_rating_data(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        umtid = body['rating_id']

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)    
        print(conn)       
        
        # create a cursor
        cur = conn.cursor()

        cur.execute("select * from get_movie_ids_based_on_rating_ids(cast(%s as integer));",(umtid,))
        smid= cur.fetchall()
        smid=smid[0]
        print(smid[0])

        cur.execute("select * from check_if_if_only_one_rating_left(cast(%s as integer));",(smid,))
        rating_data= cur.fetchall()
        rating_data=rating_data[0]
        print(rating_data)
        print(len(rating_data))

        if len(rating_data)==1:
            cur.execute("DELETE from sub_movie_rating_data WHERE sub_movie_id = %s",(smid,))

        #exceute cursor
        cur.execute("select delete_movie_rating_data(cast(%s as integer));",(umtid,));
        row = cur.fetchall()
        print(row[0][0])    
       
        cur.execute("select update_avg_sub_movie_rating();");
        res = cur.fetchall()
        print(res[0][0])
        if res[0][0]!='True':
            print("Rating did not update")
        else:
            print("Rating updated")


        if row[0][0]!= 'True':
            print('Please check the Username and Password again !')
            msg =  row[0][0]
            user['status'] = 'failure'
            user['msg']=msg
            response = HttpResponse(json.dumps(user),content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response
            
        else:
            print('The user has been deleted successfully !')
            msg =  row[0][0]
            user['status'] = 'success'
            user['msg']=msg
            response = HttpResponse(json.dumps(user),content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response 
    
    # close the communication with the PostgreSQL
        
    except IndexError as e:
        #print(e)
        user['status']='failure'
        user['msg']= str(e)
        return HttpResponse(json.dumps(user),content_type="application/json")
    except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
        user['status']='failure'
        user['msg']= str(error)
        return HttpResponse(json.dumps(user),content_type="application/json")
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


@csrf_exempt
def update_movie_rating_data(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        umtid = body['user_movie_rating_id']
        uid = body['user_id']   
        smid = body['sub_movie_id']
        umr = body['user_movie_rating']
        

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)    
        print(conn)       
		
        # create a cursor
        cur = conn.cursor()


        cur.execute("select update_avg_sub_movie_rating();");
        res = cur.fetchall()
        print(res[0][0])
        if res[0][0]!='True':
            print("Rating did not update")
        else:
            print("Rating updated")


        cur.execute("select update_movie_rating_data(cast(%s as integer),cast(%s as integer), cast(%s as integer),cast(%s as integer) );",(umtid,uid,smid,umr));
        row = cur.fetchmany()
        print(row[0][0])
        
        if row[0][0]!= 'True':  
            print('Please check the Database Operation !')
            msg =  row[0][0]
            user['status'] = 'failure'
            user['msg']=msg
            response = HttpResponse(json.dumps(user),content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response 
            
        else:

            print('The user has been added successfully !')
            msg =  row[0][0]
            user['status'] = 'success'
            user['msg']=msg
            response = HttpResponse(json.dumps(user),content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response 
    
	# close the communication with the PostgreSQL
        
    except IndexError as e:
        #print(e)
        user['status']='failure'
        user['msg']= str(e)
        return HttpResponse(json.dumps(user),content_type="application/json")
    except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
        user['status']='failure'
        user['msg']= str(error)
        return HttpResponse(json.dumps(user),content_type="application/json")
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')



def get_all_movie_rating_data(request):
    user={}
    json_data=[]
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)    
        print(conn)       
        
        # create a cursor
        cur = conn.cursor()

        cur.execute("select update_avg_sub_movie_rating();");
        res = cur.fetchall()
        print(res[0][0])
        if res[0][0]!='True':
            print("Rating did not update")
        else:
            print("Rating updated")


        #exceute cursor
        cur.execute("""select 
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
join  movie_data on (sub_movie_data .movie_id = movie_data.movie_id);""");
  
        row_header=[x[0] for x in cur.description]
        row = cur.fetchall()
        for result in row:
            json_data.append(dict(zip(row_header,result)))
            json_data =json.dumps(json_data,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
            json_data = json_data.replace('\\"', '')
            json_data =json.loads(json_data)
        
        if row[0]== '':
            print('Please check the Username and Password again !')
            user['status']='failure'
            user['artist_data']=None
            response = HttpResponse(user,content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response
            
        else:
            print('Retrived the Artist data successfully !')     
            user['rating_data']=json_data
            user['status'] = 'success'
            user= json.dumps(user,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
            user= json.loads(user)
            user=  json.dumps(user)
            response = HttpResponse(user,content_type="application/json")

            response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
            response["Cross-Origin-Opener-Policy"] = '*'   
            response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
            response["Access-Control-Max-Age"] = '1000'
            response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
            conn.commit()
            cur.close()
            return response

    
    # close the communication with the PostgreSQL
        
    except IndexError as e:
        #print(e)
        user['status']='failure'
        user['msg']= str(e)
        return HttpResponse(json.dumps(user),content_type="application/json")
    except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
        user['status']='failure'
        user['msg']= str(error)
        return HttpResponse(json.dumps(user),content_type="application/json")
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


