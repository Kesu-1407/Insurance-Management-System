# import this
import streamlit as st
import pandas as pd
from PIL import Image
import time
from usermy import *

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()

def admin_logged(user_id,passw):
    if login_admin(user_id,passw):
        st.success("Logged in as admin")
        st.session_state['admin_loggedin'] =True
        st.session_state['admin_details'] = admin_details(user_id)
    # if user_id == passw:
    #     st.success("Logged in as admin")
    #     st.session_state['admin_loggedin'] =True
    else:
        st.warning("admin_id or password is wrong")

def add_admin_page():
    st.subheader("Enter new admin details")
    st.text("Admin id")
    nadmin_id=st.text_input(label=" ",type="default",placeholder="enter admin id",key =16)
    st.text("Branch id")
    nbranch_id=st.text_input(label=" ",type="default",placeholder="enter bank branch id",key =17)
    st.text("Admin name")
    nadmin_name=st.text_input(label=" ",type="default",placeholder="enter admin name",key =18)
    st.text("Number")
    nadmin_number=st.text_input(label=" ",type="default",placeholder="enter admin number",key =19,max_chars=10)
    st.text("Password")
    nadmin_password=st.text_input(label=" ",type="password",placeholder="create password for admin",key =20)
    st.button("Submit",key="new_admin",on_click=update_admin, args=(nadmin_id, nbranch_id, nadmin_name, nadmin_number, nadmin_password))

def add_agent_page():
    st.subheader("Enter new agent details")
    st.text("Agent id")
    nagent_id=st.text_input(label=" ",type="default",placeholder="enter agent id",key=21)
    st.text("Admin id")
    nadmin_id=st.text_input(label=" ",type="default",placeholder="enter your admin's id",key=22)
    st.text("Agent name")
    nagent_name=st.text_input(label=" ",type="default",placeholder="enter agent name",key=23)
    st.text("Number")
    nagent_number=st.text_input(label=" ",type="default",placeholder="enter phone number",key=24,max_chars=10)
    st.text("City")
    nagent_city=st.text_input(label=" ",type="default",placeholder="enter city",key=25)
    st.text("Password")
    nagent_password=st.text_input(label=" ",type="password",placeholder="create password for agent",key=26)
    # st.text("Admin's name")
    # nagentad_name=st.text_input(label=" ",type="default",placeholder="enter your admin's name",key=41)
    st.button("Submit", key="new_agent",on_click=update_agent, args=(nagent_id, nadmin_id,nagent_name,nagent_number,nagent_city,nagent_password))

def add_policy_holder():
    st.subheader("Enter the new policy holder details")
    st.text("Policy number")
    npolicy_number=st.text_input(label=" ",type="default",placeholder="enter the chosen policy number",key=27)
    st.text("Policy Holder Name")
    npolicyh_name=st.text_input(label=" ",type="default",placeholder="enter the name of the policy holder",key=28)
    st.text("Mobile number")
    npolicyh_number=st.text_input(label=" ",type="default",placeholder="enter the mobile number",key=29)
    # st.text("City")
    # npolicyh_city=st.text_input(label=" ",type="default",placeholder="enter city",key=30)
    st.text("Address")
    npolicyh_address=st.text_input(label=" ",type="default",placeholder="enter the address",key=31)
    st.text("Nominee Name")
    npolicyhn_name=st.text_input(label=" ",type="default",placeholder="enter the nominee's name",key=32)
    st.text("Nominee relation")
    npolicyhn_relation=st.text_input(label=" ",type="default",placeholder="enter the nominee relation",key=33)
    st.text("Gender")
    npolicyh_gender=st.text_input(label=" ",type="default",placeholder="enter Male,Female or other",key=34)
    st.text("DOB")
    npolicyh_age=st.text_input(label=" ",type="default",placeholder="enter the DOB as yyyy-mm-dd",key=35)
    st.text("Password")
    npolicyh_pass=st.text_input(label=" ",type="password",placeholder=" Create a new password",key=36,max_chars=10)
    st.text("Enter amount already deposited")
    npolicyh_dep=st.text_input(label=" ",type="default",placeholder=" Enter deposited amount",key=50)
    st.button("Submit",key='new_policyholder',on_click=update_policy_holder,args=(npolicy_number,npolicyh_name,npolicyh_number,npolicyh_address,npolicyhn_name,npolicyhn_relation,npolicyh_gender,npolicyh_age,npolicyh_pass,npolicyh_dep))



