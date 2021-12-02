import streamlit as st
import pandas as pd
import hashlib
import sqlite3 

class auth():
    def __init__(self) -> None:
        # DB Management
        self.conn = sqlite3.connect('user_data.db')
        self.c = self.conn.cursor()
        self.Login_status = False
        pass
    
    def make_hashes(self,password):
        return hashlib.sha256(str.encode(password)).hexdigest()

    def check_hashes(self,password,hashed_text):
        if self.make_hashes(password) == hashed_text:
            return hashed_text
        return False

    # DB  Functions
    def create_usertable(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

    def add_userdata(self,username,password):
        self.c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
        self.conn.commit()

    def login_user(self,username,password):
        self.c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
        data = self.c.fetchall()
        return data

    def view_all_users(self):
        self.c.execute('SELECT * FROM userstable')
        data = self.c.fetchall()
        return data

    def getLoginStatus(self):
        return self.Login_status
    
    def auth_run(self):

        menu = ["SignUp","Login"]
        choice = st.sidebar.selectbox("Menu",menu)

        if choice == "Login":
            #st.subheader("Login um diese exelente App zu nutzen!")
            username = st.sidebar.text_input("User Name")
            password = st.sidebar.text_input("Password",type='password')
            if st.sidebar.checkbox("Login"):
                
                # if password == '12345':
                self.create_usertable()
                hashed_pswd = self.make_hashes(password)

                result = self.login_user(username,self.check_hashes(password,hashed_pswd))
                if result:

                    #st.success("Logged In as {}".format(username))
                    
                    self.Login_status = True
                    # task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
                    # if task == "Add Post":
                    #     st.subheader("Add Your Post")

                    # elif task == "Analytics":
                    #     st.subheader("Analytics")
                    # elif task == "Profiles":
                    #     st.subheader("User Profiles")
                    #     user_result = self.view_all_users()
                    #     clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
                    #     st.dataframe(clean_db)
                else:
                    st.warning("Incorrect Username/Password")
                   

        elif choice == "SignUp":
            st.subheader("Hier kann ein neuer Account angeegt werden ...")
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')

            if st.button("Signup"):
                self.create_usertable()
                self.add_userdata(new_user,self.make_hashes(new_password))
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")
