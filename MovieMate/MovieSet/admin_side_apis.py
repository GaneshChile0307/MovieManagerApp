from asyncio.windows_events import NULL
from logging import exception
from nntplib import ArticleInfo
from pydoc import describe
from django.shortcuts import render
import psycopg2
# from psycopg2.extensions import JSON
import json
from MovieSet import movie_category_data
from MovieSet.Config import config
import cx_Oracle
from django.http import HttpResponse
import ast
from ast import literal_eval as make_tuple
from ast import literal_eval
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import time

# @csrf_exempt               
# def delete_artist_details_by_admin(request):
#     mvid=''
#     seq_no=''
#     user={}
#     if request.method == "POST":
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         aid=body['artist_id']

        
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


#         cur.execute("select sub_movie_id from artist_movie_data where artist_id = (cast(%s as integer));",(aid,))
#         res = cur.fetchall()
#         print(res)

#         if len(res)==0:
#             cur.execute("DELETE from artist_data WHERE artist_id IN (cast(%s as integer));",(aid,))
#             print('Retrived the deleted data successfully !') 
#             user['msg'] = "Records Not Deleted"
#             user['status'] = 'Failure'
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


        
#         if res[0]!='':
#             for r in res :
#                 cur.execute("select * from  get_sub_movie_id_and_seq (cast(%s as integer));",(r,))
#                 ress = cur.fetchall()
#                 mvid=ress[0][0]
#                 print(mvid)
#                 seq_no=ress[0][1]
#                 print(seq_no)
        
#                 cur.execute("select *  from get_sub_movie_data_based_on_id_and_seq (cast(%s as integer) , cast(%s as integer));",(mvid,seq_no))
#                 resss = cur.fetchall()
#             #print(resss)

#                 if resss[0]!='' :
#                     for r in resss:        
#                         for result in r:
#                             rec=result
#                             print(rec)
#                             print("Y")
#                             try:
                                
#                                 cur.execute("DELETE from artist_movie_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
                                
#                                 cur.execute("DELETE from user_movie_track_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
                                
#                                 #cur.execute("DELETE from user_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))

#                                 #cur.execute("DELETE from sub_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
                                
#                                 # cur.execute("DELETE from sub_movie_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
#                                 # cur.execute("select  delete_all_movie_related_data_based_on_smid (cast(%s as integer));",(rec,))
#                                 # a = cur.fetchall()

#                             #     if a[0][0]!= 'True':
#                             #         print("Error Deleting Records")
#                             #     else:
#                             #         print("Records Deleted")
#                             #             # except Exception as e:
#                             #             #     user['status']='failure'
#                             #             #     user['msg']= e
#                             #             #     print(e)
#                             #             #     return HttpResponse(json.dumps(user),content_type="application/json")
#                             except Exception as e:
#                                 user['status']='failure'
#                                 user['msg']= e
#                                 print(e)
#                                 return HttpResponse(json.dumps(user),content_type="application/json")   

#             # try:
                
#             #     cur.execute("DELETE from artist_data WHERE artist_id IN (cast(%s as integer));",(aid,))             

#             # except Exception as e:
#             #     user['status']='failure'
#             #     user['msg']= e
#             #     print(e)

#             #     return HttpResponse(json.dumps(user),content_type="application/json")
            


#         if res[0]== '':
#             print('Please check the Username and Password again !')
#             user['status']='failure'
#             user['msg']=None
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
            
#         else:
#             print('Retrived the Artist data successfully !') 
#             user['msg'] = "Records Deleted"
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
#         #return HttpResponse(row,content_type="application/json")
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



