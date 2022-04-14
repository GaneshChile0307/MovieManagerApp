from nntplib import ArticleInfo
from pickle import TRUE
from pydoc import describe
import re
from django.shortcuts import render
import pandas
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


@csrf_exempt
def add_sub_movie_data(request):

    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        sub_movie_name = body['sub_movie_name']   
        movie_id = body['movie_id']
        sub_movie_descrip =  body['sub_movie_descrip']
        sub_movie_category = body['sub_movie_category']
        sub_movie_sequel_number = body['sub_movie_sequel_number']
       
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
        cur.execute("select get_max_sub_movie_data_id();")
        maxid = cur.fetchone()
        maxid = maxid[0]
      
        cur.execute("select add_sub_movie_data(cast(%s as integer),cast(%s as varchar), cast(%s as integer) , cast(%s as varchar), cast(%s as varchar), cast (%s as integer));",(maxid,sub_movie_name,movie_id,sub_movie_descrip,sub_movie_category,sub_movie_sequel_number));
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
                
    

def get_sub_movie_data_by_id(request,sub_movie_id):
    user={}
    json_data=[]
    if request.method == "GET":
        smid  = sub_movie_id

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
        cur.execute("select * from  get_sub_movie_data_by__id(cast(%s as integer));",(smid,))

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
            user['sub_movie_data']=None
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
            user['sub_movie_data']=json_data
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
def delete_sub_movie_data(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        smid = body['artist_id']

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
        cur.execute("select delete_sub_movie_data(cast(%s as integer));",(smid,));
        row = cur.fetchmany()
        print(row[0][0])    
       
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
def update_sub_movie_data(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        sub_movie_id = body['sub_movie_id']
        sub_movie_name = body['sub_movie_name']   
        movie_id = body['movie_id']
        sub_movie_descrip =  body['sub_movie_descrip']
        sub_movie_category = body['sub_movie_category']
        sub_movie_sequel_number = body['sub_movie_sequel_number']

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
      
        cur.execute("select update_sub_movie_data(cast(%s as integer),cast(%s as varchar), cast(%s as integer) , cast(%s as varchar), cast(%s as varchar), cast(%s as  integer));",(sub_movie_id,sub_movie_name,movie_id,sub_movie_descrip,sub_movie_category,sub_movie_sequel_number));
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



# def get_all_sub_movie_data(request):
#     user={}
#     json_data=[]
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)    
#         print(conn)       
        
#         # create a cursor
#         cur = conn.cursor()

#         #exceute cursor
#         cur.execute("""SELECT * FROM "public"."sub_movie_data";""");
#         records = cur.fetchall() 

#         df = pandas.DataFrame(records)
        
#         df.columns = ["smid", "smn", "mid" ,"smdescp","smcateg","smseq","ts"]
#         js = df.to_json(orient = 'records')
#         json_data = js.replace('\\"', '')
#         json_data =json.loads(json_data)
        
#         if records[0]== '':
#             print('Please check the Username and Password again !')
#             user['status']='failure'
#             user['sub_movie_data']=None
#             response = HttpResponse(user,content_type="application/json")

#             response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
#             response["Cross-Origin-Opener-Policy"] = '*'   
#             response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
#             response["Access-Control-Max-Age"] = '1000'
#             response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
#             conn.commit()
#             cur.close()
#             return response
            
#         else:
#             print('Retrived the Artist data successfully !')     
#             user['sub_movie_data']=json_data
#             user['status'] = 'success'
#             user= json.dumps(user,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
#             user= json.loads(user)
#             user=  json.dumps(user)
#             response = HttpResponse(user,content_type="application/json")

#             response["Access-Control-Allow-Origin"] = 'http://localhost:8000/', '*'
#             response["Cross-Origin-Opener-Policy"] = '*'   
#             response["Access-Control-Allow-Methods"] ='GET,POST,OPTIONS,DELETE,PUT',
#             response["Access-Control-Max-Age"] = '1000'
#             response["Access-Control-Allow-Headers"] = 'X-Requested-With, Content-Type'
#             conn.commit()
#             cur.close()
#             return response

    
#     # close the communication with the PostgreSQL
        
#     except IndexError as e:
#         #print(e)
#         user['status']='failure'
#         user['msg']= str(e)
#         return HttpResponse(json.dumps(user),content_type="application/json")
#     except (Exception, psycopg2.DatabaseError) as error:
#         #print(error)
#         user['status']='failure'
#         user['msg']= str(error)
#         return HttpResponse(json.dumps(user),content_type="application/json")
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


def get_all_sub_movie_data(request):
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
        cur.execute("""select sub_movie_data.* ,
                    movie_data.movie_name ,
                    movie_data.movie_description
                    FROM sub_movie_data
                    left join
                    movie_data
                    on
                    sub_movie_data.movie_id= movie_data.movie_id;""")

        row_header=[x[0] for x in cur.description]
        row = cur.fetchall()
        df = pandas.DataFrame(row)
        df.columns = row_header

        df.groupby('movie_id')['sub_movie_sequel_number'].count().sort_values(ascending=True)
        print(df)

        js = df.to_json(orient = 'records')
        json_data = js.replace('\\"', '')
        json_data =json.loads(json_data)
   
        if row[0]== '':
            print('Please check the Username and Password again !')
            user['status']='failure'
            user['sub_movie_data']=None
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
            user['sub_movie_data']=json_data
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