def admin_page():
    with mainSection:
        image = Image.open('admin_fam.jpeg')
        st.image(image)
        st.subheader(f"Welcome {st.session_state['admin_details'][0]}")
        choice=st.radio("Select the appropriate option",('View Admin List','Add new Admin','View Agent List','Add new Agent','View available plans'))
        if choice == 'View Admin List':
            st.text("This is admin list")
            df=pd.DataFrame(admin_table(),columns=('admin name','admin id','branch id','mobile number'))
            st.table(df)
        if choice == 'View Agent List':
            st.text("This is agent list:")
            df=pd.DataFrame(agent_table(),columns=('agent id','agent name','mobile number','city','admin name'))
            st.table(df)
        if choice == 'Add new Admin':
            add_admin_page()
        if choice == 'Add new Agent':
            add_agent_page()
        if choice == 'View available plans':
            st.text("The available plans are:")
            df=pd.DataFrame(plan_table(),columns=('plan no','plan name','MMA','max age','min age','min SA'))
            st.table(df)

def remove_policy_holder():
    st.text("Enter the policy holder's name want to remove")
    remove_name=st.text_input(label=" ",type="default",placeholder="enter the name",key=36)
    st.button("Confirm",key="done",on_click=remove_holder,args=(remove_name,))

            

def LoggedOut_Clicked():
    # st.session_state['loggedIn'] = False
    # st.session_state['details'] = None
    # st.session_state['checkout'] = False
    st.session_state['admin_loggedin'] = False
    st.session_state['agent_loggedin'] = False
    st.session_state['holder_loggedin'] = False
    st.session_state['admin_details'] =None
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)


def agent_page():
    with mainSection:
        image1 = Image.open('agent_fam.jpg')
        st.image(image1)
        st.subheader(f"Welcome {st.session_state['agent_details'][0]}")
        choice=st.radio('Chose the appropriate option',('View policy holders','Add a new policy holder','View plans','View Policies','Remove a policy holder'))
        if choice == 'View policy holders':
            st.text(f"The list of policy holders under {st.session_state['agent_details'][0]} are: ")
            df=pd.DataFrame(policy_holder_table(),columns=('policy no','name','number','address','nominee-name','nominee-relation','gender','DOB','amount paid'))
            st.table(df)
        if choice == 'View plans':
            st.text("The available plans are:")
            df=pd.DataFrame(plan_table(),columns=('plan no','plan name','MMA','max age','min age','min SA'))
            st.table(df)
        if choice == 'View Policies':
            st.text("The available policy schemes are:")
            df=pd.DataFrame(policy_table2(),columns=('policy no','plan no','DOC','mode','term','FUP','SA','premium'))
            st.table(df)
        if choice == 'Add a new policy holder':
            add_policy_holder()
        if choice == 'Remove a policy holder':
            remove_policy_holder()