@csrf_exempt               
def delete_artist_details_by_admin(request):
    mvid=''
    seq_no=''
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        aid=body['artist_id']

        
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


        cur.execute("select sub_movie_id from artist_movie_data where artist_id = (cast(%s as integer));",(aid,))
        res = cur.fetchall()
        print(res)

        if len(res)==0:
            cur.execute("DELETE from artist_data WHERE artist_id IN (cast(%s as integer));",(aid,))
            print('Retrived the deleted data successfully !') 
            user['msg'] = "Records  Deleted"
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


        
        if res[0]!='':
            for r in res :
                try:
                    
                    cur.execute("DELETE from artist_movie_data WHERE sub_movie_id IN (cast(%s as integer));",(r,))
                    
                    cur.execute("DELETE from user_movie_track_data WHERE sub_movie_id IN (cast(%s as integer));",(r,))
                    
                    cur.execute("DELETE from user_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(r,))

                    #add avg movie raing function here
                    cur.execute("select update_avg_sub_movie_rating();");
                    resss = cur.fetchall()
                    print(resss[0][0])
                    if resss[0][0]!='True':
                        print("Rating did not update")
                    else:
                        print("Rating updated")

                    cur.execute("DELETE from sub_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(r,))
                    
                    cur.execute("DELETE from sub_movie_data WHERE sub_movie_id IN (cast(%s as integer));",(r,))
                    
                except Exception as e:
                    user['status']='failure'
                    user['msg']= e
                    print(e)
                    return HttpResponse(json.dumps(user),content_type="application/json")   

            try:
                
                cur.execute("DELETE from artist_data WHERE artist_id IN (cast(%s as integer));",(aid,))             

            except Exception as e:
                user['status']='failure'
                user['msg']= e
                print(e)

                return HttpResponse(json.dumps(user),content_type="application/json")
            


        if res[0]== '':
            print('Please check the Username and Password again !')
            user['status']='failure'
            user['msg']=None
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
            user['msg'] = "Records Deleted"
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
        #return HttpResponse(row,content_type="application/json")
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
def delete_movie_details_by_admin(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        aid=body['movie_id']

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)    
        print(conn)       
        
        #create a cursor
        cur = conn.cursor()
        cur.execute("select sub_movie_id from sub_movie_data where movie_id = (cast(%s as integer));",(aid,))
        res = cur.fetchall()
        print(res)

        if len(res)==0:
            cur.execute("DELETE from movie_data WHERE movie_id IN (cast(%s as integer));",(aid,))
            print('Retrived the deleted data successfully !') 
            user['msg'] = "Records  Deleted"
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

        if res[0]!='' :
            for result in res:
                rec=result[0]
                print(rec)
                try:
                    
                    cur.execute("DELETE from artist_movie_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
                    
                    cur.execute("DELETE from user_movie_track_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
                    
                    cur.execute("DELETE from user_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))
                    
                    cur.execute("DELETE from sub_movie_rating_data WHERE sub_movie_id IN (cast(%s as integer));",(rec,))

                    cur.execute("select update_avg_sub_movie_rating();");
                    resss = cur.fetchall()
                    print(resss[0][0])
                    if resss[0][0]!='True':
                        print("Rating did not update")
                    else:
                        print("Rating updated")
                    
            
                except Exception as e:
                    user['status']='failure'
                    user['msg']= e
                    print(e)
                    return HttpResponse(json.dumps(user),content_type="application/json")
        

            try:
                cur.execute("DELETE from sub_movie_data WHERE movie_id IN (cast(%s as integer));",(aid,))
                #time.sleep(1)
                cur.execute("DELETE from movie_data WHERE movie_id IN (cast(%s as integer));",(aid,))             
                #time.sleep(1)
             
            except Exception as e:
                user['status']='failure'
                user['msg']= e
                print(e)
                return HttpResponse(json.dumps(user),content_type="application/json")


        if res[0]== '':
            print('Please check the Username and Password again !')
            user['status']='failure'
            user['msg']=None
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
            user['msg'] = "Records Deleted"
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
def delete_sub_movie_details_by_admin(request):
    user={}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        smid=body['submovie_id']

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


        cur.execute("select * from  get_sub_movie_id_and_seq (cast(%s as integer));",(smid,))
        res = cur.fetchall()
        #print(res[0][0])
        mvid=res[0][0]
        #print(res[0][1])
        seq_no=res[0][1]

        cur.execute("select *  from get_sub_movie_data_based_on_id_and_seq (cast(%s as integer) , cast(%s as integer));",(mvid,seq_no))
        res = cur.fetchall()
        #print(res)

        if res[0]!='' :
            for result in res:
                rec=result[0]
                #print(rec)
                try:
                
                    cur.execute("select  delete_all_movie_related_data_based_on_smid (cast(%s as integer));",(rec,))
                    r = cur.fetchall()

                    if r[0][0]!= 'True':
                        print("Error Deleting Records")
                    else:
                        print("Records Deleted")

                except Exception as e:
                    user['status']='failure'
                    user['msg']= e
                    print(e)
                    return HttpResponse(json.dumps(user),content_type="application/json")
    


        if res[0]== '':
            print('Please check the Username and Password again !')
            user['status']='failure'
            user['msg']=None
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
            user['msg'] = "Records Deleted"
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