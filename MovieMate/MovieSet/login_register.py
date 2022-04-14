from django.shortcuts import render
import psycopg2
# from psycopg2.extensions import JSON
import json
from MovieSet.Config import config
import cx_Oracle
from django.http import HttpResponse
import ast
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder  
from ast import literal_eval as make_tuple
from ast import literal_eval
import json
import  pandas


@csrf_exempt
def register_user(request):

    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        firstname = body['firstname']   
        lastname = body['lastname']
        dateofbirth =  body['dateofbirth']
        gender = body['gender']
        phone = body['phone']
        email = body['email']
        address = body['address']
        city = body['city']
        password = body['password']
        usertype =  body['usertype']

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
        cur.execute("select getmaxuserdataid();")
        usermaxid = cur.fetchone()
        usermaxid = usermaxid[0]
      
        cur.execute("select RegisterUser(cast(%s as integer),cast(%s as varchar), cast(%s as varchar) , cast(%s as varchar), cast(%s as varchar), cast(%s as  varchar),  cast (%s as varchar), cast(%s as varchar), cast(%s as varchar),cast(%s as varchar),cast(%s as varchar));",(usermaxid,firstname,lastname,dateofbirth,gender,phone,email,address,city,password,usertype,));
        # cur.execute('CALL regsiteruser(%s,%s,%s,%s,%s,%s,%s,%s)',(firstname,lastname,dateofbirth,address,phone,email,password,usertype))
        # process the result set
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
            print('The user has registered in database!')
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
def login_user(request):
   
    #user={}
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']   
        password = body['password']

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
        cur.execute("select LoginUser(%s,%s);",(username,password));
        row = cur.fetchmany()
        print(row[0][0])    

        if row[0][0]!= 'True':
            print('Please check the Username and Password again !')
            err =  row[0][0]
            user['user_type']=None
            user['status'] = 'failure'
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
            print('The user has Logged in !')

            cur.execute("select LoginUserType(%s );",(username,));
            usertype = cur.fetchmany()
            user['user_type']=usertype[0][0]
            user['status'] = 'success'
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



def get_user_details_by_id(request,user_id):
    user={}
    json_data=[]
    if request.method == "GET":
        uid  = user_id

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
        cur.execute("select getuserdetailsbyid(cast(%s as integer));",(uid,));
        row = cur.fetchmany() 
        mt= make_tuple(str(row[0]))[0].strip(r'()').split(",")
        #print(mt)

        userdata= jsonStr = json.dumps(mt)
        userdata = userdata.replace('\\"', '')
        userdata=  json.loads(userdata)
        #artistdata= json.dumps(artistdata)
        print(userdata)

        df = pandas.DataFrame(userdata)
        df=df.T
        df.columns = ["uid", "fn", "ln" ,"dob","ug","ucn","email","cntry","cty","pass","type","ts"]
        js = df.to_json(orient = 'records')
        json_data = js.replace('\\"', '')
        json_data =json.loads(json_data)

        if mt[0]== '':
            print('Please check the Username and Password again !')
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
            print('Retrived the Artist data successfully !') 
            user['user_data']=json_data
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



def get_user_details_by_email(request):
    user={}
    json_data=[]
    if request.method == "GET":
        print(request.GET['email'])
        em = request.GET['email']   
        

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
        cur.execute("select getuserdetailsby_email(cast(%s as varchar));",(em,));
        row = cur.fetchmany() 
        mt= make_tuple(str(row[0]))[0].strip(r'()').split(",")
        #print(mt)

        userdata= jsonStr = json.dumps(mt)
        userdata = userdata.replace('\\"', '')
        userdata=  json.loads(userdata)
        #artistdata= json.dumps(artistdata)
        print(userdata)

        df = pandas.DataFrame(userdata)
        df=df.T
        df.columns = ["uid", "fn", "ln" ,"dob","ug","ucn","email","cntry","cty","pass","type","ts"]
        js = df.to_json(orient = 'records')
        json_data = js.replace('\\"', '')
        json_data =json.loads(json_data)

        if mt[0]== '':
            print('Please check the Username and Password again !')
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
            print('Retrived the Artist data successfully !') 
            user['user_data']=json_data
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