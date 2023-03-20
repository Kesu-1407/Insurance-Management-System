import mysql.connector
import streamlit as st

con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jupy1298',
    database='insurance'
)

mycur=con.cursor()

def login_admin(id,password):
    mycur.execute(f"SELECT password FROM admin WHERE admin_id= '{id}'")
    entries = mycur.fetchone()
    passw=entries[0]
    print(passw)
    if passw==password:
        return True
    else:
        return False

def login_agent(code,password):
    mycur.execute(f"SELECT password FROM agent WHERE agent_id='{code}'")
    ent=mycur.fetchone()
    passw=ent[0]
    if passw==password:
        return True
    else:
        return False

def login_holder(code,password):
    mycur.execute(f"SELECT password FROM policy_holder WHERE name='{code}'")
    ent=mycur.fetchone()
    passw=ent[0]
    if passw==password:
        return True
    else:
        return False
print(login_holder('Shreya', 'Shreya'))

def admin_details(id):
    mycur.execute(f"SELECT name,admin_id,branch_id,number FROM admin WHERE admin_id='{id}'")
    entry=mycur.fetchall()
    return(entry[0][0], entry[0][1],entry[0][2],entry[0][3])

def policy_holder_details(id):
    mycur.execute(f"SELECT user_id , name ,policy_number ,number, amt_paid   FROM policy_holder WHERE name='{id}'")
    entry=mycur.fetchall()
    return(entry[0][0], entry[0][1],entry[0][2],entry[0][3], entry[0][4])

def policy_holder_table2(userid):
    #policy table 
    mycur.execute(f"SELECT p.policy_number,p.plan_no,p.DOC, p.mode,p.term,p.FUP,p.SA,p.premium,ph.user_id FROM policy p,policy_holder ph WHERE user_id={userid} AND p.policy_number = ph.policy_number")
    event = mycur.fetchall()
    return(event)

def view_amt_due(userid,pnumber):
    mycur.execute(f"SELECT premium FROM policy WHERE policy_number ={pnumber} ")
    premium = mycur.fetchone()
    mycur.execute(f"SELECT amt_paid FROM policy_holder WHERE user_id = {userid}")
    amt = mycur.fetchone()
    mycur.execute(f"SELECT FUP from policy WHERE policy_number= {pnumber}")
    fu = mycur.fetchone()
    f = fu[0]
    if amt[0] == 'payment completed':
        return amt[0], f
    a = premium[0]-int(amt[0])
    return a,f

def payment_made(nid):
    mycur.execute(f"SELECT premium FROM policy WHERE policy_number ={nid} ")
    premium = mycur.fetchone()
    mycur.execute(f"SELECT amt_paid FROM policy_holder WHERE policy_number = {nid}")
    amt = mycur.fetchone()
    a = premium[0]-int(amt[0])
    mycur.execute(f"UPDATE policy_holder SET amt_paid='payment completed' WHERE policy_number = {nid}")
    con.commit()
    return a
    


def agent_details(id):
    mycur.execute(f"SELECT name,admin_id,agent_id,number,city FROM agent WHERE agent_id='{id}'")
    entry=mycur.fetchall()
    return(entry[0][0], entry[0][1],entry[0][2],entry[0][3],entry[0][4])

def admin_table():
    mycur.execute("SELECT name,admin_id,branch_id,number FROM admin")
    enter=mycur.fetchall()
    return(enter)

def agent_table():
    mycur.execute("SELECT k.agent_id,k.name,k.number,k.city,n.name FROM agent k, admin n where k.admin_id=n.admin_id")
    enter=mycur.fetchall()
    return(enter)

def policy_table2():
    mycur.execute("SELECT policy_number,plan_no,DOC,mode,term,FUP,SA,premium FROM policy")
    enter=mycur.fetchall()
    return(enter)

def policy_holder_table():
    mycur.execute("SELECT policy_number,name,number,address,nominee_name,nominee_relation,gender,DOB,amt_paid FROM policy_holder")
    enter=mycur.fetchall()
    return(enter)

def update_admin(nadmin_id,nbranch_id, nadmin_name,nadmin_number,nadmin_password ):
    mycur.execute(f"INSERT into admin values('{nadmin_id}',{nbranch_id}, '{nadmin_name}',{nadmin_number},'{nadmin_password}')")
    con.commit()
    st.success('New Admin Added')

def update_agent(nagent_id,nadmin_id, nagent_name,nagent_number,nagent_city,nagent_password ):
    mycur.execute(f"INSERT into agent values('{nagent_id}','{nadmin_id}','{nagent_name}',{nagent_number},'{nagent_city}','{nagent_password}')")
    con.commit()
    st.success('New Agent added!')

def update_policy_holder(npolicy_number,npolicyh_name,npolicyh_number,npolicyh_address,npolicyhn_name,npolicyhn_relation,npolicyh_gender,npolicyh_age,npolicyh_pass,npolicyh_dep):
    mycur.execute(f"INSERT into policy_holder values({npolicy_number},{npolicyh_number},'{npolicyh_address}','{npolicyhn_name}','{npolicyhn_relation}','{npolicyh_gender}','{npolicyh_age}','{npolicyh_pass}',{npolicyh_dep},DEFAULT,'{npolicyh_name}')")
    con.commit()
    st.success('New policy holder added!')

def plan_table():
    mycur.execute("SELECT * FROM plan")
    enter=mycur.fetchall()
    return(enter)

def policy_table():
    mycur.execute("SELECT * FROM policy")
    enter=mycur.fetchall()
    return(enter)

def remove_holder(remove_name):
    print (remove_name)
    mycur.execute(f"DELETE FROM policy_holder where name='{remove_name}' ")
    con.commit()
    st.success('Policy holder has been successfully removed')
# mycur.execute(f"SELECT password FROM admin WHERE admin_id= 00011")
# entries = mycur.fetchone()
# for row in entries:
#     print(row)

#admin_name('Sejal@11')


print("connection established!")