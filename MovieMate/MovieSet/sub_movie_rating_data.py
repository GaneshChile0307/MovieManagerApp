from nntplib import ArticleInfo
from pydoc import describe
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
def add_sub_movie_rating_data(request):

    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        sub_movie_id = body['sub_movie_id']
        sub_movie_rating = body['sub_movie_rating']

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

        #get max_id before query
        cur.execute("select get_max_sub_movie_rating_data_id();")
        sub_movie_rating_id = cur.fetchone()
        sub_movie_rating_id = sub_movie_rating_id[0]
        print(sub_movie_rating_id)
      
        cur.execute("select add_sub_movie_rating_data(cast(%s as integer),cast(%s as integer), cast(%s as integer) );",(sub_movie_rating_id,sub_movie_id,sub_movie_rating,));
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
                
    

def get_sub_movie_rating_data_by_id(request,sub_movie_rating_id):
    user={}
    json_data=[]
    if request.method == "GET":
        smtid  = sub_movie_rating_id

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
        cur.execute("select get_sub_movie_rating_data_by_id(cast(%s as integer));",(smtid,));
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
        df.columns =["smrid", "smid", "smr"]
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
def delete_sub_movie_rating_data(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        smtid = body['sub_movie_rating_id']

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
        cur.execute("select delete_sub_movie_rating_data(cast(%s as integer));",(smtid,));
        row = cur.fetchall()
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
            cur.execute("select update_avg_sub_movie_rating();");
            res = cur.fetchall()
            print(res[0][0])
            if res[0][0]!='True':
                print("Rating did not update")
            else:
                print("Rating updated")
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
def update_sub_movie_rating_data(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        smtid = body['sub_movie_rating_id']  
        smid = body['sub_movie_id']
        smr = body['sub_movie_rating']
        

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
        
        cur.execute("select update_sub_movie_rating_data(cast(%s as integer),cast(%s as integer), cast(%s as integer) );",(smtid,smid,smr));
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
            
            cur.execute("select update_avg_sub_movie_rating();");
            res = cur.fetchall()
            print(res[0][0])
            if res[0][0]!='True':
                print("Rating did not update")
            else:
                print("Rating updated")
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



def get_all_sub_movie_rating_data(request):
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
        cur.execute("""SELECT * FROM "public"."sub_movie_rating_data";""");
        records = cur.fetchall() 

        df = pandas.DataFrame(records)
        
        df.columns = ["smrid", "smid", "smr"]
        js = df.to_json(orient = 'records')
        json_data = js.replace('\\"', '')
        json_data =json.loads(json_data)
        
        if records[0]== '':
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
            user['rating_gdata']=json_data
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