def holder_page():
    with mainSection:
        image2 = Image.open('policy_holder_fam.jpg')
        st.image(image2)
        st.subheader(f"Welcome {st.session_state['holder_details'][1]}")
        
        ch=st.radio("Chose the appropriate option",("View my policy","View amount due and due date","Make Payment"))
        if ch == "View my policy":
            st.text("Your policy is:")
            #st.text(st.session_state['holder_details'][1])
            holder_df=pd.DataFrame(policy_holder_table2(st.session_state['holder_details'][0]),columns=('Policy number','Plan Number','DOC','mode','term','FUP','SA','premium','user_id'))
            st.table(holder_df)
        if ch == "View amount due and due date":
            amt , fup = view_amt_due(st.session_state['holder_details'][0],st.session_state['holder_details'][2])
            if amt == 'payment completed' :
                st.subheader('your Payment is completed ')
            else :
                st.subheader("Your Remaining amount is : Rs " + str(amt)+" which is due on "+ str(fup))
            #st.text("Due on " + str(fup))
        if ch == "Make Payment":
            tickers=('Select the below options','UPI','Credit Card','Debit Card','Net-Banking')
            choice=st.selectbox('How would you want to make the payment?',tickers)
            if choice == 'UPI':
                st.button("confirm payment",key="payment",on_click=paid,args=(st.session_state['holder_details'][2],))
            if choice == 'Credit Card':
                st.button("confirm payment",key="payment",on_click=paid,args=(st.session_state['holder_details'][2],))
            if choice == 'Debit Card':
                st.button("confirm payment",key="payment",on_click=paid,args=(st.session_state['holder_details'][2],))
            if choice == 'Net-Banking':
                st.button("confirm payment",key="payment",on_click=paid,args=(st.session_state['holder_details'][2],))

def paid(num):
    amount=payment_made(num)
    with st.spinner('Payment Processing.....'):
        time.sleep(4)
        st.success("Your payment of Rs "+str(amount)+" is successful and updated")

        

def agent_logged(id,passw):
    if login_agent(id,passw):
        st.success("Logged in as agent")
        st.session_state['agent_loggedin'] = True
        st.session_state['agent_details'] = agent_details(id)
    else:
        st.warning("agency_code or password is wrong")   

def holder_logged(id ,passw):
    if login_holder(id,passw):
        st.success("Logged in as Policy holder")
        st.session_state['holder_loggedin'] = True
        st.session_state['holder_details'] = policy_holder_details(id)
    else:
        st.warning("Name or password wrong")

def login_page():
    tab1,tab2,tab3=st.tabs(["Admin","Agent", "Policy Holder"])

    with tab1: 
        st.subheader("Admin")
        #st.form_submit_button("login")
        id=st.text_input(label="",type="default",placeholder="enter the admin id",key =12)
        passw=st.text_input(label ="",type="password",placeholder="enter password", key=13)
        st.button("login",on_click=admin_logged,args=(id,passw))

    with tab2:
        st.subheader("Agent")
        #st.form_submit_button("login")
        code=st.text_input("agency_code",type="default",placeholder="enter agent id", key =14)
        passw=st.text_input("password",type="password",placeholder="enter password", key =15)
        st.button("login",key="my_agentpass",on_click=agent_logged,args=(code,passw))

    with tab3: 
        st.subheader("Policy Holder")
        #st.form_submit_button("login")
        code=st.text_input("Name",type="default",placeholder="enter your name", key =16)
        passw=st.text_input("password",type="password",placeholder="enter password", key =17)
        st.button("login",key="my_holderpass",on_click=holder_logged,args=(code,passw))


with headerSection:
    st.title("Insurance Management System")
    if 'admin_loggedin' not in st.session_state:
        st.session_state['admin_loggedin'] = False
        login_page()

    if 'agent_loggedin' not in st.session_state:
        st.session_state['agent_loggedin'] = False
    if 'holder_loggedin' not in st.session_state:
        st.session_state['holder_loggedin'] = False
    else:
        if st.session_state['admin_loggedin'] == True :
            admin_page()
            show_logout_page()

        elif st.session_state['agent_loggedin'] ==True:
            agent_page()
            show_logout_page()

        elif st.session_state['holder_loggedin'] == True:
            holder_page()
            show_logout_page()

        elif st.session_state['admin_loggedin'] ==False:
            login_page()
        else:
            login_page()


