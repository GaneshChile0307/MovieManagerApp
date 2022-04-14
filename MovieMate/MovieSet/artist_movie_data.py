from nntplib import ArticleInfo
from pydoc import describe
from this import d
from django.shortcuts import render
import psycopg2
# from psycopg2.extensions import JSON
import json
from MovieSet.Config import config
#import cx_Oracle
from django.http import HttpResponse
import ast
from ast import literal_eval as make_tuple
from ast import literal_eval
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import pandas


@csrf_exempt
def add_artist_movie(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        submovieid = body['submovieid']   
        artistid = body['artistid']
        artisttype = body['artisttype']

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

        #get max_id before query
        cur.execute("select getmaxartistmovieid();")
        maxid = cur.fetchone()
        maxid = maxid[0]

        cur.execute("select add_artist_movie(cast(%s as integer), cast(%s as integer), cast(%s as integer), cast(%s as varchar));",(maxid,submovieid,artistid,artisttype));
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

            print('The artist movie data has been added successfully !')
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
                
    

def get_artist_movie_data_by_id(request,artist_movieid):
    user={}
    json_data=[]
    if request.method == "GET":
        amid  = artist_movieid
        

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
        cur.execute("""SELECT * FROM artist_movie_data where artist_movie_id = %s;""",(amid,))
        row_header=[x[0] for x in cur.description]
        row = cur.fetchall()
        for result in row:
            json_data.append(dict(zip(row_header,result)))
            json_data =json.dumps(json_data,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
            json_data = json_data.replace('\\"', '')
            json_data =json.loads(json_data)
        

        if row[0]== '':
            print('No artist movie data found !')
            user['status']='failure'
            user['artist_data']=None
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
            print('Retrived the Artist Movie data successfully !') 
            user['artist_moviedata']=json_data
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
def delete_artist_movie(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['artistmovieid']

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
        cur.execute("select deleteartistmoviedatabyid(cast(%s as integer));",(id,));
        row = cur.fetchall()
        print(row[0][0])    
       
        if row[0][0]!= 'True':
            print('Movie data not found !')
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
            print('The artist movie data has been deleted successfully !')
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
def update_artist_movie(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        artistmovieid = body['artistmovieid']
        submovieid = body['submovieid']   
        artistid = body['artistid']
        artisttype = body['artisttype']

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
      
        cur.execute("select updateartistmovie(cast(%s as integer),cast(%s as integer),cast(%s as integer),cast(%s as varchar));",(artistmovieid,submovieid,artistid,artisttype));
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

            print('The artist movie data has been deleted successfully !')
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



def get_all_artist_movie_data(request):
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

        #exceute cursor
        cur.execute("select * from get_all_artist_movie__data();");

        row_header=[x[0] for x in cur.description]
        row = cur.fetchall()
        df = pandas.DataFrame(row)
        df.columns = row_header

        new_df=df.groupby(["smid","sub_seq"]).apply(pandas.DataFrame.sort_values,'sub_seq' ,ascending=True)
        print(new_df)

        js = new_df.to_json(orient = 'records')
        json_data = js.replace('\\"', '')
        json_data =json.loads(json_data)


        if row[0]== '':
            print('Artist Movie record does not exist !')
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
            print('Retrived the Movie data successfully !') 
            user['artist_moviedata']=json_data
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
